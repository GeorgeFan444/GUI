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

# define the mouse-over event for various buttons
# this produces an error because this function cannot define an action for buttons with different names, the only way to generalise event for all button type widget is to create a class
# alternatively I created a pair of Enter-Leave function for each of the buttons as demonstrated in the next interation
# due to my current programming method, it is highly inconvienient to implemete 'class' at this stage, so an inefficient way to achieve mouse-over colour change is used
def Enter(button):
    button0['background'] = 'white'
    button1['background'] = 'white'
    button2['background'] = 'white'
    button3['background'] = 'white'
    button4['background'] = 'white'
    button5['background'] = 'white'
    button6['background'] = 'white'
    button7['background'] = 'white'
    button8['background'] = 'white'
    button9['background'] = 'white'

def Leave(button):
    button0['background'] = 'light grey'
    button1['background'] = 'light grey'
    button2['background'] = 'light grey'
    button3['background'] = 'light grey'
    button4['background'] = 'light grey'
    button5['background'] = 'light grey'
    button6['background'] = 'light grey'
    button7['background'] = 'light grey'
    button8['background'] = 'light grey'
    button9['background'] = 'light grey'
    




# special number
π = 3.1415

# creating operation function buttons

buttonDecimal = Button(root, text=' . ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('.'), height=1, width=7) 
buttonDecimal.grid(row=5, column=1)
# example of binding the mouse-over feature to a button (incorrect way, since my custom Enter-Leave function does not apply to every widget of the same type)
button.bind('<Enter>',Enter)
button.bind('<Leave>',Leava)

buttonPi = Button(root, text=' π ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('π'), height=1, width=7) 
buttonPi.grid(row=5, column=2)

buttonSqrt = Button(root, text=' √ ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('**0.5'), height=1, width=7) 
buttonSqrt.grid(row=3, column=4)

buttonEqual = Button(root, text=' = ', fg='black', bg='orange', padx=0, pady=10, command=lambda: evaluate(equation), height=4, width=7) 
buttonEqual.grid(row=4, column=4, rowspan=2)

buttonAC = Button(root, text=' AC ', fg='white', bg='red', padx=0, pady=10, command=lambda: press('AC'), height=1, width=7) 
buttonAC.grid(row=1, column=4)

buttonDelete = Button(root, text=' DEL ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('DEL'), height=1, width=7) 
buttonDelete.grid(row=1, column=3)

buttonAnswer = Button(root, text=' ANS ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('ANS'), height=1, width=7) 
buttonAnswer.grid(row=1, column=2)

buttonRB = Button(root, text=' ) ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(')'), height=1, width=7) 
buttonRB.grid(row=1, column=1)

buttonLB = Button(root, text=' ( ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('('), height=1, width=7) 
buttonLB.grid(row=1, column=0)

buttonPlus = Button(root, text=' + ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('+'), height=1, width=7) 
buttonPlus.grid(row=5, column=3)

buttonMinus = Button(root, text=' - ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('-'), height=1, width=7) 
buttonMinus.grid(row=4, column=3)

buttonTimes = Button(root, text=' × ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('*'), height=1, width=7) 
buttonTimes.grid(row=3, column=3)

buttonExponent = Button(root, text=' ^ ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('**'), height=1, width=7) 
buttonExponent.grid(row=2, column=4)

buttonDivide = Button(root, text=' ÷ ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('/'), height=1, width=7) 
buttonDivide.grid(row=2, column=3)

button0 = Button(root, text=' 0 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('0'), height=1, width=7) 
button0.grid(row=5, column=0)

button1 = Button(root, text=' 1 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('1'), height=1, width=7) 
button1.grid(row=4, column=0)
       
button2 = Button(root, text=' 2 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('2'), height=1, width=7) 
button2.grid(row=4, column=1)
         
button3 = Button(root, text=' 3 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('3'), height=1, width=7) 
button3.grid(row=4, column=2)

button4 = Button(root, text=' 4 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('4'), height=1, width=7) 
button4.grid(row=3, column=0)

button5 = Button(root, text=' 5 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('5'), height=1, width=7) 
button5.grid(row=3, column=1)

button6 = Button(root, text=' 6 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('6'), height=1, width=7) 
button6.grid(row=3, column=2)

button7 = Button(root, text=' 7 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('7'), height=1, width=7) 
button7.grid(row=2, column=0)

button8 = Button(root, text=' 8 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('8'), height=1, width=7) 
button8.grid(row=2, column=1)

button9 = Button(root, text=' 9 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press('9'), height=1, width=7) 
button9.grid(row=2, column=2)

        
    
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
