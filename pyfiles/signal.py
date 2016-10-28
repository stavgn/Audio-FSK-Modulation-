import numpy as np
import scipy.io.wavfile as wf
import matplotlib.pyplot as plt

class Signal:

    RESOLUTION = 1000

    def __init__(self, payload, amplitude=10000, frequencies=(700, 1400), phase=0, nperiods=1,generate_plot = False):
        self.signal = np.ndarray((1))
        self.payload = payload
        self.amplitude = amplitude
        self.nperiods = nperiods
        self.frequencies = frequencies
        self.phase = phase
        self.isModulated = False
        self.generate_plot = generate_plot

    def modulateSignal(self, func):
        func(self)
        self.isModulated = True

    def generateAudiofile(self, bitrate, filename=True):
        if self.isModulated:
            if filename:
                filename = self.payload.rawData
            wf.write("./audio/{0}.wav".format(filename), len(self.signal) / self.payload.bits_length * bitrate / self.nperiods, self.signal.astype(np.dtype('i2')))
        else:
            print "No Modulated Signal Found"

    def plotSignal(self,start= 0 ,end = True):
        if self.isModulated:
            if end:
                end = len(self.signal)
            plt.plot(self.signal[start:end])
            plt.show()