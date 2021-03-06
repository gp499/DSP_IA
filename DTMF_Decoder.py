from scipy.io import wavfile
import math


class PygoertzelDtmf:
    def __init__(self, samplerate):
        self.samplerate = samplerate
        self.goertzel_freq = [1209.0,1336.0,1477.0,1633.0,697.0,770.0,852.0,941.0]
        self.s_prev = {}
        self.s_prev2 = {}
        self.totalpower = {}
        self.N = {}
        self.coeff = {}
        # create goertzel parameters for each frequency so that
        # all the frequencies are analyzed in parallel
        for k in self.goertzel_freq:
            self.s_prev[k] = 0.0
            self.s_prev2[k] = 0.0
            self.totalpower[k] = 0.0
            self.N[k] = 0.0
            normalizedfreq = k / self.samplerate
            self.coeff[k] = 2.0*math.cos(2.0 * math.pi * normalizedfreq)

    def __get_number(self, freqs):
        hi = [1209.0, 1336.0, 1477.0, 1633.0]
        lo = [697.0, 770.0, 852.0, 941.0]
        # get hi freq
        hifreq = 0.0
        hifreq_v = 0.0
        for f in hi:
            if freqs[f] > hifreq_v:
                hifreq_v = freqs[f]
                hifreq = f
        # get lo freq
        lofreq = 0.0
        lofreq_v = 0.0
        for f in lo:
            if freqs[f] > lofreq_v:
                lofreq_v = freqs[f]
                lofreq = f
        if lofreq == 697.0:
            if hifreq == 1209.0:
                return "1"
            elif hifreq == 1336.0:
                return "2"
            elif hifreq == 1477.0:
                return "3"
            elif hifreq == 1633.0:
                return "A"
        elif lofreq == 770.0:
            if hifreq == 1209.0:
                return "4"
            elif hifreq == 1336.0:
                return "5"
            elif hifreq == 1477.0:
                return "6"
            elif hifreq == 1633.0:
                return "B"
        elif lofreq == 852.0:
            if hifreq == 1209.0:
                return "7"
            elif hifreq==1336.0:
                return "8"
            elif hifreq == 1477.0:
                return "9"
            elif hifreq == 1633.0:
                return "C"
        elif lofreq == 941.0:
            if hifreq == 1209.0:
                return "*"
            elif hifreq == 1336.0:
                return "0"
            elif hifreq == 1477.0:
                return "#"
            elif hifreq == 1633.0:
                return "D"

    def run(self, sample):
        freqs = {}
        for freq in self.goertzel_freq:
            s = sample + (self.coeff[freq] * self.s_prev[freq]) - self.s_prev2[freq]
            self.s_prev2[freq] = self.s_prev[freq]
            self.s_prev[freq] = s
            self.N[freq] += 1
            power = (self.s_prev2[freq]*self.s_prev2[freq]) + (self.s_prev[freq]*self.s_prev[freq]) \
                    - (self.coeff[freq]*self.s_prev[freq]*self.s_prev2[freq])
            self.totalpower[freq] += sample*sample
            if self.totalpower[freq] == 0:
                self.totalpower[freq] = 1
            freqs[freq] = power / self.totalpower[freq] / self.N[freq]
        return self.__get_number(freqs)


class DTMF_Decoder:
    def __init__(self):
        self.framerate, frames = wavfile.read('C:/Users/91845/PycharmProjects/DSP_IA/op.wav', 'r')
        nchannels = 1
        # if stereo get left/right
        if nchannels == 2:
            self.left = [frames[i] for i in range(0, len(frames), 2)]
            self.right = [frames[i] for i in range(1, len(frames), 2)]
        else:
            self.left = frames
            self.right = self.left
        self.binsize = 400
        # Split the bin in 4 to average out errors due to noise
        self.binsize_split = 4
        self.prevvalue = ""
        self.prevcounter = 0

    def decode(self,):
        op = str()
        for i in range(0, len(self.left) - self.binsize, int(self.binsize / self.binsize_split)):
            goertzel = PygoertzelDtmf(self.framerate)
            for j in self.left[i:i + self.binsize]:
                value = goertzel.run(j)
            if value == self.prevvalue:
                self.prevcounter += 1
                if self.prevcounter == 10:
                    op += str(value)
            else:
                self.prevcounter = 0
                self.prevvalue = value
        return op
#
# if __name__ == '__main__':
#     dtmf = DTMF_Decoder()
#     dtmf.decode()

    # load wav file
    # framerate, frames = wavfile.read('C:/Users/91845/PycharmProjects/DSP_IA/op.wav', 'r')
    # nchannels = 1
    # sampwidth = 1
    # # if stereo get left/right
    # if nchannels == 2:
    #     left = [frames[i] for i in range(0,len(frames),2)]
    #     right = [frames[i] for i in range(1,len(frames),2)]
    # else:
    #     left = frames
    #     right = left
    # binsize = 400
    # # Split the bin in 4 to average out errors due to noise
    # binsize_split = 4
    # prevvalue = ""
    # prevcounter = 0
    # for i in range(0,len(left)-binsize, int(binsize/binsize_split)):
    #     goertzel = PygoertzelDtmf(framerate)
    #     for j in left[i:i+binsize]:
    #         value = goertzel.run(j)
    #     if value == prevvalue:
    #         prevcounter += 1
    #         if prevcounter == 10:
    #             print(value)
    #     else:
    #         prevcounter = 0
    #         prevvalue = value
