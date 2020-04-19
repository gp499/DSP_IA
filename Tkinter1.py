from tkinter import *
window= Tk()
window.geometry('612x612')
window.resizable(0,0)
window.title("Mobile Keypad")
#pack is used to show the object in the window
top_frame = Label(window).pack()
middle_frame = Label(window).pack()
bottom_frame = Label(window).pack()

# input_frame = Frame(window,width = 312,height = 50)
# input_frame.pack(side = TOP)
#
# input_field = Entry(input_frame, font=('Arial',18,'bold'))
# input_field.grid(row=0,column=0)
# input field.pack(ipady = 10)

btns_frame = Frame(window,width=312,height=272.5,bg='grey')
btns_frame.pack()

bt7 = Button(btns_frame, text="7", width =10,height=3,bg="orange", fg="red").grid(column=1,row=1)
bt8 = Button(btns_frame, text="8", width =10,height=3,bg="orange", fg="red").grid(column=2,row=1)
bt9 = Button(btns_frame, text="9", width =10,height=3,bg="orange", fg="red").grid(column=3,row=1)

bt4 = Button(btns_frame, text="4", width =10,height=3,bg="orange", fg="red").grid(column=1,row=2)
bt5 = Button(btns_frame, text="5", width =10,height=3,bg="orange", fg="red").grid(column=2,row=2)
bt6 = Button(btns_frame, text="6", width =10,height=3,bg="orange", fg="red").grid(column=3,row=2)

bt1 = Button(btns_frame, text="1", width =10,height=3,bg="orange", fg="red").grid(column=1,row=3)
bt2 = Button(btns_frame, text="2", width =10,height=3,bg="orange", fg="red").grid(column=2,row=3)
bt3 = Button(btns_frame, text="3", width =10,height=3,bg="orange", fg="red").grid(column=3,row=3)

bt_star = Button(btns_frame, text="*", width =10,height=3,bg="orange", fg="red").grid(column=1,row=4)
bt0 = Button(btns_frame, text="0", width =10,height=3,bg="orange", fg="red").grid(column=2,row=4)
bt_hash = Button(btns_frame, text="#", width =10,height=3,bg="orange", fg="red").grid(column=3,row=4    )



window.mainloop()