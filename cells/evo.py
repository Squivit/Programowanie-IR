from random import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm

# colormap
trimap = ListedColormap(['white', 'red', 'blue'])

### randomowe dane pomagające w wizulizacji ###
# ilość kroków ewolucji
steps = 8
data = []
c = round(random()*256)
data0 = [int(b) for b in np.binary_repr(c)]
data.append(np.array(data0))
print(c)
print(data0)

for i in range(steps):
    data0 = np.roll(data0,1)
    b = round(random()*5)
    if b >=3:
        data0[0] = 2
    data.append(data0)


for a in data:
    print(a)

## KONIEC ##

bounds = [0, 1, 2, 3]
norm = BoundaryNorm(bounds, trimap.N)

fig, ax = plt.subplots(figsize=(16,9))
img = ax.matshow(data, cmap=trimap,vmin=np.min(data) - 0.5, vmax=np.max(data) + 0.5)
ax.axis(True)
# make a color bar
plt.colorbar(img, ticks=[0, 1, 2])
plt.show()