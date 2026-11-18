import bpy, sys, math, numpy as np
from mathutils import Vector

args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
PREVIEW = "preview" in args
SUN_AZ = float(next((a.split("=")[1] for a in args if a.startswith("az=")), "250"))  # compass bearing the sun is IN (0=N/+Y, 90=E/+X)
D = r"C:\Users\Beached\Desktop\OpenMoon base terrain"

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.unit_settings.system = 'METRIC'
sc.unit_settings.scale_length = 1.0
sc.unit_settings.length_unit = 'METERS'

# --- terrain (README Option 1)
bpy.ops.wm.ply_import(filepath=D + r"\mesh_20m.ply")
terrain = bpy.context.selected_objects[0]
terrain.name = "Terrain_primary_base"
for p in terrain.data.polygons:
    pass
terrain.data.shade_smooth() if hasattr(terrain.data, "shade_smooth") else None

mat = bpy.data.materials.new("Regolith_LROC")
mat.use_nodes = True
nt = mat.node_tree
bsdf = nt.nodes["Principled BSDF"]
bsdf.inputs["Roughness"].default_value = 1.0
bsdf.inputs["Specular IOR Level"].default_value = 0.1
tex = nt.nodes.new("ShaderNodeTexImage")
tex.image = bpy.data.images.load(D + r"\texture_2m.jpg")
tex.interpolation = 'Cubic'
uvn = nt.nodes.new("ShaderNodeUVMap"); uvn.uv_map = "UVMap"
nt.links.new(uvn.outputs["UV"], tex.inputs["Vector"])   # alignment verified: no V flip needed
nt.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
terrain.data.materials.append(mat)

# --- surface height at base (raycast down at 0,0)
bpy.context.view_layer.update()
dg = bpy.context.evaluated_depsgraph_get()
def ground(x, y):
    ok, loc, nrm, *_ = sc.ray_cast(dg, Vector((x, y, 10000)), Vector((0, 0, -1)))
    return loc.z if ok else None
z0 = ground(0, 0)
print("SURFACE_Z", z0)

# --- human
bpy.ops.import_scene.gltf(filepath=D + r"\human\CesiumMan.glb")
imported = list(bpy.context.selected_objects)
roots = [o for o in imported if o.parent is None]
human = bpy.data.objects.new("Human_1.8m", None)
sc.collection.objects.link(human)
for r in roots:
    r.parent = human
sc.frame_set(1)
bpy.context.view_layer.update()
def mesh_bbox():
    dg2 = bpy.context.evaluated_depsgraph_get()
    pts = []
    for o in imported:
        if o.type == 'MESH':
            e = o.evaluated_get(dg2); m = e.to_mesh()
            pts += [e.matrix_world @ v.co for v in m.vertices]
            e.to_mesh_clear()
    a = np.array([tuple(p) for p in pts])
    return a.min(0), a.max(0)
lo, hi = mesh_bbox()
s = 1.8 / (hi[2] - lo[2])
human.scale = (s, s, s)
bpy.context.view_layer.update()
lo, hi = mesh_bbox()
cx, cy = (lo[0] + hi[0]) / 2, (lo[1] + hi[1]) / 2
human.location = (-cx, -cy, z0 - lo[2])
bpy.context.view_layer.update()
lo, hi = mesh_bbox()
print("HUMAN_BBOX", lo, hi, "height", hi[2] - lo[2])
# freeze the pose: drop the walk animation so it stays put on any frame
for o in imported:
    if o.animation_data:
        o.animation_data.action = None

# --- lighting: sun 2 deg above horizon, black world, no atmosphere
sun_data = bpy.data.lights.new("Sun", 'SUN')
sun_data.energy = float(next((a.split("=")[1] for a in args if a.startswith("e=")), "20"))
sun_data.angle = math.radians(0.53)
sun_data.use_shadow = False   # no cast shadows (terrain or human)
sun = bpy.data.objects.new("Sun_2deg", sun_data)
sc.collection.objects.link(sun)
# rotation (88deg about X) points light toward +Y (sun in the south); rz turns it to SUN_AZ
sun.rotation_euler = (math.radians(90 - 2), 0, math.radians(180 - SUN_AZ))
world = bpy.data.worlds.new("Space_black"); world.use_nodes = True
world.node_tree.nodes["Background"].inputs["Color"].default_value = (0, 0, 0, 1)
world.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.0
sc.world = world

# --- cameras
def make_cam(name, loc, target, lens):
    cd = bpy.data.cameras.new(name); cd.lens = lens; cd.clip_start = 0.1; cd.clip_end = 60000
    c = bpy.data.objects.new(name, cd); sc.collection.objects.link(c)
    c.location = loc
    c.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
    return c
chest = Vector((0, 0, z0 + 1.0))
# close: 15 m north-west of the human, eye height
ang = math.radians(SUN_AZ + 80)   # side-lit
cl = Vector((15 * math.sin(ang), 15 * math.cos(ang), 0)); cl.z = ground(cl.x, cl.y) + 1.6
close = make_cam("Cam_close_15m", cl, chest, 35)
# wide: 250 m away, looking past the human toward the crater side
wang = math.radians(float(next((a.split("=")[1] for a in args if a.startswith("wide=")), "0")))
wl = Vector((250 * math.sin(wang), 250 * math.cos(wang), 0)); wl.z = ground(wl.x, wl.y) + 6
wide = make_cam("Cam_wide_250m", wl, chest, 50)
for c in (close, wide):
    d = (chest - c.location)
    ok, loc, *_ = sc.ray_cast(bpy.context.evaluated_depsgraph_get(), c.location, d.normalized(), distance=d.length - 1.5)
    print("LOS", c.name, "blocked" if ok else "clear", "dist", round(d.length, 1))

# --- render settings
sc.render.engine = 'CYCLES'
cy = sc.cycles
try:
    prefs = bpy.context.preferences.addons["cycles"].preferences
    for t in ("OPTIX", "CUDA", "HIP", "ONEAPI"):
        try:
            prefs.compute_device_type = t; prefs.get_devices()
            if any(d.type == t for d in prefs.devices):
                for d in prefs.devices: d.use = True
                cy.device = 'GPU'; print("DEVICE", t); break
        except TypeError:
            pass
except Exception as e:
    print("GPU setup failed", e)
cy.samples = 32 if PREVIEW else 256
cy.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = 1920, 1080
sc.render.resolution_percentage = 50 if PREVIEW else 100
sc.render.image_settings.file_format = 'PNG'
sc.view_settings.view_transform = 'AgX'
sc.view_settings.exposure = 0.0

out = D if not PREVIEW else r"C:\Users\Beached\AppData\Local\Temp\claude\430f9eef4f5515e2\2f56ca85-f6f8-4853-b580-4acbc22428cd\scratchpad"
for c, fn in ((close, "render_close_15m.png"), (wide, "render_wide_250m.png")):
    sc.camera = c
    sc.render.filepath = out + "\\" + fn
    bpy.ops.render.render(write_still=True)
    print("RENDERED", sc.render.filepath)
sc.camera = close

if not PREVIEW:
    bpy.ops.file.pack_all()
    bpy.ops.wm.save_as_mainfile(filepath=D + r"\openmoon-primary-base.blend", compress=True)
    print("SAVED")
