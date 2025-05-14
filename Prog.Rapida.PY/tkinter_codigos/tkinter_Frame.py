import tkinter as tk
janela = tk.Tk()

botao = tk.Button()
frame_a = tk.Frame()
frame_b = tk.Frame()
label_a = tk.Label(master=frame_a,text="Frame A")
label_a.pack()

label_b = tk.Label(master=frame_a,text="Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

botao = tk.Button(
    text="Botão",# texto exibido
    fg="white",# muda cor do texto
    bg="black", #cor de fundo
    width=10, #largura
    height=2, #altura
)
botao.pack()
janela.mainloop()