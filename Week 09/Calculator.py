import tkinter as tk

def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("320x380")
root.resizable(False, False)
root.configure(bg="#95adea")

# Remove this if image not available
# root.iconphoto(False, tk.PhotoImage(file="im.png"))

# Entry Box
entry = tk.Entry(
    root,
    font=("Arial", 20),
    bd=10,
    relief=tk.RIDGE,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3),
]

for (text, row, col) in buttons:

    if text == "C":
        action = clear

    elif text == "=":
        action = calculate

    else:
        action = lambda x=text: press(x)

    tk.Button(
        root,
        text=text,
        width=5,
        height=2,
        font=("Arial", 14),
        command=action
    ).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()