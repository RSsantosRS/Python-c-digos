import tkinter as tk

class Exemplos_Menu:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Menu")
        self.janela.geometry("300x200")
        self.janela.config(bg= "white")
        menubar = tk.Menu(self.janela)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label = "Novo")
        filemenu.add_command(label = "Abrir")
        filemenu.add_command(label ="Fechar")
        filemenu.add_separator()
        filemenu.add_command(label= "Sair", command = self.sair)
        menubar.add_cascade(label = "Arquivo", menu = filemenu)
        self.janela.config(menu=menubar)
        menu_ajuda = tk.Menu(menubar,tearoff=0)
        menu_ajuda.add_command(label = "Bem-vindo")
        #comando para abrir menus em botoes expecificos
        menu_ajuda.add_command(label= "Sobre", command = self.sobre)
        menubar.add_cascade(label = "Ajuda", menu= menu_ajuda)
        self.janela.mainloop()
    def sair(self):
        self.janela.destroy()

    def sobre(self):
        segunda_janela = tk.Toplevel(self.janela)
        segunda_janela.title('Sobre')
        segunda_janela.geometry('200x100')

    def janela_Extra(self):
        import pathlib
        import os
        path = pathlib.Path(__file__).parent.absolute()
        os.system(fr"{path}\\exemplo_ttk.py")

if __name__ == "__main__":
    Exemplos_Menu()