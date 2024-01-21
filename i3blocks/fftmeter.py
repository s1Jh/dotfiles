import soundcard as sc
import matplotlib.pyplot as plt 
from scipy.fft import rfft, rfftfreq
import numpy as np 

# get a list of all speakers:
speakers = sc.all_speakers()
# get the current default speaker on your system:
default_speaker = sc.default_speaker()

# get a list of all microphones:v
mics = sc.all_microphones(include_loopback=True)
# get the current default microphone on your system:
default_mic = mics[0]

for i in range(len(mics)):
    try:
        print(f"{i}: {mics[i].name}")
    except Exception as e:
        print(e)

sr = 10000
chunk = 1000

with default_mic.recorder(samplerate=sr) as mic:
    while 1:
        print("Recording...")
        data = mic.record(numframes=chunk)
    
        yf = rfft(data)

        xf = rfftfreq(chunk*2 - 1, 1 / sr)
        plt.hist(np.abs(yf))
        plt.show()

