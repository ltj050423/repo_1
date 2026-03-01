from tkinter import *
window = Tk()

btnlist = [None] * 3

for i in range(0, 3):
    btnlist[i] = Button(window, text="버튼" + str(i + 1))

for btn in btnlist:
    btn.pack(side = RIGHT)


window.mainloop()