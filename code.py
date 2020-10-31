import numpy as np
from scipy import signal
import sounddevice as sd
from scipy.io.wavfile import read
import time
import pysptk 

Fs = 8000
sd.default.samplerate = Fs

def normalize(vec):
    vec_new = []
    for i in range(len(vec)):
        vec_new.append(vec[i]/np.max(vec))
    return vec_new


def index(vok):
    for i in range(len(vokal_trans_str)):
        if  vokal_trans_str[i] == vok:
            return pysptk.sptk.lpc(np.array(normalize(vokal_vec[i])), order=10)
               
    
def endre_vokal(recording):
    ak = pysptk.sptk.lpc(np.array(normalize(recording)), order=10)
    ar0=ak[1:]
    ar1=np.append([1],ar0)
    ak_x = index(vokal())
    ar2=ak_x[1:]
    ar3=np.append([1],ar2)
    filtrert = signal.lfilter(ar1,[ak[0]], x=recording)
    changed = signal.lfilter([ak_x[0]], ar3, x=filtrert)
    print('Tada!')
    return changed

def opptak(duration):
    print('Spiller inn lyd..')
    rec = sd.rec(int(duration*Fs),samplerate=Fs, channels=2)
    time.sleep(duration/4)
    print('.')
    time.sleep(duration/4)
    print('.')
    time.sleep(duration/4)
    print('.')
    time.sleep(duration/4)
    print('Ferdig!')
    rec_ny = []
    for i in range(len(rec)):
        rec_ny.append(rec[i][0])
    return normalize(rec_ny)

def vokal():
    return input('Hvilken vokal vil du endre til?')

fs, a =read('a.wav')
fs, e =read('e.wav')
fs, i =read('i.wav')
fs, o =read('o.wav')
fs, u =read('u.wav')
fs, y =read('y.wav')
fs, ae =read('ae.wav')
fs, oe =read('oe.wav')
fs, aa =read('aa.wav')

vokal_trans_str = ['a', 'e', 'i', 'o', 'u', 'y', 'ae', 'oe', 'aa']
vokal_vec = [a, e, i, o, u, y, ae, oe, aa]

rec = opptak(1.2)

sd.play(normalize(rec))
time.sleep(2)
sd.play(normalize(endre_vokal(rec)))





