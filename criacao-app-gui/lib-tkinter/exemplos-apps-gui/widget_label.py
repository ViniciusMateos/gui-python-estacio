import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title(" Aplicação GUI com o Widget Label") 

ttk.Label(janela, text="Componente Label" ).grid(column=0, row=0) # feito o posicionamento do componente “label” na “janela” com o gerenciador de layout “grid”.
janela.mainloop()