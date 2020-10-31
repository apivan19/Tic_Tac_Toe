# %%
from vpython import *

# %%
my_sphere = sphere(color=color.red, radius=0.9, make_trail=False, retain=50)
# %%
side = 3.0
thickness = 0.8
s1 = 2 * side - thickness
s2 = 2 * side - thickness
my_box = box(pos=vector(side, 0, 0), size=vector(thickness, s1, s2), color=color.green)
helix()