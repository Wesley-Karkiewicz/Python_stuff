import numpy as np
import random as ran
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()
ax = plt.axes(xlim=(0, 200), ylim=(-1.25, 1.25))
DisplayWave, = ax.plot([],[])
def GeneratePureSineWave(frequency, Amplitude, Resolution, Length_In_Time):
    WaveY= np.array([])
    TimeX=np.array([])
    #Since we cant take fraction of a sample
    TotalSamples = round((1/Length_In_Time)*Resolution)
    
    for Sample in range(TotalSamples):
        point = Amplitude*math.sin(2*np.pi*frequency*((Sample+1)/TotalSamples))
        WaveY = np.append(WaveY,point)
        TimeX = np.append(TimeX,Sample)
        
    SineWave = np.array([WaveY, TimeX])
    #print(WaveY)
    return SineWave

def init():
    DisplayWave.set_data([],[])
    return DisplayWave,

def animate(i):
    ax = plt.axes(xlim=(0, (i*5)-1), ylim=(-1.25, 1.25))
    DisplayWave, = ax.plot([],[])
    Wave=GeneratePureSineWave(100, 1, (i*5), 1)
    DisplayWave.set_data(Wave[1], Wave[0])
    
    return DisplayWave,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1550, interval=10)
#anim.save('10Hz.mp4', fps=30, extra_args=['-vcodec', 'libx264'])                           
#print(PureSine[0])
#plt.plot(PureSine[1], PureSine[0])
plt.style.use('dark_background')
plt.show()


        
        
