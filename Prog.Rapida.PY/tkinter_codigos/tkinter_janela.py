import tkinter as tk

janela = tk.Tk()

label = tk.Label(
    text="Brincando com Label",
    fg="#E6E6FA",
    bg="#FF1493"
)
botao = tk.Button(
    text="Botão",
    width=25,
    height=5,
)
entry = tk.Entry(fg="yellow",bg="blue",width=50)
#cria uma area para entrada de dados na tela, com as configurações de personalizadas.

label.pack()
botao.pack()
entry.pack()
janela.mainloop()