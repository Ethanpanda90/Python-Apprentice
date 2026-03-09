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

a = simpledialog.askinteger("Simple Adder", "Please type in a number.")

b = simpledialog.askinteger("Simple Adder", "Please type another number.")

sum = a + b

messagebox.showinfo("Simple Adder", f"The sum of those two numbers are: {sum}")

window.mainloop()