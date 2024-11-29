 # um kit de ferramentas GUI baseadas em uma biblioteca C++ chamada wxWidgets que foi lançada em 1998. 
# usa os componentes (widgets) reais na plataforma nativa sempre que possível.
# principal diferença entre o wxpython e outros kits de ferramentas, como PyQt ou Tkinter.

# As aplicações desenvolvidas em wxpython se assemelham a aplicações nativas do sistema operacional em que estão sendo executadas.
# wxpython também oferece suporte a componentes personalizados.

import wx
class Janela(wx.Frame):
   def __init__(self, parent, title):
      super(Janela, self).__init__(parent, title=title, size = (400,300))
      self.panel = ExemploPainel(self)
      self.text_ctrl = wx.TextCtrl(self.panel, pos=(5, 5))
      self.btn_test = wx.Button(self.panel, label='Pressione esse componente!', pos=(5, 55))


class ExemploPainel(wx.Panel):
   def __init__(self, parent):
      super(ExemploPainel, self).__init__(parent)


class ExemploApp(wx.App):
   def OnInit(self):
      self.frame = Janela(parent=None, title="Janela wxPython")
      self.frame.Show()
      return True


app = ExemploApp()
app.MainLoop()