import tkinter as tk
from tkinter import ttk

# produzirá uma janela com duas linhas deslizantes

def mostrar_valores():
   print (w1.get(), w2.get())

janela = tk.Tk()

w1 = ttk.Scale(janela, from_=0, to=50) # instanciados componentes “sliders”.
w1.pack()
w2 = ttk.Scale(janela, from_=0, to=100, orient=tk.HORIZONTAL) # instanciados componentes “sliders”.
w2.pack()

# Além disso, são determinadas as propriedades “from”, “to” e “orient”, que são responsáveis, respectivamente, pelo espectro de escala componente e pela orientação do componente na tela.

ttk.Button(janela, text='Mostrar a Escala', command=mostrar_valores).pack()

janela.mainloop()