# principais formas de o usuário entrar com dados no sistema.

import tkinter as tk
def mostrar_nomes():
   print("Nome: %s\nSobrenome: %s" % (e1.get(), e2.get()))

janela = tk.Tk()
janela.title("Aplicação GUI com o Widget Entry")
tk.Label(janela,text="Nome").grid(row=0)

tk.Label(janela,text="Sobrenome").grid(row=1)

e1 = tk.Entry(janela) # instâncias do componente entry
e2 = tk.Entry(janela) # instâncias do componente entry

e1.grid(row=0, column=1) # posicionados na janela
e2.grid(row=1, column=1) # posicionados na janela
 
tk.Button(janela, text='Sair',command=janela.quit).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Button(janela, text='Exibir Dados', command=mostrar_nomes).grid(row=3,column=1,sticky=tk.W,pady=4) # função “mostrar_nomes” é associada ao comportamento do botão.



tk.mainloop()