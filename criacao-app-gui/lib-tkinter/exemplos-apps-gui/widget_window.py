# vai exibir uma janela redimensionável

import tkinter as tk

janela = tk.Tk()
janela.title(" Aplicação GUI")
janela.mainloop()

# Para fixar o tamanho da janela, é necessário determinar essa propriedade

import tkinter as tk

janela = tk.Tk()
janela.title(" Aplicação GUI NÃO Dimensionável") 
janela.resizable(False, False)
janela.mainloop()