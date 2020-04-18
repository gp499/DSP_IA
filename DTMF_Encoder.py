import pyaudio
import numpy as np


def main():
    # Playback parameter
    silence_length = 0.1
    tone_length = 0.5
    sampling_freq = 8000
    volume = 0.5
    freq = [697.0, 770.0, 852.0, 941.0, 1209.0, 1336.0, 1477.0, 1633.0]
    tones = {
    '1': (freq[0],freq[4]),
    '2': (freq[0],freq[5]),
    '3': (freq[0],freq[6]),
    'A': (freq[0],freq[7]),
    '4': (freq[1],freq[4]),
    '5': (freq[1],freq[5]),
    '6': (freq[1],freq[6]),
    'B': (freq[1],freq[7]),
    '7': (freq[2],freq[4]),
    '8': (freq[2],freq[5]),
    '9': (freq[2],freq[6]),
    'C': (freq[2],freq[7]),
    'F': (freq[3],freq[4]),
    '0': (freq[3],freq[5]),
    'M': (freq[3],freq[6]),
    'D': (freq[3],freq[7])
    }
    t = np.linspace(0,tone_length,int(sampling_freq*tone_length)+1)
    s = np.zeros(int(sampling_freq*silence_length),dtype='float32')
    play = pyaudio.PyAudio()
    sound = play.open(rate=sampling_freq, channels=1, format=pyaudio.paFloat32, output=True)
    keys = input("Insert string:").upper()
    keys = [k for k in keys if k in tones]
    for k,key in enumerate(keys):
        tone = tones[key]
        wave = volume*np.sin(2.0*np.pi*t*tone[0]) + np.sin(2.0*np.pi*t*tone[1])
        wave = wave.astype('float32')
        sound.write(wave.tostring())
        if k+1 != len(keys):
            sound.write(s.tostring())
    sound.close()
    play.terminate()
    return


if __name__ == '__main__':
    main()