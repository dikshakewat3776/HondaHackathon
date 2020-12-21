from kivy.app import App
from kivy.uix.button import Button


class MainApp(App):
    def build(self):
        button = Button(text='Say Something',
                        size_hint=(.2, .2),
                        pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=self.on_press_button)

        return button

    def on_press_button(self, instance):
        print('You pressed the button!')
        # TODO: assign a MOBID for user


if __name__ == '__main__':
    app = MainApp()
    app.run()