import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("datos_diff.dat")
x = np.linspace(-1,1,30)
#plt.plot(x, data[-1,1:])
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,3,1)
ax.imshow(data)
ax2 = fig.add_subplot(1,3,2)
ax2.plot(x,data[-1,1:])
ax3 = fig.add_subplot(1,3,3)
ax2.plot(x,data[0,:])

plt.savefig("diffusivity_equation.png")
plt.close()
