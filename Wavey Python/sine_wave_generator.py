import numpy as np
import random as ran
import math
import matplotlib.pyplot as plt
def GeneratePureSineWave(frequency, Amplitude, Resolution, Length_In_Time):
    WaveY= np.array([])
    TimeX=np.array([])
    #Since we cant take fraction of a sample
    TotalSamples = round(Length_In_Time*Resolution)
    for Sample in range(TotalSamples):
        point = Amplitude*math.sin(2*np.pi*frequency*((Sample+1)/TotalSamples))
        WaveY = np.append(WaveY,point)
        TimeX = np.append(TimeX,Sample)
        
    SineWave = np.array([WaveY, TimeX])
    #print(WaveY)
    return SineWave

PureSine = GeneratePureSineWave(300, 1, 628, 1)
#print(PureSine[0])
plt.plot(PureSine[1], PureSine[0])
plt.show()


        
        
