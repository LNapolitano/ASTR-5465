import numpy as np
import matplotlib.pyplot as plt

def dist_ratio(Av,dt):
	return(10**(Av*dt/5))
r=20

plt.plot(np.arange(0,r,0.1),dist_ratio(0.1,np.arange(0,r,0.1)))
plt.plot(np.arange(0,r,0.1),dist_ratio(0.5,np.arange(0,r,0.1)))
plt.plot(np.arange(0,r,0.1),dist_ratio(1.0,np.arange(0,r,0.1)))
plt.plot(np.arange(0,r,0.1),dist_ratio(1.5,np.arange(0,r,0.1)))
plt.yscale('log')
plt.xlabel('True Distance (pc)')
plt.ylabel('da/dt')
plt.show()

plt.plot(np.arange(0,r,0.1),1/dist_ratio(0.1,np.arange(0,r,0.1)))
plt.plot(np.arange(0,r,0.1),1/dist_ratio(0.5,np.arange(0,r,0.1)))
plt.plot(np.arange(0,r,0.1),1/dist_ratio(1.0,np.arange(0,r,0.1)))
plt.plot(np.arange(0,r,0.1),1/dist_ratio(1.5,np.arange(0,r,0.1)))
plt.xlabel('True Distance (pc)')
plt.ylabel('λa/λt')
plt.show()

plt.plot(np.arange(0,r,0.1),(1/dist_ratio(0.1,np.arange(0,r,0.1)))**3)
plt.plot(np.arange(0,r,0.1),(1/dist_ratio(0.5,np.arange(0,r,0.1)))**3)
plt.plot(np.arange(0,r,0.1),(1/dist_ratio(1.0,np.arange(0,r,0.1)))**3)
plt.plot(np.arange(0,r,0.1),(1/dist_ratio(1.5,np.arange(0,r,0.1)))**3)

plt.xlabel('True Distance (pc)')
plt.ylabel('ρa/ρt')
plt.show()