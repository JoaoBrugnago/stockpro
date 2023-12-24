from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (400, 600)

class Manager(ScreenManager):
  pass

class Menu(Screen):
  pass

class Compras(Screen):
  pass

class MyApp(App):
  def build(self):
    return Manager()
  
MyApp().run()