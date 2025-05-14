import tkinter as tk

border_effects ={
    "flat": tk.FLAT,
    "afundado": tk.SUNKEN,
    "elevado": tk.RAISED,
    "borda": tk.GROOVE,
    "ondulado": tk.RIDGE,
}

Window = tk.Tk()
 
for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=Window, relief=relief,borderwidth=5)
    frame.pack(side=tk.TOP)#muda a direção das caixas
    label= tk.Label(master=frame, text=relief_name)
    label.pack()

Window.mainloop()