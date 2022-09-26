from kivy.config import Config
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window



Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (400, 750)


def get_ingridients(m):
    solt = str(10 * m / 1000)
    nitro = str(15 * m / 1000)
    mono = str(.5 * m / 1000)
    starts = str(5 * m / 1000)
    time = str(round(m / 500 * 2))
    return {'solt': solt,
            'nitro': nitro, 'mono': mono,
            'starts': starts,
            'time': time}


class Conteiner(GridLayout):
    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0

        ingridients = get_ingridients(mass)
        self.solt.text = ingridients.get('solt')
        self.nitro.text = ingridients.get('nitro')
        self.mono.text = ingridients.get('mono')
        self.starts.text = ingridients.get('starts')
        self.time.text = ingridients.get('time')


class MyApp(App):

    def build(self):

        return Conteiner()


if __name__ == '__main__':
    MyApp().run()
