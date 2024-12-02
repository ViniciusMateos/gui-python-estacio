import tkinter as tk

janela = tk.Tk()

T = tk.Text(janela, height=2, width=30) # instância do componente “Text”.
T.insert(tk.END, "Este é um texto\ncom duas linhas\n")

tk.mainloop()
