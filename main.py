from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.solution = TextInput(multiline=False, readonly=True, halign='right', font_size=35)
        main_layout.add_widget(self.solution)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        
        grid = GridLayout(cols=4, spacing=5)
        for row in buttons:
            for label in row:
                button = Button(text=label, font_size=28)
                button.bind(on_press=self.on_button_press)
                grid.add_widget(button)
                
        main_layout.add_widget(grid)
        return main_layout

    def on_button_press(self, instance):
        text = instance.text
        if text == 'C':
            self.solution.text = ""
        elif text == '=':
            try:
                self.solution.text = str(eval(self.solution.text))
            except Exception:
                self.solution.text = "Error"
        else:
            self.solution.text += text

if __name__ == '__main__':
    CalculatorApp().run()
