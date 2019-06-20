# import everything from tkinter module, astrix after import is a wildcard
from tkinter import *

# following the workbook tutorial to construct a customised display window
root = Tk()
root.title("Basic Calculator")
root.configure(background = "light grey") 
root.geometry("444x666+4+8")

# main
root.mainloop()
