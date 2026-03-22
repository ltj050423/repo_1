from tkinter import *
import random

#tkinter window settings
window = Tk()

window.title("숫자 야구")
window.geometry("640x500")
window.resizable(False, False)

answernumber = []
print(answernumber)
strike_count = 0
ball_count = 0
out_count = 0

#defenition: function for making a new set of number to guess
#새로운 4개 숫자 리스트를 만든다
def newnumber():
    global answernumber
    answernumber = []
    for i in range(0,4):
        inputrandnumber = random.randint(0, 9)
        answernumber.append(inputrandnumber)
    strike_count = 0
    out_count = 0
    ball_count = 0

def numbercheck():
    #첫번째 숫자와 나머지 숫자를 비교.
    if numlist[0] == answernumber[0]:
        strike_count += 1
    elif numlist[0] == answernumber[1]:
        ball_count += 1
    elif numlist[0] == answernumber[2]:
        ball_count += 1
    elif numlist[0] == answernumber[3]:
        ball_count += 1
    else:
        out_count += 1
    #두번째 숫자와 나머지...
    if numlist[1] == answernumber[0]:
        ball_count += 1
    elif numlist[1] == answernumber[1]:
        strike_count += 1
    elif numlist[1] == answernumber[2]:
        ball_count += 1
    elif numlist[1] == answernumber[3]:
        ball_count += 1
    else:
        out_count += 1
    #세번째
    if numlist[2] == answernumber[0]:
        ball_count += 1
    elif numlist[2] == answernumber[1]:
        ball_count += 1
    elif numlist[2] == answernumber[2]:
        strike_count += 1
    elif numlist[2] == answernumber[3]:
        ball_count += 1
    else:
        out_count += 1
    #네번째
    if numlist[3] == answernumber[0]:
        ball_count += 1
    elif numlist[3] == answernumber[1]:
        ball_count += 1
    elif numlist[3] == answernumber[2]:
        ball_count += 1
    elif numlist[3] == answernumber[3]:
        strike_count += 1
    else:
        out_count += 1
 
numlist = list()

#defenition: functions for typing numbers 1~0까지 숫자를 하나씩 추가한다

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

#labels
#--------------------
try_1 = Label(window, text = "_ _ _ _")
try_2 = Label(window, text = "_ _ _ _")
try_3 = Label(window, text = "_ _ _ _")
try_4 = Label(window, text = "_ _ _ _")
try_5 = Label(window, text = "_ _ _ _")
try_6 = Label(window, text = "_ _ _ _")
try_7 = Label(window, text = "_ _ _ _")
try_8 = Label(window, text = "_ _ _ _")
try_9 = Label(window, text = "_ _ _ _")

try_1.place(x= 320, y= 50)


#debug mode below
#----------------------------------------------------------
def debug_show_answer():
    print(answernumber)

debug_show_answernumber = Button(window, text= "debug_showanswer", command= debug_show_answer)
debug_show_answernumber.place(x = 50, y = 450)

def debug_generate_answer():
    newnumber()
debug_generate_answer_button = Button(window, text="debug_generate new number", command= newnumber)
debug_generate_answer_button.place(x = 50, y = 400)
#------------------------------------------------------------

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