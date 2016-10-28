from pyfiles import payload, signal, modulate
import sys

payload1 = payload.Payload(sys.argv[1])
signal1 = signal.Signal(payload1)
signal1.modulateSignal(modulate.FSK)
signal1.generateAudiofile(10)
#signal1.plotSignal(0,2000)
