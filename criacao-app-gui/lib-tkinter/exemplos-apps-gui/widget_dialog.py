import tkinter as tk
from tkinter import messagebox as mb

def resposta():
   mb.showerror("Resposta", "Desculpe, nenhuma resposta disponível!") # instanciados componentes “messageDialog

def verificacao():
   if mb.askyesno('Verificar', 'Realmente quer sair?'): # instanciados componentes “messageDialog
      mb.showwarning('Yes', 'Ainda não foi implementado') # instanciados componentes “messageDialog
   else:
      mb.showinfo('No', 'A opção de Sair foi cancelada') # instanciados componentes “messageDialog

tk.Button(text='Sair', command=verificacao).pack(fill=tk.X)
tk.Button(text='Resposta', command=resposta).pack(fill=tk.X)

tk.mainloop()

# apesar de pouca implementação, é possível que o usuário tenha bastante interação com o sistema.

