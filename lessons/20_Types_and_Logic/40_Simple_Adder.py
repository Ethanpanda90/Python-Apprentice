"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.
"""

from tkinter import messagebox, simpledialog, Tk

window = Tk()    
window.withdraw()

integer1 = simpledialog.askinteger("Simple Adder", "Please type in a number.")

integer2 = simpledialog.askinteger("Simple Adder", "Please type another number.")

sum = int(integer1) + int(integer2)

shownsum = messagebox.showinfo("The sum of those two numbers are...", sum)

window.mainloop()