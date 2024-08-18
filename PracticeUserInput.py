# Python program to create a simple GUI
# calculator using Tkinter
 
# import everything from tkinter module
from tkinter import *
import webbrowser 


def addMe():
        num1 = float(first_no.get())
        num2 = float(second_no.get())
        result = num1 + num2
        label3.config(text=result)

def subtrackMe():
        num1 = float(first_no.get())
        num2 = float(second_no.get())
        result = num1 - num2
        label3.config(text=result)

def multiplyMe():
        num1 = float(first_no.get())
        num2 = float(second_no.get())
        result = num1 * num2
        label3.config(text=result)

def divideMe():
        num1 = float(first_no.get())
        num2 = float(second_no.get())
        result = num1 / num2
        label3.config(text=result)
 
# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
 
    # set the background colour of GUI window
    gui.configure(background="purple")
 
    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("500x500")

    first_no = IntVar()
    second_no = IntVar()

    label1 = Label(gui,text="Enter first number").grid(row=0,column=1)
    entry1 = Entry(gui, text="first number", textvariable=second_no).grid(row=1, column=1)
    label2 = Label(gui,text="Enter second number").grid(row=2,column=1)
    entry2 = Entry(gui, text="second number",textvariable=first_no).grid(row=3, column=1)
    add = Button(gui,text="Add Numbers", command=addMe).grid(row=4,column=1)
    add = Button(gui,text="Subtract Numbers", command=subtrackMe).grid(row=5,column=1)
    add = Button(gui,text="Multiply Numbers", command=multiplyMe).grid(row=6,column=1)
    add = Button(gui,text="Divide Numbers", command=divideMe).grid(row=7,column=1)
    label3 = Label(gui)
    label3.grid(row=8, column=1)


    # start the GUI
    gui.mainloop()