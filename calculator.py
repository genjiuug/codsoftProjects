from tkinter import *

firstnumber=secnumber=operator=None

def get_digit(digits):
    currents = resultlabels['text']
    new1 = currents + str(digits)
    resultlabels.config(text=new1)

def clear():
    resultlabels.config(text='')

def get_operator(op):
    global firstnumber,operator

    firstnumber = int(resultlabels['text'])
    operator = op
    resultlabels.config(text='')

def get_result():
    global firstnumber,secnumber,operator

    second_number = int(resultlabels['text'])

    if operator == '+':
        resultlabels.config(text=str(firstnumber+second_number))
    elif operator == '-':
        resultlabels.config(text=str(firstnumber - secnumber))
    elif operator == '*':
        resultlabels.config(text=str(firstnumber * secnumber))
    else:
        if second_number == 0:
            resultlabels.config(text='Error')
        else:
            resultlabels.config(text=str(round(firstnumber / secnumber,2)))

root = Tk()
root.geometry('320x480')
root.title('Calculator')
root.resizable(0,0)
root.configure(background='grey')

resultlabels = Label(root,text='',bg='grey',fg='white')
resultlabels.grid(row=0,column=0,columnspan=5,pady=(60,25),sticky='w')
resultlabels.config(font=('verdana',30,'bold'))

btn7 = Button(root,text='7',fg='black',bg='white',width=6,height=3,command=lambda :get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14))

btn8 = Button(root,text='8',fg='black',bg='white',width=6,height=3,command=lambda :get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14))

btn9 = Button(root,text='9',bg='white',fg='black',width=6,height=3,command=lambda :get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))

btnaddition = Button(root,text='+',bg='white',fg='black',width=6,height=3,command=lambda :get_operator('+'))
btnaddition.grid(row=1,column=3)
btnaddition.config(font=('verdana',14))

btn4 = Button(root,text='4',fg='black',bg='white',width=6,height=3,command=lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))

btn5 = Button(root,text='5',fg='black',bg='white',width=6,height=3,command=lambda :get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))

btn6 = Button(root,text='6',fg='black',bg='white',width=6,height=3,command=lambda :get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14))

btn_subtract = Button(root,text='-',fg='black',bg='white',width=6,height=3,command=lambda :get_operator('-'))
btn_subtract.grid(row=2,column=3)
btn_subtract.config(font=('verdana',14))

btn1 = Button(root,text='1',fg='black',bg='white',width=6,height=3,command=lambda :get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14))

btn2 = Button(root,text='2',fg='black',bg='white',width=6,height=3,command=lambda :get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14))

btn3 = Button(root,text='3',fg='black',bg='white',width=6,height=3,command=lambda :get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14))

btnmultiply = Button(root,text='*',fg='black',bg='white',width=6,height=3,command=lambda :get_operator('*'))
btnmultiply.grid(row=3,column=3)
btnmultiply.config(font=('verdana',14))

btnclear = Button(root,text='C',fg='black',bg='white',width=6,height=3,command=lambda :clear())
btnclear.grid(row=4,column=0)
btnclear.config(font=('verdana',14))

btn0 = Button(root,text='0',fg='black',bg='white',width=6,height=3,command=lambda :get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14))

btnequ = Button(root,text='=',fg='black',bg='white',width=6,height=3,command=get_result)
btnequ.grid(row=4,column=2)
btnequ.config(font=('verdana',14))

btndivide = Button(root,text='/',fg='black',bg='white',width=6,height=3,command=lambda :get_operator('/'))
btndivide.grid(row=4,column=3)
btndivide.config(font=('verdana',14))

root.mainloop()