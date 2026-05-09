import tkinter as tk

def animate(btn, color):
    original = btn.cget("bg")
    btn.config(bg=color)
    root.after(120, lambda: btn.config(bg=original))

def calculate(op, btn):
    animate(btn, "grey")

    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                result_label.config(text="Cannot divide by 0")
                return
            result = num1 / num2

        result_label.config(text="Calculating...")
        root.after(200, lambda: result_label.config(text=f"Result: {result}"))

    except:
        result_label.config(text="Invalid Input")

def make_btn(text, color, op, row, col):
    btn = tk.Button(btn_frame, text=text, bg=color, fg="white",
                    font=("Arial", 12, "bold"), width=5, bd=0)
    btn.config(command=lambda b=btn: calculate(op, b))
    btn.grid(row=row, column=col, padx=6, pady=6)

    btn.bind("<Enter>", lambda e: btn.config(bg="#333"))
    btn.bind("<Leave>", lambda e: btn.config(bg=color))

    return btn

root = tk.Tk()
root.title("🔥 Calculator")
root.geometry("340x450")
root.config(bg="#121212")

title = tk.Label(root, text="Calculator", font=("Arial", 18, "bold"),
                 fg="white", bg="#121212")
title.pack(pady=10)

entry1 = tk.Entry(root, font=("Arial", 14), justify="center")
entry1.pack(pady=10)

entry2 = tk.Entry(root, font=("Arial", 14), justify="center")
entry2.pack(pady=10)

btn_frame = tk.Frame(root, bg="#121212")
btn_frame.pack(pady=20)

make_btn("+", "#4CAF50", "+", 0, 0)
make_btn("-", "#f44336", "-", 0, 1)
make_btn("*", "#2196F3", "*", 1, 0)
make_btn("/", "#ff9800", "/", 1, 1)

result_label = tk.Label(root, text="Result", font=("Arial", 14, "bold"),
                        fg="white", bg="#121212")
result_label.pack(pady=20)

root.mainloop()