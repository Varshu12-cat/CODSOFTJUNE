import tkinter as tk

def click(event):
    current = str(entry.get())
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# GUI Setup
root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")

entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill="both")
    for button_text in row:
        btn = tk.Button(row_frame, text=button_text, font="Arial 18", height=2, width=6)
        btn.pack(side=tk.LEFT, expand=True, fill="both")
        btn.bind("<Button-1>", click)

root.mainloop()

