import bpy, sys, math, numpy as np
from mathutils import Vector

args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
PREVIEW = "preview" in args
def arg(k, d): return float(next((a.split("=")[1] for a in args if a.startswith(k + "=")), d))
CLOSE_B = arg("close", 20)     # bearing of close camera from the human (deg, 0 = +Y north)
WIDE_B = arg("wide", 20)
OV_B = arg("ov", 216)
D = r"C:\Users\Beached\Desktop\OpenMoon base terrain"
SCR = r"C:\Users\Beached\AppData\Local\Temp\claude\430f9eef4f5515e2\2f56ca85-f6f8-4853-b580-4acbc22428cd\scratchpad"

bpy.ops.wm.open_mainfile(filepath=D + r"\openmoon-primary-base.blend")
sc = bpy.context.scene
terrain = bpy.data.objects["Terrain_primary_base"]
bpy.context.view_layer.update()
dg = bpy.context.evaluated_depsgraph_get()
def ground(x, y):
    ok, loc, *_ = sc.ray_cast(dg, Vector((x, y, 10000)), Vector((0, 0, -1)))
    return loc.z if ok else None

pts = {"Base": (596.0, 478.3, 2735.9), "B1": (4996.8, -6556.5, 3511.8), "B2": (6318.0, -6976.4, 3463.3),
       "B3": (-1070.7, 1688.1, 2353.9), "M1": (-463.9, -3918.2, 3272.4), "M2": (-2742.9, -3738.5, 3212.9)}
Z = {}
for k, (x, y, zc) in pts.items():
    Z[k] = ground(x, y)
    print("CHECK", k, round(Z[k], 2), "expected", zc, "diff", round(Z[k] - zc, 2))
BX, BY, BZ = pts["Base"][0], pts["Base"][1], Z["Base"]

# --- move human
human = bpy.data.objects["Human_1.8m"]
parts = [o for o in human.children_recursive]
def mesh_bbox():
    dg2 = bpy.context.evaluated_depsgraph_get(); P = []
    for o in parts:
        if o.type == 'MESH':
            e = o.evaluated_get(dg2); m = e.to_mesh()
            P += [tuple(e.matrix_world @ v.co) for v in m.vertices]; e.to_mesh_clear()
    a = np.array(P); return a.min(0), a.max(0)
lo, hi = mesh_bbox()
human.location += Vector((BX - (lo[0] + hi[0]) / 2, BY - (lo[1] + hi[1]) / 2, BZ - lo[2]))
bpy.context.view_layer.update()
lo, hi = mesh_bbox()
print("HUMAN", lo, hi, "height", round(hi[2] - lo[2], 3))

# --- tower markers
col = bpy.data.collections.get("Towers") or bpy.data.collections.new("Towers")
if col.name not in sc.collection.children: sc.collection.children.link(col)
tm = bpy.data.materials.get("Tower_marker") or bpy.data.materials.new("Tower_marker")
tm.use_nodes = True
b = tm.node_tree.nodes["Principled BSDF"]
b.inputs["Base Color"].default_value = (1.0, 0.45, 0.05, 1)
b.inputs["Emission Color"].default_value = (1.0, 0.45, 0.05, 1)
b.inputs["Emission Strength"].default_value = 30.0   # self-lit so 1 m masts show up from far away
for k in ("B1", "B2", "B3", "M1", "M2"):
    if k in bpy.data.objects: bpy.data.objects.remove(bpy.data.objects[k])
    me = bpy.data.meshes.new(k + "_mast")
    import bmesh
    bm = bmesh.new(); bmesh.ops.create_cone(bm, cap_ends=True, segments=16, radius1=0.5, radius2=0.5, depth=10.0)
    bmesh.ops.translate(bm, verts=bm.verts, vec=(0, 0, 5.0))   # origin at the foot
    bm.to_mesh(me); bm.free()
    me.materials.append(tm)
    o = bpy.data.objects.new(k, me); col.objects.link(o)
    o.location = (pts[k][0], pts[k][1], Z[k])

# --- cameras
def aim(c, loc, target):
    c.location = loc
    c.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
def cam(name, old=None, lens=35):
    c = bpy.data.objects.get(old) if old else None
    if c is None:
        c = bpy.data.objects.new(name, bpy.data.cameras.new(name)); sc.collection.objects.link(c)
    c.name = name; c.data.name = name; c.data.lens = lens; c.data.clip_start = 0.1; c.data.clip_end = 60000
    return c
def at(bearing, dist, up):
    r = math.radians(bearing); x, y = BX + dist * math.sin(r), BY + dist * math.cos(r)
    return Vector((x, y, ground(x, y) + up))
chest = Vector((BX, BY, BZ + 1.0))
close = cam("Cam_close", "Cam_close_15m", 35); aim(close, at(CLOSE_B, 15, 1.6), chest)
wide = cam("Cam_wide", "Cam_wide_250m", 50); aim(wide, at(WIDE_B, 250, 6), chest)
ov = cam("Cam_overview", None, 24)
r = math.radians(OV_B)
ov_loc = Vector((BX + 3000 * math.sin(r), BY + 3000 * math.cos(r), BZ + 1500))
mid = Vector(((BX + pts["B3"][0]) / 2, (BY + pts["B3"][1]) / 2, (BZ + Z["B3"]) / 2))
aim(ov, ov_loc, mid)
print("OV ground clearance", round(ov_loc.z - ground(ov_loc.x, ov_loc.y), 1))
dg = bpy.context.evaluated_depsgraph_get()
for c, tgt in ((close, chest), (wide, chest), (ov, chest), (ov, Vector((pts["B3"][0], pts["B3"][1], Z["B3"] + 5)))):
    d = tgt - c.location
    ok, *_ = sc.ray_cast(dg, c.location, d.normalized(), distance=d.length - 1.5)
    print("LOS", c.name, "->", tuple(round(v) for v in tgt[:2]), "blocked" if ok else "clear", round(d.length, 1))
# B3 and base inside overview frame?
from bpy_extras.object_utils import world_to_camera_view
sc.camera = ov
for k in ("Base", "B3"):
    p = world_to_camera_view(sc, ov, Vector((pts[k][0], pts[k][1], Z[k])))
    print("FRAME", k, round(p.x, 3), round(p.y, 3))

# --- render
sun = bpy.data.objects["Sun_2deg"]
print("SUN elev", round(90 - math.degrees(sun.rotation_euler.x), 2), "shadow", sun.data.use_shadow)
sc.cycles.samples = 32 if PREVIEW else 256
sc.render.resolution_percentage = 50 if PREVIEW else 100
out = SCR if PREVIEW else D
for c, fn in ((close, "render_close.png"), (wide, "render_wide.png"), (ov, "render_overview.png")):
    sc.camera = c; sc.render.filepath = out + "\\" + fn
    bpy.ops.render.render(write_still=True); print("RENDERED", fn)
sc.camera = close
if not PREVIEW:
    bpy.ops.file.pack_all()
    bpy.ops.wm.save_as_mainfile(filepath=D + r"\openmoon-primary-base.blend", compress=True)
    print("SAVED")
