# Create 10/04/2022
# Author @AStrukov


from kivy.app import App
from kivy.uix.widget import Widget


class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    # root = App()
    # root.name()
    # root.run()

    PongApp().run()

print('z')

