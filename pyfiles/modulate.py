import numpy as np

def FSK(signal):
    cs = __genPiSeq(signal)
    signal.signal = np.ndarray((len(cs)))
    for i in xrange(len(signal.payload.bitArray)):
        if signal.payload.bitArray[i] == 0:
            signal.signal[i * signal.nperiods * signal.RESOLUTION: signal.nperiods * signal.RESOLUTION * (i + 1)] = signal.amplitude * np.cos(2 * np.pi * signal.frequencies[0] * cs[i* signal.nperiods * 1000: signal.nperiods * 1000 * (i + 1)] + signal.phase)
        else:
            signal.signal[i * signal.nperiods * signal.RESOLUTION: signal.nperiods * signal.RESOLUTION * (i + 1)] = signal.amplitude * np.cos(2 * np.pi * signal.frequencies[1] * cs[i* signal.nperiods * 1000: signal.nperiods * 1000 * (i + 1)] + signal.phase)

def __genPiSeq(signal):
    return np.linspace(0, np.pi * signal.nperiods * signal.payload.bits_length, signal.payload.bits_length * signal.RESOLUTION)