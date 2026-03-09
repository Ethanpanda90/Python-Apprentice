"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().
"""

from tkinter import messagebox, simpledialog, Tk

window = Tk()    
window.withdraw()

a = simpledialog.askinteger("Infuriating Calculator", "Please type in a number.")

b = simpledialog.askinteger("Infuriating Calculator", "Please type another number.")

operation = simpledialog.askstring("Infuriating Calculator", "Please type in an operation.")

if operation = "+":
   calculated = a + b
   messagebox.showinfo("Infuriating Calculator", f"Calculation: {calculated}")
else:
   if operation = "-":
      calculated = a - b
      messagebox.showinfo("Infuriating Calculator", f"Calculation: {calculated}")
   else:
      if operation = "*":
         calculated = a * b
         messagebox.showinfo("Infuriating Calculator", f"Calculation: {calculated}")
      else:
         if operation = "/":
            calculated = a / b
            messagebox.showinfo("Infuriating Calculator", f"Calculation: {calculated}")



window.mainloop()