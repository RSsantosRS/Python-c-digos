import tkinter as tk

class Exemplo_grid:
    def __init__(self):
        self.janela = tk.Tk()
        for i in range(3):
            for j in range(3):
                frame = tk.Frame(master=self.janela, relief=tk.RAISED, borderwidth=1)
                frame.grid(row=-i, column=j,padx=5,pady=5)
                label = tk.Label(master=frame, text=f"Linha {i}\n Coluna {j}")
                label.pack()
                self.janela.mainloop()

class Exemplo_Frame():
    def __init__(self):
        self.janela = tk.Tk()
        #comando para BLOQUEAR o redimensionamento da janela
        self.janela.resizable(False, False)
        for i in range(3):
            self.janela.columnconfigure(i,weight=1,minsize=75)
            self.janela.rowconfigure(i, weight=1, minsize=50)
            for j in range(3):
                frame = tk.Frame(master=self.janela,relief =tk.RAISED, borderwidth=1)
                frame.grid(row=i,column=j,padx=5,pady=5)
                label = tk.Label(master = frame, text=f"Linha {i}\n Coluna {j}")
                label.pack()
        self.janela.mainloop()


if __name__ == "__main__":
    Exemplo_Frame()
