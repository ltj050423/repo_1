from tkinter import *
window = Tk()

window.title("숫자 야구")
window.geometry("640x400")
window.resizable(False, False)

b1 = Button(window, text= "1")
b2 = Button(window, text= "2")
b3 = Button(window, text = "3")
b4 = Button(window, text= "4")


btnlist = [None] * 3

for i in range(0, 3):
    btnlist[i] = Button(window, text="버튼" + str(i + 1))


for btn in btnlist:
    btn.pack(side = RIGHT)

b1.place(x = 300, y=300)

window.mainloop()