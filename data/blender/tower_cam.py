import bpy, sys, math
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
PREVIEW = "preview" in args
BEAR = float(next((a.split("=")[1] for a in args if a.startswith("bear=")), "350"))
D = r"C:\Users\Beached\Desktop\OpenMoon base terrain"
SCR = r"C:\Users\Beached\AppData\Local\Temp\claude\430f9eef4f5515e2\2f56ca85-f6f8-4853-b580-4acbc22428cd\scratchpad"
bpy.ops.wm.open_mainfile(filepath=D + r"\openmoon-primary-base.blend")
sc = bpy.context.scene
names = ["B1", "M1", "B2", "M2", "B3", "B4", "M3"]
P = {n: bpy.data.objects[n].location.copy() for n in names}
human = bpy.data.objects["Human_1.8m"]
base = Vector((596.0, 478.3, 2735.9)); P["Base"] = base
ctr = sum(P.values(), Vector()) / len(P)

c = bpy.data.objects.get("Cam_towers")
if c is None:
    c = bpy.data.objects.new("Cam_towers", bpy.data.cameras.new("Cam_towers")); sc.collection.objects.link(c)
c.data.lens = 24; c.data.clip_start = 1; c.data.clip_end = 100000
sc.camera = c
r = math.radians(BEAR)
for dist in range(4000, 30001, 500):          # back off until every marker sits inside a 6% margin
    c.location = ctr + Vector((dist * math.sin(r), dist * math.cos(r), 0.6 * dist))
    c.rotation_euler = (ctr - c.location).to_track_quat('-Z', 'Y').to_euler()
    bpy.context.view_layer.update()
    fr = {n: world_to_camera_view(sc, c, p) for n, p in P.items()}
    if all(0.06 < f.x < 0.94 and 0.06 < f.y < 0.94 and f.z > 0 for f in fr.values()):
        break
print("CAM dist", dist, "loc", tuple(round(v) for v in c.location), "height above centre", round(c.location.z - ctr.z))
W, H = sc.render.resolution_x, sc.render.resolution_y
for n, f in fr.items():
    print("FRAME", n, round(f.x * W), round((1 - f.y) * H), "range_m", round(f.z))
dg = bpy.context.evaluated_depsgraph_get()
for n, p in P.items():
    t = p + Vector((0, 0, 5)); d = t - c.location
    ok, *_ = sc.ray_cast(dg, c.location, d.normalized(), distance=d.length - 3)
    print("LOS", n, "blocked" if ok else "clear")

sc.cycles.samples = 32 if PREVIEW else 256
sc.render.resolution_percentage = 50 if PREVIEW else 100
sc.render.filepath = (SCR if PREVIEW else D) + r"\render_towers.png"
bpy.ops.render.render(write_still=True); print("RENDERED")
if not PREVIEW:
    sc.camera = bpy.data.objects["Cam_close"]
    bpy.ops.file.pack_all()
    bpy.ops.wm.save_as_mainfile(filepath=D + r"\openmoon-primary-base.blend", compress=True); print("SAVED")
