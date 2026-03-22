"""
Am I Big Yet?

Ask the user's age then use an if-elif-else statement to 
tell the user what age groups the user is in. The groups are:

0-2: Baby
3-5: Toddler
6-12: Child
13-19: Teen
20-64: Adult
65+: Senior

Except, if the user is the same age as you, print "You are pretty awesome!"

Here is how you ask the user's age in integer format.  The first argument is 
the title of the window, the second is the message to the user.

age = simpledialog.askinteger("Your Age", "How old are you?") 

Or, you could ask the user for a float with simpledialog.askfloat() 

age =  simpledialog.askfloat("Your Age", "How old are you?")

Here is how you show the user a message window. The first parameter is the title of the window, 
the second is the message to show the user.

messagebox.showinfo('What you are', "You are a baby.")
"""

from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups


age = simpledialog.askfloat("Your Age", "How old are you?")


# Use if statements to determine the age group
# and create a message

if age <= 2:
    messagebox.showinfo('What you are...', "You are skibidi, a skibidi baby.")
else:
    if age <= 5:
        messagebox.showinfo('What you are...', "Oh my brainrot, you're a toddler.")
    else:
        if age < 12:
            messagebox.showinfo('What you are...', "Finaly, your growing up you child. Took you long enough.")
        else:
            if age == 12:
                messagebox.showinfo('What you are...', "You're pretty awesome to be 12!")
            else:
                if age <= 19:
                    messagebox.showinfo('What you are...', "Wowie, a teenager.")
                else:
                    if age <= 64:
                        messagebox.showinfo('What you are...', "You are an adult, who now has responsibilities in life.")
                    else:
                        if age == 67:
                            messagebox.showinfo('What you are...', "SHUT UP ABOUT 67 I'M TIRED OF SEEING IT.")
                        else:
                            if age >= 65:
                                messagebox.showinfo('What you are...', "You are a senior, therefore, you should be respected.")


window.mainloop()  # Keeps the window open

 
# Try to write your program so you only need to use one messagebox.showinfo() function.