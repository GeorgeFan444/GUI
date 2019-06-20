# import everything from tkinter module, astrix after import is a wildcard
from tkinter import *

# creating the expression variable for later, displaying any button press
expression = "" 

root = Tk()
root.configure(background="light grey") 
root.title("Basic Calculator")  
root.geometry("444x666+4+8")
# creating customised button widgets with various customisations inside parenthesis
# the gird method allows the button to be arranged in a row-column form, suitable for a calculator
buttonEqual = Button(root, text=' = ', fg='black', bg='orange', padx=0, pady=10, command=lambda: press(Equal), height=1, width=7) 
buttonEqual.grid(row=3, column=2, columnspan=2, ipadx=20)
        
buttonDecimal = Button(root, text=' . ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(Decimal), height=1, width=7) 
buttonDecimal.grid(row=3, column=1)
        
button0 = Button(root, text=' 0 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(0), height=1, width=7) 
button0.grid(row=3, column=0)
        
button1 = Button(root, text=' 1 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(1), height=1, width=7) 
button1.grid(row=2, column=0)
        
button2 = Button(root, text=' 2 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(2), height=1, width=7) 
button2.grid(row=2, column=1)
        
button3 = Button(root, text=' 3 ', fg='black', bg='light grey', padx=0, pady=10, command=lambda: press(3), height=1, width=7) 
button3.grid(row=2, column=2)

#main
root.mainloop()
