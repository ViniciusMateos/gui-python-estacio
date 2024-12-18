import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

def escolha_carreira():
   print("Gerencial: %d,\nTécnica : %d" % (var1.get(), var2.get())) # exibirá os valores dos objetos “var1” e “var2”, que estão relacionados aos “checkboxes

ttk.Label(janela, text="Escolha sua vocação:").grid(row=0, sticky=tk.W)

var1 = tk.IntVar() # Quando um “checkbox” for selecionado, o seu respectivo objetivo vai retornar valor 1; caso o componente não seja selecionado, o valor do objeto será 0.
ttk.Checkbutton(janela, text="Gerencial", variable=var1).grid(row=1, sticky=tk.W)

var2 = tk.IntVar() # Quando um “checkbox” for selecionado, o seu respectivo objetivo vai retornar valor 1; caso o componente não seja selecionado, o valor do objeto será 0.
ttk.Checkbutton(janela, text="Técnica", variable=var2).grid(row=2, sticky=tk.W)

ttk.Button(janela, text='Sair', command=janela.quit).grid(row=3, sticky=tk.W, pady=4)
ttk.Button(janela, text='Mostrar', command=escolha_carreira).grid(row=4, sticky=tk.W, pady=4)

janela.mainloop()