# import everything from tkinter module, messagebox for displaying errors
from tkinter import *
import tkinter.messagebox



# ANS variable to enable the memory function
ANS = '0'

# name check
if __name__ == "__main__" :
    
    root = Tk()
    root.configure(background = "light grey") 
    root.title("Basic Calculator")  
    root.geometry("305x350+4+8")
    # disabling size variation
    root.resizable(False,False)
    # StringVar() is the variable class
    # StringVar is a class that provides helper functions for directly creating and accessing such variables in the Python interpreter
    equation = StringVar()
    # creating entry space for our input/output display, Entry(root, xxx) indicates what will be displayed in the box, in this case StringVar()
    expression_field = Entry(root, textvariable = equation, state = 'readonly')
    # customising expression box
    expression_field.grid(rowspan=1, columnspan=5, ipadx=80, ipady=20, padx=0, pady=10)
    # set method to display initial text
    equation.set('enter your expression')
    # creating the expression variable for later, displaying any button press
    expression = ""

def Enter0(button):
    button0['background'] = 'white'
def Leave0(button):
    button0['background'] = 'light grey'

def Enter1(button):
    button1['background'] = 'white'
def Leave1(button):
    button1['background'] = 'light grey'
    
def Enter2(button):
    button2['background'] = 'white'
def Leave2(button):
    button2['background'] = 'light grey'
    
def Enter3(button):
    button3['background'] = 'white'
def Leave3(button):
    button3['background'] = 'light grey'
    
def Enter4(button):
    button4['background'] = 'white'
def Leave4(button):
    button4['background'] = 'light grey'
    
def Enter5(button):
    button5['background'] = 'white'
def Leave5(button):
    button5['background'] = 'light grey'

def Enter6(button):
    button6['background'] = 'white'
def Leave6(button):
    button6['background'] = 'light grey'
    
def Enter7(button):
    button7['background'] = 'white'
def Leave7(button):
    button7['background'] = 'light grey'
    
def Enter8(button):
    button8['background'] = 'white'
def Leave8(button):
    button8['background'] = 'light grey'
    
def Enter9(button):
    button9['background'] = 'white'
def Leave9(button):
    button9['background'] = 'light grey'
    
def EnterAC(button):
    buttonAC['background'] = 'white'
def LeaveAC(button):
    buttonAC['background'] = 'light grey'
    
def EnterExponent(button):
    buttonExponent['background'] = 'white'
def LeaveExponent(button):
    buttonExponent['background'] = 'light grey'
    
def EnterDivide(button):
    buttonDivide['background'] = 'white'
def LeaveDivide(button):
    buttonDivide['background'] = 'light grey'
    
def EnterTimes(button):
    buttonTimes['background'] = 'white'
def LeaveTimes(button):
    buttonTimes['background'] = 'light grey'
    
def EnterMinus(button):
    buttonMinus['background'] = 'white'
def LeaveMinus(button):
    buttonMinus['background'] = 'light grey'
    
def EnterPlus(button):
    buttonPlus['background'] = 'white'
def LeavePlus(button):
    buttonPlus['background'] = 'light grey'
    
def EnterRB(button):
    buttonRB['background'] = 'white'
def LeaveRB(button):
    buttonRB['background'] = 'light grey'
    
def EnterLB(button):
    buttonLB['background'] = 'white'
def LeaveLB(button):
    buttonLB['background'] = 'light grey'
    
def EnterAnswer(button):
    buttonAnswer['background'] = 'white'
def LeaveAnswer(button):
    buttonAnswer['background'] = 'light grey'
    
def EnterDelete(button):
    buttonDelete['background'] = 'white'
def LeaveDelete(button):
    buttonDelete['background'] = 'light grey'

def EnterEqual(button):
    buttonEqual['background'] = 'gold'
def LeaveEqual(button):
    buttonEqual['background'] = 'orange'
    
def EnterAC(button):
    buttonAC['background'] = 'cyan'
def LeaveAC(button):
    buttonAC['background'] = 'red'
    
