# import everything from tkinter module
from tkinter import *

# creating the expression variable for later, displaying any button press
expression = "" 

# name check
if __name__ == "__main__" :
    
    root = Tk()
    root.configure(background="light grey") 
    root.title("Basic Calculator")  
    root.geometry("284x350+4+8")
    # disabling size variation
    root.resizable(False,False)
    # StringVar() is the variable class
    # StringVar is a class that provides helper functions for directly creating and accessing such variables in the Python interpreter
    equation = StringVar()
    # creating entry space for our input/output display, Entry(root, xxx) indicates what will be displayed in the box, in this case StringVar()
    expression_field = Entry(root, textvariable = equation)
    # customising expression box
    expression_field.grid(rowspan=1, columnspan=5, ipadx=80, ipady=20, padx=0, pady=10)
    # set method to display initial text
    equation.set('enter your expression')

# assigning operations
operations = '+','-','×','÷','=','^','√','(',')'

# creating operation function buttons
buttonDecimal = Button(root, text=' . ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(Decimal), height=1, width=7) 
buttonDecimal.grid(row=5, column=1)

buttonPi = Button(root, text=' π ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(3.1415), height=1, width=7) 
buttonPi.grid(row=5, column=2)

buttonSqrt = Button(root, text=' √ ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(Root), height=1, width=7) 
buttonSqrt.grid(row=3, column=4)

buttonEqual = Button(root, text=' = ', fg='black', bg='orange', padx=0, pady=10, command=lambda: press(Divide), height=4, width=7) 
buttonEqual.grid(row=4, column=4, rowspan=2)

buttonAC = Button(root, text=' AC ', fg='red', bg='light grey', padx=0, pady=10, command=lambda: press(Ans), height=1, width=7) 
buttonAC.grid(row=1, column=4)

buttonDelete = Button(root, text=' DEL ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(Ans), height=1, width=7) 
buttonDelete.grid(row=1, column=3)

buttonAnswer = Button(root, text=' ANS ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(Ans), height=1, width=7) 
buttonAnswer.grid(row=1, column=2)

buttonRB = Button(root, text=' ) ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(RB), height=1, width=7) 
buttonRB.grid(row=1, column=1)

buttonLB = Button(root, text=' ( ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(LB), height=1, width=7) 
buttonLB.grid(row=1, column=0)

buttonPlus = Button(root, text=' + ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(Plus), height=1, width=7) 
buttonPlus.grid(row=5, column=3)

buttonMinus = Button(root, text=' - ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(Minus), height=1, width=7) 
buttonMinus.grid(row=4, column=3)

buttonTimes = Button(root, text=' × ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(Times), height=1, width=7) 
buttonTimes.grid(row=3, column=3)

buttonExponent = Button(root, text=' ^ ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(Exponent), height=1, width=7) 
buttonExponent.grid(row=2, column=4)

buttonDivide = Button(root, text=' ÷ ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(Divide), height=1, width=7) 
buttonDivide.grid(row=2, column=3)

button0 = Button(root, text=' 0 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(0), height=1, width=7) 
button0.grid(row=5, column=0)
        
button1 = Button(root, text=' 1 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(1), height=1, width=7) 
button1.grid(row=4, column=0)
        
button2 = Button(root, text=' 2 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(2), height=1, width=7) 
button2.grid(row=4, column=1)
        
button3 = Button(root, text=' 3 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(3), height=1, width=7) 
button3.grid(row=4, column=2)

button4 = Button(root, text=' 4 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(4), height=1, width=7) 
button4.grid(row=3, column=0)

button5 = Button(root, text=' 5 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(5), height=1, width=7) 
button5.grid(row=3, column=1)

button6 = Button(root, text=' 6 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(6), height=1, width=7) 
button6.grid(row=3, column=2)

button7 = Button(root, text=' 7 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(7), height=1, width=7) 
button7.grid(row=2, column=0)

button8 = Button(root, text=' 8 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(8), height=1, width=7) 
button8.grid(row=2, column=1)

button9 = Button(root, text=' 9 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(9), height=1, width=7) 
button9.grid(row=2, column=2)


def press(num): 
    # globalise expression variable 
    global expression 
    # adding strings
    expression = expression + str(num)
    # update the expression by using set method 
    equation.set(expression) 


#main
root.mainloop()

