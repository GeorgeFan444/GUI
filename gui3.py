# import everything from tkinter module
from tkinter import *

# creating the expression variable for later, displaying any button press
expression = "" 
  
root = Tk()
root.configure(background="light grey") 
root.title("Basic Calculator")  
root.geometry("444x666+4+8")
# StringVar() is the variable class
# StringVar is a class that provides helper functions for directly creating and accessing such variables in the Python interpreter
equation = StringVar()
# creating entry space for our input/output display, Entry(root, xxx) indicates what will be displayed in the box, in this case StringVar()
expression_field = Entry(root, textvariable = equation)
expression_field.grid(columnspan=4, ipadx=70, ipady=10, padx=0, pady=10)
equation.set('enter your expression') 

buttonEqual = Button(root, text=' = ', fg='black', bg='orange', padx=0, pady=10, command=lambda: press(Equal), height=1, width=7) 
buttonEqual.grid(row=5, column=2, columnspan=1, ipadx=0)
        
buttonDecimal = Button(root, text=' . ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(Decimal), height=1, width=7) 
buttonDecimal.grid(row=5, column=1)
        
button0 = Button(root, text=' 0 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(0), height=1, width=7) 
button0.grid(row=5, column=0)
        
button1 = Button(root, text=' 1 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(1), height=1, width=7) 
button1.grid(row=4, column=0)
        
button2 = Button(root, text=' 2 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(2), height=1, width=7) 
button2.grid(row=4, column=1)
        
button3 = Button(root, text=' 3 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(3), height=1, width=7) 
button3.grid(row=4, column=2)

button4 = Button(root, text=' 4 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(3), height=1, width=7) 
button4.grid(row=3, column=0)

button5 = Button(root, text=' 5 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(3), height=1, width=7) 
button5.grid(row=3, column=1)

button6 = Button(root, text=' 6 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(3), height=1, width=7) 
button6.grid(row=3, column=2)

button7 = Button(root, text=' 7 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(3), height=1, width=7) 
button7.grid(row=2, column=0)

button8 = Button(root, text=' 8 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(3), height=1, width=7) 
button8.grid(row=2, column=1)

button9 = Button(root, text=' 9 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(3), height=1, width=7) 
button9.grid(row=2, column=2)


#main
root.mainloop()