def EnterSqrt(button):
    buttonSqrt['background'] = 'white'
def LeaveSqrt(button):
    buttonSqrt['background'] = 'light grey'
    
def EnterPi(button):
    buttonPi['background'] = 'white'
def LeavePi(button):
    buttonPi['background'] = 'light grey'
    
def EnterDecimal(button):
    buttonDecimal['background'] = 'white'
def LeaveDecimal(button):
    buttonDecimal['background'] = 'light grey'
    


# special number
π = 3.1415

# creating operation function buttons

buttonDecimal = Button(root, text=' . ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('.'), height=1, width=7) 
buttonDecimal.grid(row=5, column=1)
buttonDecimal.bind('<Enter>',EnterDecimal)
buttonDecimal.bind('<Leave>',LeaveDecimal)

buttonPi = Button(root, text=' π ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('π'), height=1, width=7) 
buttonPi.grid(row=5, column=2)
buttonPi.bind('<Enter>',EnterPi)
buttonPi.bind('<Leave>',LeavePi)

buttonSqrt = Button(root, text=' √ ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('**0.5'), height=1, width=7) 
buttonSqrt.grid(row=3, column=4)
buttonSqrt.bind('<Enter>',EnterSqrt)
buttonSqrt.bind('<Leave>',LeaveSqrt)

buttonEqual = Button(root, text=' = ', fg='black', bg='orange', padx=0, pady=10, command=lambda: evaluate(equation), height=4, width=7) 
buttonEqual.grid(row=4, column=4, rowspan=2)
buttonEqual.bind('<Enter>',EnterEqual)
buttonEqual.bind('<Leave>',LeaveEqual)

buttonAC = Button(root, text=' AC ', fg='white', bg='red', padx=0, pady=10, command=lambda: press('AC'), height=1, width=7) 
buttonAC.grid(row=1, column=4)
buttonAC.bind('<Enter>',EnterAC)
buttonAC.bind('<Leave>',LeaveAC)

buttonDelete = Button(root, text=' DEL ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('DEL'), height=1, width=7) 
buttonDelete.grid(row=1, column=3)
buttonDelete.bind('<Enter>',EnterDelete)
buttonDelete.bind('<Leave>',LeaveDelete)

buttonAnswer = Button(root, text=' ANS ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('ANS'), height=1, width=7) 
buttonAnswer.grid(row=1, column=2)
buttonAnswer.bind('<Enter>',EnterAnswer)
buttonAnswer.bind('<Leave>',LeaveAnswer)

buttonRB = Button(root, text=' ) ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(')'), height=1, width=7) 
buttonRB.grid(row=1, column=1)
buttonRB.bind('<Enter>',EnterRB)
buttonRB.bind('<Leave>',LeaveRB)

buttonLB = Button(root, text=' ( ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('('), height=1, width=7) 
buttonLB.grid(row=1, column=0)
buttonLB.bind('<Enter>',EnterLB)
buttonLB.bind('<Leave>',LeaveLB)

buttonPlus = Button(root, text=' + ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('+'), height=1, width=7) 
buttonPlus.grid(row=5, column=3)
buttonPlus.bind('<Enter>',EnterPlus)
buttonPlus.bind('<Leave>',LeavePlus)

buttonMinus = Button(root, text=' - ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('-'), height=1, width=7) 
buttonMinus.grid(row=4, column=3)
buttonMinus.bind('<Enter>',EnterMinus)
buttonMinus.bind('<Leave>',LeaveMinus)

buttonTimes = Button(root, text=' × ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('*'), height=1, width=7) 
buttonTimes.grid(row=3, column=3)
buttonTimes.bind('<Enter>',EnterTimes)
buttonTimes.bind('<Leave>',LeaveTimes)

buttonExponent = Button(root, text=' ^ ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('**'), height=1, width=7) 
buttonExponent.grid(row=2, column=4)
buttonExponent.bind('<Enter>',EnterExponent)
buttonExponent.bind('<Leave>',LeaveExponent)

buttonDivide = Button(root, text=' ÷ ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('/'), height=1, width=7) 
buttonDivide.grid(row=2, column=3)
buttonDivide.bind('<Enter>',EnterDivide)
buttonDivide.bind('<Leave>',LeaveDivide)

button0 = Button(root, text=' 0 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('0'), height=1, width=7) 
button0.grid(row=5, column=0)
button0.bind('<Enter>',Enter0)
button0.bind('<Leave>',Leave0)
        
button1 = Button(root, text=' 1 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('1'), height=1, width=7) 
button1.grid(row=4, column=0)
button1.bind('<Enter>',Enter1)
button1.bind('<Leave>',Leave1)
            
button2 = Button(root, text=' 2 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('2'), height=1, width=7) 
button2.grid(row=4, column=1)
button2.bind('<Enter>',Enter2)
button2.bind('<Leave>',Leave2)
            
button3 = Button(root, text=' 3 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('3'), height=1, width=7) 
button3.grid(row=4, column=2)
button3.bind('<Enter>',Enter3)
button3.bind('<Leave>',Leave3)

button4 = Button(root, text=' 4 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('4'), height=1, width=7) 
button4.grid(row=3, column=0)
button4.bind('<Enter>',Enter4)
button4.bind('<Leave>',Leave4)

button5 = Button(root, text=' 5 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('5'), height=1, width=7) 
button5.grid(row=3, column=1)
button5.bind('<Enter>',Enter5)
button5.bind('<Leave>',Leave5)

button6 = Button(root, text=' 6 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('6'), height=1, width=7) 
button6.grid(row=3, column=2)
button6.bind('<Enter>',Enter6)
button6.bind('<Leave>',Leave6)

button7 = Button(root, text=' 7 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('7'), height=1, width=7) 
button7.grid(row=2, column=0)
button7.bind('<Enter>',Enter7)
button7.bind('<Leave>',Leave7)

button8 = Button(root, text=' 8 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('8'), height=1, width=7) 
button8.grid(row=2, column=1)
button8.bind('<Enter>',Enter8)
button8.bind('<Leave>',Leave8)

button9 = Button(root, text=' 9 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('9'), height=1, width=7) 
button9.grid(row=2, column=2)
button9.bind('<Enter>',Enter9)
button9.bind('<Leave>',Leave9)




        
    
# enclosing all special functions and characters into the press(button) function, this includes solutions to all possible inputs
def press(button): 
    # globalise expression variable
    global expression
    global answer
    # adding strings
    for u in range(len(expression)+1):
        if u == 40:
            tkinter.messagebox.showerror('Error','Length exceeding the limit')
            expression=expression[:len(expression)-len(expression)+40]
    # I took out the decimal as an indivial elif statement because multiple decimal points added will result in Math Error
    if button in 'π0123456789()':
        expression += button
    elif button == 'DEL':
        expression=expression[:len(expression)-1]
    elif button == 'AC':
        # clearing the expression, but does not affect the memory function ANS
        expression = ""
        equation.set("")
    elif button == 'ANS':
        button = answer
        expression += button
    elif button in '.-+*/':
        # if the ending character of the expression is decimal, then do nothing when '.' is clicked, otherwise add a decimal point
        if expression.endswith(button):
            return
        expression += button
    elif button == '**':
        # same for powers and roots
        if expression.endswith(button):
            return
        expression += button
    elif button == '**0.5':
        # the purpose of this is to avoid confusions when using consecutive operations
        if expression.endswith(button):
            return
        expression += button
        
    # update the expression by using set method 
    equation.set(expression)

def evaluate(equation): 
    # Try and except is used to handle the errors, such as zero division
    global expression
    if expression == "":
        return
    try:
        global answer
        # eval function evaluate the expression before str converts the result into strings
        result = str(eval(expression))
        answer = str(result)
        equation.set(result)
        expression = ""
    except: 
        equation.set(" Math error ") 
        expression = ""

#main
root.mainloop()
