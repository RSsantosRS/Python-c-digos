import tkinter as tk

def ao_focar(event):
    if entrada.get() == "Digite o seu nome aqui!":
        entrada.delete(0, "end")
        entrada.config(fg="black") #altera a cor do texto para preto 

def ao_desfocar(event):
    if not entrada.get():
        entrada.insert(0, "Digite o seu nome aqui!")
        entrada.config(Fg="gray")#altera a cor para cinza

janela = tk.Tk()
entrada = tk.Entry(width=40, bg="white", fg="gray")
entrada.pack()
entrada.insert(0, "Digite o seu nome aqui!")

entrada.bind("<FocusIn>", ao_focar)
#quando a caixa de entrada ganha o foco, chama a funcao ao_focar

entrada.bind("<FocusOut>", ao_desfocar)
#quando a caixa perde o foco, chama a funcao ao_desfocar
janela.mainloop()