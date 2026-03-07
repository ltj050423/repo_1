from tkinter import *
import random

#tkinter window settings
window = Tk()

window.title("숫자 야구")
window.geometry("640x500")
window.resizable(False, False)

#defenition: function for making a new set of number to guess
def newnumber():
    answernumber = list()
    for i in range(0,4):
        inputrandnumber = random.randint(0, 9)
    answernumber.append(inputrandnumber)
'''
def numbercheck():
    for h in range(0, 4):
        '''


numlist = list()

#defenition: functions for typing numbers
def type_1():
    numlist.append(1)
def type_2():
    numlist.append(2)
def type_3():
    numlist.append(3)
def type_4():
    numlist.append(4)
def type_5():
    numlist.append(5)
def type_6():
    numlist.append(6)
def type_7():
    numlist.append(7)
def type_8():
    numlist.append(8)
def type_9():
    numlist.append(9)
def type_0():
    numlist.append(0)

b1 = Button(window, text= "1", command=type_1)
b2 = Button(window, text= "2", command=type_2)
b3 = Button(window, text= "3", command=type_3)
b4 = Button(window, text= "4", command=type_4)
b5 = Button(window, text= "5", command=type_5)
b6 = Button(window, text= "6", command=type_6)
b7 = Button(window, text= "7", command=type_7)
b8 = Button(window, text= "8", command=type_8)
b9 = Button(window, text= "9", command=type_9)
b0 = Button(window, text= "0", command=type_0)


def testprint():
    print(numlist)
testprintbutton = Button(window, text= "testprint", command=testprint)
testprintbutton.place(x = 200, y = 50)




b1.place(x = 300, y=300)
b2.place(x = 330, y=300)
b3.place(x = 360, y=300)
b4.place(x = 300, y=330)
b5.place(x = 330, y=330)
b6.place(x = 360, y=330)
b7.place(x = 300, y=360)
b8.place(x = 330, y=360)
b9.place(x = 360, y=360)
b0.place(x = 330, y=390)

window.mainloop()