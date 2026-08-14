from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class CalculatorApp(App):
    def build(self):
        Window.size = (400, 600)
        self.expression = ""
        
        # Main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # Display
        self.display = TextInput(
            text='0',
            font_size=40,
            readonly=True,
            halign='right',
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.display)
        
        # Buttons layout
        buttons_layout = BoxLayout(orientation='vertical', spacing=5)
        
        # Button rows
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        
        for row in buttons:
            row_layout = BoxLayout(spacing=5)
            for label in row:
                btn = Button(
                    text=label,
                    font_size=30,
                    size_hint=(1, 1)
                )
                btn.bind(on_press=self.on_button_press)
                row_layout.add_widget(btn)
            buttons_layout.add_widget(row_layout)
        
        # Clear button
        clear_btn = Button(
            text='C',
            font_size=30,
            size_hint=(1, 0.15),
            background_color=(1, 0, 0, 1)
        )
        clear_btn.bind(on_press=self.clear_display)
        buttons_layout.add_widget(clear_btn)
        
        layout.add_widget(buttons_layout)
        return layout
    
    def on_button_press(self, instance):
        button_text = instance.text
        
        if button_text == '=':
            try:
                # Evaluate the expression
                result = str(eval(self.expression))
                self.display.text = result
                self.expression = result
            except:
                self.display.text = 'Error'
                self.expression = ''
        else:
            self.expression += button_text
            self.display.text = self.expression
    
    def clear_display(self, instance):
        self.expression = ''
        self.display.text = '0'

if __name__ == '__main__':
    CalculatorApp().run()
