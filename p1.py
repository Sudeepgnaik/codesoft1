import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except Exception as e:
        result.set("Error")

# Create the main window
root = tk.Tk()

root.title("Calculator")

# Create an Entry widget for input
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Create a StringVar to store the result
result = tk.StringVar()
result.set("")

# Create a Label to display the result
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=1, column=0, columnspan=4)

# Create buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]


# Function to handle button clicks
def button_click(event):
    if event.widget.cget("text") == "=":
        evaluate_expression()
    else:
        current_text = entry.get()
        new_text = current_text + event.widget.cget("text")
        entry.delete(0, tk.END)
        entry.insert(0, new_text)

# Create and place the buttons in the grid
row_val = 2
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20)
    button.grid(row=row_val, column=col_val)
    button.bind("<Button-1>", button_click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a clear button
clear_button = tk.Button(root, text="C", padx=20, pady=20, command=lambda: entry.delete(0, tk.END))

clear_button.grid(row=row_val, column=col_val)

# Run the main loop
root.mainloop()
