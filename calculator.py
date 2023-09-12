import tkinter as tk
from tkinter.font import Font

# Function to update the display with the clicked button's value
def button_click(value):
    current_text = display_var.get()
    # Concatenate the clicked value to the current text
    display_var.set(current_text + str(value))

# Function to clear the display
def clear():
    display_var.set("")

# Function to perform the calculation
def calculate():
    try:
        expression = display_var.get()
        result = str(eval(expression))
        display_var.set(result)
    except:
        display_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")  # Set the background color to black

# Create and set variables
display_var = tk.StringVar()
display_var.set("")

# Create the display
display_font = Font(family='Courier', size=24)
display = tk.Entry(root, textvariable=display_var, font=display_font, justify='right', bg='black', fg='white')
display.grid(row=0, column=0, columnspan=4)

# Define button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and arrange buttons
row_val = 1
col_val = 0
button_font = Font(family='Courier', size=18)

for label in button_labels:
    tk.Button(root, text=label, padx=20, pady=20, font=button_font, bg='white', fg='black',
              command=lambda label=label: button_click(label) if label != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create the clear button
tk.Button(root, text="Clear", padx=20, pady=20, font=button_font, bg='white', fg='black', command=clear).grid(row=row_val, column=col_val, columnspan=4)

# Run the GUI main loop
root.mainloop()
