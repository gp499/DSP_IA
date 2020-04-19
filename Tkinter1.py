from tkinter import *
import pyaudio
from scipy.io import wavfile
from DTMF_Encoder import *
from DTMF_Decoder import *

window = Tk()
window.geometry('612x612')
window.resizable(0, 0)
window.title("DTMF Encoder Decoder")
# pack is used to show the object in the window
top_frame = Label(window).pack()
middle_frame = Label(window).pack()
bottom_frame = Label(window).pack()
number1 = ""


def but_click(number):
    global number1
    number1 += number
    input_text.set(number1)


def but_clear():
    global number1
    number1 = ""
    input_text.set("")


def but_encode():
    but_clear()
    dtmfE = DTMF_Encoder()
    keys = number1.upper()
    dtmfE.encoder(keys)


def but_decode():
    dtmfD = DTMF_Decoder()
    output = dtmfD.decode()
    input_text.set(output)


def but_play():
    framerate, frames = wavfile.read('C:/Users/91845/PycharmProjects/DSP_IA/op.wav', 'r')
    play = pyaudio.PyAudio()
    sound = play.open(rate=framerate, channels=1, format=pyaudio.paFloat32, output=True)
    sound.write(frames.tostring())
    sound.close()
    play.terminate()

input_text = StringVar()
input_frame = Frame(window, width=312, height=50)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('Arial', 18, 'bold'), textvariable=input_text, width=50)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(window, width=312, height=272.5, bg='grey')
btns_frame.pack()

bt1 = Button(btns_frame, text="1", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("1")).grid(column=1, row=1)
bt2 = Button(btns_frame, text="2", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("2")).grid(column=2, row=1)
bt3 = Button(btns_frame, text="3", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("3")).grid(column=3, row=1)
btA = Button(btns_frame, text="A", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("A")).grid(column=4, row=1)

bt4 = Button(btns_frame, text="4", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("4")).grid(column=1, row=2)
bt5 = Button(btns_frame, text="5", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("5")).grid(column=2, row=2)
bt6 = Button(btns_frame, text="6", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("6")).grid(column=3, row=2)
btB = Button(btns_frame, text="B", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("B")).grid(column=4, row=2)

bt7 = Button(btns_frame, text="7", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("7")).grid(column=1, row=3)
bt8 = Button(btns_frame, text="8", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("8")).grid(column=2, row=3)
bt9 = Button(btns_frame, text="9", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("9")).grid(column=3, row=3)
btC = Button(btns_frame, text="C", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("C")).grid(column=4, row=3)

bt_star = Button(btns_frame, text="*", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("*")).grid(column=1, row=4)
bt0 = Button(btns_frame, text="0", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("0")).grid(column=2, row=4)
bt_hash = Button(btns_frame, text="#", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("#")).grid(column=3, row=4)
btD = Button(btns_frame, text="D", width=10, height=3, bg="orange", fg="red", command=lambda: but_click("D")).grid(column=4, row=4)

bt_play = Button(btns_frame, text="PLAY", width=10, height=3, bg="orange", fg="red", command=lambda: but_play()).grid(column=1, row=5)
bt_encode = Button(btns_frame, text="ENCODE", width=10, height=3, bg="orange", fg="red", command=lambda: but_encode()).grid(column=2, row=5)
bt_decode = Button(btns_frame, text="DECODE", width=10, height=3, bg="orange", fg="red", command=lambda: but_decode()).grid(column=3, row=5)
bt_clear = Button(btns_frame, text="CLEAR", width=10, height=3, bg="orange", fg="red", command=lambda: but_clear()).grid(column=4, row=5)

window.mainloop()