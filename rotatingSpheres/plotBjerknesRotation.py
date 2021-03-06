from __future__ import division 
#import matplotlib
#matplotlib.use("Agg")
import numpy as np
import pylab as plt

from matplotlib import animation
import re

Writer = animation.writers['ffmpeg']
writer = Writer(fps = 15, metadata=dict(artist='Me'),bitrate=1800)
<<<<<<< HEAD
fn = 'Np40Nt10000dt0.01icrandO20.npy'
=======
fn = 'Np20Nt10000dt0.01icrandO0.npy'
>>>>>>> 42b30dc13fb715784e247f968d4da1caeed37429


a = 1.6*10**(-6)# particle radius, everything in SI units for now
lims = 20*a
interval = 20 #ms between frame
pos = np.load(fn)
div = 10 # divider for how many timesteps to render
alpha = .5 # transparency to use for particles

# Extract the Np,Nt,dt, 
Np = int(fn[fn.find('Np')+len('Np'):fn.rfind('Nt')])
Nt = int(fn[fn.find('Nt')+len('Nt'):fn.rfind('dt')])
dt = float(fn[fn.find('dt')+len('dt'):fn.rfind('ic')])

# Plot test results
lims /=a
pos /= a # Normalize positions by particle radius

fig = plt.figure() #XZ Plots (torque is in y)
ax = plt.axes(xlim=(-lims,lims),ylim=(-lims,lims))
s = ((ax.get_window_extent().width  / (2*lims) *20/fig.dpi) ** 2) #marker sizes scaled for plot (not scatter), trial and error
ax.set_title('XZ Plane '+ fn)

for n in range(Np):
	plt.plot(pos[n,:,0],pos[n,:,2],alpha=alpha)
  
plt.plot(np.linspace(-lims,lims),0*np.linspace(-lims,lims),'k-') # Trapping plane
plt.scatter(pos[:,0,0],pos[:,0,2],s=s) # Highlight starting points
plt.scatter(pos[:,-1,0],pos[:,-1,2],marker='s',s=s) # Highlight ending points
plt.show()

plt.figure() #XY Plots (trapping plane)
plt.xlim((-lims,lims))
plt.ylim((-lims,lims))
for n in range(0,Np):
	plt.plot(pos[n,:,0],pos[n,:,1],alpha=alpha)
plt.scatter(pos[:,0,0],pos[:,0,1],s=s) # Highlight starting points
plt.scatter(pos[:,-1,0],pos[:,-1,1],marker='s',s=s) # Highlight ending points
plt.show()


## ANIMATIONS: New method with circle
# Set up figure for animation (XZ)
fig = plt.figure()
ax = plt.axes(xlim=(-lims,lims),ylim=(-lims,lims))
ax.set_aspect(1)
title = ax.text(0,lims, "", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5}, ha="center")
plt.xlabel('x, particle radii')
plt.ylabel('z, particle radii')
ax.set_title('XZ Plane '+ fn)
def init():
	return []
      
# Animation function, will be called sequentially
def animate(i):
	#title.set_text(str(i*dt))
	patches=[]
	[p.remove() for p in reversed(ax.patches)] # Remove drawings from all previous time steps so that graphics don't overlap (basically blit=True but works on video output as well)
	for n in range(Np):
		x = pos[n,i,0]
		z = pos[n,i,2]

		patches.append(ax.add_patch(plt.Circle((x,z),radius=1,alpha=alpha)))

	return patches
# Call the animator
animxz = animation.FuncAnimation(fig, animate, init_func=init, frames=np.arange(0,Nt,div,dtype=int),interval= interval,blit=False)
plt.show()


# Set up figure for animation (XY)
fig = plt.figure()
ax = plt.axes(xlim=(-lims,lims),ylim=(-lims,lims))
ax.set_aspect(1)
ax.set_title('XY Plane '+ fn)
plt.xlabel('x, particle radii')
plt.ylabel('y, particle radii')
def init():
	return []
      
# Animation function, will be called sequentially
def animate(i):
	#title.set_text(str(i*dt)+' s')
	patches=[]
	[p.remove() for p in reversed(ax.patches)] # Remove drawings from all previous time steps so that graphics don't overlap (basically blit=True but works on video output as well)
	for n in range(Np):
		x = pos[n,i,0]
		y = pos[n,i,1]
		m = ax.add_patch(plt.Circle((x,y),radius=1,alpha=alpha))
		m.set_rasterized(True)
		patches.append(m)
	return patches
# Call the animator
animxy = animation.FuncAnimation(fig, animate, init_func=init, frames=np.arange(0,Nt,div,dtype=int),interval= interval,blit=False)
plt.show()
animxz.save(fn+'xz.mp4',writer=writer)
animxy.save(fn+'xy.mp4',writer=writer)
	
## Other useful analytics
#fig,axes = plt.subplots(3,1 , sharex=True)
#for n in range(Np):
	#for coord in[0,1,2]:
		#axes[coord].plot(np.arange(Nt+1)*dt,pos[n,:,coord],alpha=alpha)
#plt.show()







