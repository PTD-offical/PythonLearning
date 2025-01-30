import tkinter as tk

CAlC = ""


# Functions
def AddToCalc(symbol):
    global CAlC
    CAlC += str(symbol)
    txtResult.delete("1.0", "end")
    txtResult.insert("1.0", CAlC)


def EvalCalc():
    global CAlC
    try:
        CAlC = str(eval(CAlC))
        txtResult.delete("1.0", "end")
        txtResult.insert("1.0", CAlC)
    except ZeroDivisionError:
        ClearCalc()
        txtResult.insert("1.0", "Cannot divide by 0")
    except:
        ClearCalc()
        txtResult.insert("1.0", "Invalid Input")


def ClearCalc():
    global CAlC
    CAlC = ""
    txtResult.delete("1.0", "end")


# GUI
root = tk.Tk()
root.title("Dark Theme Calculator")
root.geometry("300x350")
root.configure(bg="#2e2e2e")
root.resizable(False, False)  # Prevent window resizing
root.minsize(300, 350)  # Set the minimum size to the same as the current size

# Result Text Window
txtResult = tk.Text(root, height=2, width=16, font=("Arial", 24), bg="#1e1e1e", fg="white", bd=0)
txtResult.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Common button options
button_options = {
    "padx": 10,
    "pady": 10,
    "width": 5,
    "height": 2,
    "font": ("Arial", 14),
    "bd": 0,
    "relief": "flat",
}

# Dark theme button colors
buttons = [
    ("1", 1, 0, "#3b3b3b", "white"), ("2", 1, 1, "#3b3b3b", "white"), ("3", 1, 2, "#3b3b3b", "white"), ("+", 1, 3, "#ff9500", "black"),
    ("4", 2, 0, "#3b3b3b", "white"), ("5", 2, 1, "#3b3b3b", "white"), ("6", 2, 2, "#3b3b3b", "white"), ("-", 2, 3, "#ff9500", "black"),
    ("7", 3, 0, "#3b3b3b", "white"), ("8", 3, 1, "#3b3b3b", "white"), ("9", 3, 2, "#3b3b3b", "white"), ("*", 3, 3, "#ff9500", "black"),
    ("C", 4, 0, "#d9534f", "white"), ("0", 4, 1, "#3b3b3b", "white"), ("=", 4, 2, "#5cb85c", "white"), ("/", 4, 3, "#ff9500", "black"),
]

# Adding buttons to the grid
for text, row, col, bg_color, fg_color in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, command=EvalCalc, bg=bg_color, fg=fg_color, **button_options)
    elif text == "C":
        btn = tk.Button(root, text=text, command=ClearCalc, bg=bg_color, fg=fg_color, **button_options)
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: AddToCalc(t), bg=bg_color, fg=fg_color, **button_options)
    btn.grid(row=row, column=col, sticky="nsew")

# Main Loop for GUI
root.mainloop()
