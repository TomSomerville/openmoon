import bpy, bmesh, sys, numpy as np
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
PREVIEW = "preview" in args
D = r"C:\Users\Beached\Desktop\OpenMoon base terrain"
SCR = r"C:\Users\Beached\AppData\Local\Temp\claude\430f9eef4f5515e2\2f56ca85-f6f8-4853-b580-4acbc22428cd\scratchpad"
bpy.ops.wm.open_mainfile(filepath=D + r"\openmoon-primary-base.blend")
sc = bpy.context.scene

# --- swap terrain
old = bpy.data.objects["Terrain_primary_base"]
mat = old.data.materials[0]
old_me = old.data
bpy.data.objects.remove(old); bpy.data.meshes.remove(old_me)
bpy.ops.wm.ply_import(filepath=D + r"\mesh_20m.ply")
t = bpy.context.selected_objects[0]; t.name = "Terrain_primary_base"; t.data.name = "Terrain_primary_base"
t.data.materials.append(mat)
if hasattr(t.data, "shade_smooth"): t.data.shade_smooth()
for c in list(t.users_collection):
    if c != sc.collection: c.objects.unlink(t)
if t.name not in sc.collection.objects: sc.collection.objects.link(t)
tex = next(n for n in mat.node_tree.nodes if n.type == 'TEX_IMAGE')
old_img = tex.image
tex.image = bpy.data.images.load(D + r"\texture_2m.jpg")
bpy.data.images.remove(old_img)
print("TEXTURE", tex.image.filepath, "uv", [u.name for u in t.data.uv_layers])

# UV alignment check against the new heightmap
me = t.data
co = np.empty(len(me.vertices) * 3, np.float32); me.vertices.foreach_get("co", co); co = co.reshape(-1, 3)
uv = np.empty(len(me.loops) * 2, np.float32); me.uv_layers[0].data.foreach_get("uv", uv); uv = uv.reshape(-1, 2)
vi = np.empty(len(me.loops), np.int32); me.loops.foreach_get("vertex_index", vi)
hm = bpy.data.images.load(D + r"\heightmap_5m_16bit.png"); hm.colorspace_settings.name = "Non-Color"
w, h = hm.size; a = np.empty(w * h * 4, np.float32); hm.pixels.foreach_get(a); a = a.reshape(h, w, 4)[:, :, 0]
idx = np.random.default_rng(0).choice(len(uv), 100000, replace=False)
hv = a[np.clip((uv[idx, 1] * h).astype(int), 0, h - 1), np.clip((uv[idx, 0] * w).astype(int), 0, w - 1)] * 3601.49
print("UVCHECK corr", round(float(np.corrcoef(hv, co[vi[idx], 2])[0, 1]), 6), "bounds", co.min(0), co.max(0))
bpy.data.images.remove(hm)

bpy.context.view_layer.update()
dg = bpy.context.evaluated_depsgraph_get()
def ground(x, y):
    ok, loc, *_ = sc.ray_cast(dg, Vector((x, y, 10000)), Vector((0, 0, -1))); return loc.z

# --- move human and cameras by the same offset
human = bpy.data.objects["Human_1.8m"]
parts = list(human.children_recursive)
def foot():
    dg2 = bpy.context.evaluated_depsgraph_get(); P = []
    for o in parts:
        if o.type == 'MESH':
            e = o.evaluated_get(dg2); m = e.to_mesh(); P += [tuple(e.matrix_world @ v.co) for v in m.vertices]; e.to_mesh_clear()
    A = np.array(P); lo, hi = A.min(0), A.max(0); return Vector(((lo[0] + hi[0]) / 2, (lo[1] + hi[1]) / 2, lo[2])), hi[2] - lo[2]
f0, _ = foot()
z0 = ground(0, 0)
delta = Vector((0, 0, z0)) - f0
print("BASE_Z", round(z0, 2), "expected 2823.5", "DELTA", tuple(round(v, 2) for v in delta))
human.location += delta
cams = [o for o in sc.objects if o.type == 'CAMERA']
for c in cams: c.location += delta
bpy.context.view_layer.update()
f1, hgt = foot(); print("HUMAN foot", tuple(round(v, 2) for v in f1), "height", round(hgt, 3))
dg = bpy.context.evaluated_depsgraph_get()
for c in cams:
    print("CAM", c.name, tuple(round(v, 1) for v in c.location), "clearance", round(c.location.z - ground(c.location.x, c.location.y), 1))

# --- towers
towers = bpy.data.collections["Towers"]; exp = bpy.data.collections["Towers (expansion)"]
for o in list(towers.objects) + list(exp.objects):
    m = o.data; bpy.data.objects.remove(o); bpy.data.meshes.remove(m)
orange = bpy.data.materials["Tower_marker"]; cyan = bpy.data.materials["Tower_marker_mine"]
def mast(name, x, y, mat, col):
    me = bpy.data.meshes.new(name + "_mast"); bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=16, radius1=0.5, radius2=0.5, depth=10.0)
    bmesh.ops.translate(bm, verts=bm.verts, vec=(0, 0, 5.0)); bm.to_mesh(me); bm.free(); me.materials.append(mat)
    o = bpy.data.objects.new(name, me); col.objects.link(o); o.location = (x, y, ground(x, y))
    print("PLACED", name, tuple(round(v, 1) for v in o.location)); return o
for bn, mn, x, y, col in (("B1", "M1", -1059.9, -4396.5, towers), ("B2", "M2", -3338.9, -4216.8, towers),
                          ("B4", "M3", 5722.0, -7454.7, exp)):
    mast(bn, x - 10, y, orange, col); mast(mn, x + 10, y, cyan, col)
mast("B3", -1666.7, 1209.8, orange, towers)

# --- frame positions for the tower view labels
W, H = sc.render.resolution_x, sc.render.resolution_y
ct = bpy.data.objects["Cam_towers"]
pts = {n: bpy.data.objects[n].location for n in ("B1", "M1", "B2", "M2", "B3", "B4", "M3")}
pts["Base"] = Vector((0, 0, z0))
for n, p in pts.items():
    f = world_to_camera_view(sc, ct, p); print("FRAME", n, round(f.x * W), round((1 - f.y) * H))

# --- render
sc.cycles.samples = 32 if PREVIEW else 256
sc.render.resolution_percentage = 50 if PREVIEW else 100
out = SCR if PREVIEW else D
for cn, fn in (("Cam_close", "render_close.png"), ("Cam_wide", "render_wide.png"),
               ("Cam_overview", "render_overview.png"), ("Cam_towers", "render_towers.png")):
    sc.camera = bpy.data.objects[cn]; sc.render.filepath = out + "\\" + fn
    bpy.ops.render.render(write_still=True); print("RENDERED", fn)
sc.camera = bpy.data.objects["Cam_close"]
if not PREVIEW:
    bpy.ops.file.pack_all()
    print("PACKED", [(i.name, bool(i.packed_file)) for i in bpy.data.images])
    bpy.ops.wm.save_as_mainfile(filepath=D + r"\openmoon-primary-base.blend", compress=True); print("SAVED")
