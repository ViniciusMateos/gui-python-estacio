# framework python de código aberto para o desenvolvimento de aplicações com interfaces de usuário e multitoque
# escrito em python e Cython, baseado em OpenGL ES 2, suporta vários dispositivos de entrada e possui uma extensa biblioteca de componentes (widgets
# mesmo código, a aplicação funciona para Windows, macOS, Linux, Android e iOS. 
# Todos os widgets Kivy são construídos com suporte multitoque.

from kivy.app import App
from kivy.uix.button import Button

class ExemploApp(App):
    def build(self):
        return Button(text='Olá, Mundo!')

if __name__ == '__main__':
    ExemploApp().run()

    
# Um ponto interessante pode ser observado no código, que é a utilização da programação orientada a objetos.

