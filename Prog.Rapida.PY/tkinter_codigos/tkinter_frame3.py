import tkinter as tk

janela = tk.Tk()
frame1 = tk.Frame(master=janela, width=100, height=100,bg="red")
frame1.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
frame2 = tk.Frame(master=janela, width=50, height=50,bg="yellow")
frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
frame3 = tk.Frame(master=janela, width=25, height=25,bg="blue")
frame3.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

janela.mainloop()
#pode ser alterado o fill.tk.both para X e altera ate onde vai os frames da tela