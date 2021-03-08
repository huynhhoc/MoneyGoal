from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        self.button = Button()
        return self.button

    def on_press_button(self):
        print('You pressed the button!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()