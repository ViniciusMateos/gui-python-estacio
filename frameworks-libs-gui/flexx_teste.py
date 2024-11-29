# kit de ferramentas para o desenvolvimento de interfaces gráficas com o usuário implementado em python que faz uso de tecnologia web para sua renderização.
# pode ser usado para criar tanto aplicações de desktop como para web e até mesmo exportar uma aplicação para um documento HTML independente.

from flexx import flx

class Exemplo(flx.Widget):
    def init(self):
        flx.Button(text='Olá')
        flx.Button(text='Mundo')

if __name__ == '__main__':
    app = flx.App(Exemplo)  # Cria a aplicação
    app.launch('browser')  # Abre no navegador
    flx.run()  # Inicia o loop principal