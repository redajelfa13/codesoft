import tkinter as tk

def on_button_click(symbol):
    current_text = entry.get()
    if symbol == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif symbol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, symbol)


root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the expression
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_val = 1
col_val = 0
for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, width=10, height=2, font=('Arial', 18), command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val, columnspan=2)
        col_val += 2
    else:
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val)
        col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
