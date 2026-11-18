import bpy, bmesh
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
D = r"C:\Users\Beached\Desktop\OpenMoon base terrain"
bpy.ops.wm.open_mainfile(filepath=D + r"\openmoon-primary-base.blend")
sc = bpy.context.scene

for k in ("B1", "B2", "M1", "M2", "B4", "M3"):
    o = bpy.data.objects.get(k)
    if o:
        print("REMOVED", k, tuple(round(v, 1) for v in o.location)); bpy.data.objects.remove(o)
bpy.context.view_layer.update()
dg = bpy.context.evaluated_depsgraph_get()
def ground(x, y):
    ok, loc, *_ = sc.ray_cast(dg, Vector((x, y, 10000)), Vector((0, 0, -1))); return loc.z

towers = bpy.data.collections["Towers"]
exp = bpy.data.collections.get("Towers (expansion)") or bpy.data.collections.new("Towers (expansion)")
if exp.name not in towers.children: towers.children.link(exp)

orange = bpy.data.materials["Tower_marker"]
cyan = bpy.data.materials.get("Tower_marker_mine") or orange.copy()
cyan.name = "Tower_marker_mine"
b = cyan.node_tree.nodes["Principled BSDF"]
b.inputs["Base Color"].default_value = (0.0, 0.85, 1.0, 1)
b.inputs["Emission Color"].default_value = (0.0, 0.85, 1.0, 1)

def mast(name, x, y, mat, col):
    me = bpy.data.meshes.new(name + "_mast"); bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=16, radius1=0.5, radius2=0.5, depth=10.0)
    bmesh.ops.translate(bm, verts=bm.verts, vec=(0, 0, 5.0)); bm.to_mesh(me); bm.free()
    me.materials.append(mat)
    o = bpy.data.objects.new(name, me); col.objects.link(o)
    o.location = (x, y, ground(x, y)); return o

# each pair: base tower 10 m west, mine tower 10 m east of the given point (20 m apart)
pairs = [("B1", "M1", -463.9, -3918.2, 3272.4, towers), ("B2", "M2", -2742.9, -3738.5, 3212.9, towers),
         ("B4", "M3", 6318.0, -6976.4, 3463.3, exp)]
for bn, mn, x, y, zc, col in pairs:
    print("CHECK", bn + "+" + mn, round(ground(x, y), 2), "expected", zc)
    ob = mast(bn, x - 10, y, orange, col); om = mast(mn, x + 10, y, cyan, col)
    print("PLACED", bn, tuple(round(v, 1) for v in ob.location), mn, tuple(round(v, 1) for v in om.location))
b3 = bpy.data.objects["B3"]; print("B3 kept", tuple(round(v, 1) for v in b3.location))
print("TOWERS", sorted(o.name for o in towers.objects), "EXP", sorted(o.name for o in exp.objects))

ov = bpy.data.objects["Cam_overview"]; sc.camera = ov
for o in list(towers.objects) + list(exp.objects):
    p = world_to_camera_view(sc, ov, o.location)
    print("FRAME", o.name, round(p.x, 3), round(p.y, 3), "in" if 0 <= p.x <= 1 and 0 <= p.y <= 1 and p.z > 0 else "out")

sc.cycles.samples = 256; sc.render.resolution_percentage = 100
sc.render.filepath = D + r"\render_overview.png"
bpy.ops.render.render(write_still=True); print("RENDERED")
sc.camera = bpy.data.objects["Cam_close"]
bpy.ops.file.pack_all()
bpy.ops.wm.save_as_mainfile(filepath=D + r"\openmoon-primary-base.blend", compress=True); print("SAVED")
