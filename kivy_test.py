import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.9.1')


class KivyTest(App):

    def build(self):
        self.title = 'Hello world'
        return Label(text='Hello world')


if __name__ == '__main__':
    KivyTest().run()

