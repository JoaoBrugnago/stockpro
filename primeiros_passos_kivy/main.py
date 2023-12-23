from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (400, 600)

class GerenciadorTelas(ScreenManager):
  pass

class PrimeiraTela(Screen):
  pass

class SegundaTela(Screen):
  pass

class MyApp(App):
  def build(self):
    return GerenciadorTelas()
  
MyApp().run()

# https://www.youtube.com/watch?v=hh41Rduyaxw&ab_channel=Mundoinovador