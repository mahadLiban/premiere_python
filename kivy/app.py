import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

kivy.require('2.0.0')


class gameView(BoxLayout):
    def __init__(self):
        super(gameView, self).__init__()
        self.randomValue = random.randint(0, 1000)
    def check_number(self):
        if int(self.answer_input.text) == self.randomValue :
            self.result_label.text = "Congrat !"
            self.result_label.color  = "#00EF0B"
            self.randomValue = random.randint(0, 1000)
        elif int(self.answer_input.text) > self.randomValue :
            self.result_label.text = "Less than ! " + self.answer_input.text + " try again"
            self.result_label.color  = "#EF3E00"
        elif int(self.answer_input.text) < self.randomValue :
            self.result_label.text = "More than ! " + self.answer_input.text + " try again"
            self.result_label.color  = "#EF3E00"


class MahadApp(App):
    def build(self):
        return gameView()

mahadApp = MahadApp()
mahadApp.run()