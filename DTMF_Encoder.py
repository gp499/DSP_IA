import pyaudio
import numpy as np
from scipy.io import wavfile


class DtmfEncoder:
    def __init__(self):
        self.silence_length = 0.1
        self.tone_length = 0.5
        self.sampling_freq = 8000
        self.volume = 0.5
        freq = [697.0, 770.0, 852.0, 941.0, 1209.0, 1336.0, 1477.0, 1633.0]
        self.tones = {
            '1': (freq[0], freq[4]),
            '2': (freq[0], freq[5]),
            '3': (freq[0], freq[6]),
            'A': (freq[0], freq[7]),
            '4': (freq[1], freq[4]),
            '5': (freq[1], freq[5]),
            '6': (freq[1], freq[6]),
            'B': (freq[1], freq[7]),
            '7': (freq[2], freq[4]),
            '8': (freq[2], freq[5]),
            '9': (freq[2], freq[6]),
            'C': (freq[2], freq[7]),
            'F': (freq[3], freq[4]),
            '0': (freq[3], freq[5]),
            'M': (freq[3], freq[6]),
            'D': (freq[3], freq[7])
        }
        self.t = np.linspace(0, self.tone_length, int(self.sampling_freq * self.tone_length) + 1)
        self.s = np.zeros(int(self.sampling_freq * self.silence_length), dtype='float32')
        self.play = pyaudio.PyAudio()
        self.sound = self.play.open(rate=self.sampling_freq, channels=1, format=pyaudio.paFloat32, output=True)

    def encoder(self,keys):
        keys = [k for k in keys if k in self.tones]
        waveop = np.zeros(int(self.sampling_freq * self.silence_length), dtype='float32')
        for k, key in enumerate(keys):
            tone = self.tones[key]
            wave = self.volume * np.sin(2.0 * np.pi * self.t * tone[0]) + np.sin(2.0 * np.pi * self.t * tone[1])
            wave = wave.astype('float32')
            waveop = np.append(waveop, wave)
            self.sound.write(wave.tostring())
            if k + 1 != len(keys):
                self.sound.write(self.s.tostring())
        self.sound.close()
        self.play.terminate()
        wavfile.write('op.wav', self.sampling_freq, waveop.astype('float32'))
        return

#
# def main():
#     # Playback parameter
#     silence_length = 0.1
#     tone_length = 0.5
#     sampling_freq = 8000
#     volume = 0.5
#     freq = [697.0, 770.0, 852.0, 941.0, 1209.0, 1336.0, 1477.0, 1633.0]
#     tones = {
#     '1': (freq[0],freq[4]),
#     '2': (freq[0],freq[5]),
#     '3': (freq[0],freq[6]),
#     'A': (freq[0],freq[7]),
#     '4': (freq[1],freq[4]),
#     '5': (freq[1],freq[5]),
#     '6': (freq[1],freq[6]),
#     'B': (freq[1],freq[7]),
#     '7': (freq[2],freq[4]),
#     '8': (freq[2],freq[5]),
#     '9': (freq[2],freq[6]),
#     'C': (freq[2],freq[7]),
#     'F': (freq[3],freq[4]),
#     '0': (freq[3],freq[5]),
#     'M': (freq[3],freq[6]),
#     'D': (freq[3],freq[7])
#     }
#     t = np.linspace(0,tone_length,int(sampling_freq*tone_length)+1)
#     s = np.zeros(int(sampling_freq*silence_length),dtype='float32')
#     play = pyaudio.PyAudio()
#     sound = play.open(rate=sampling_freq, channels=1, format=pyaudio.paFloat32, output=True)
#     keys = input("Insert string:").upper()
#     keys = [k for k in keys if k in tones]
#     waveop = np.zeros(int(sampling_freq*silence_length),dtype='float32')
#     for k,key in enumerate(keys):
#         tone = tones[key]
#         wave = volume*np.sin(2.0*np.pi*t*tone[0]) + np.sin(2.0*np.pi*t*tone[1])
#         wave = wave.astype('float32')
#         waveop = np.append(waveop,wave)
#         sound.write(wave.tostring())
#         if k+1 != len(keys):
#             sound.write(s.tostring())
#     sound.close()
#     play.terminate()
#     wavfile.write('op.wav', sampling_freq, waveop.astype('float32'))
#     return


if __name__ == '__main__':
    dtmf = DtmfEncoder()
    keys = input("Insert string:").upper()
    dtmf.encoder(keys)
