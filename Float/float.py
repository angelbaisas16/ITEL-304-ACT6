from kivy.app import App
from kivy.lang import Builder
 
root = Builder.load_string('''
FloatLayout:
    canvas.before:
        Color:
            rgba: 0, 128, 128, 0.3
        Rectangle:
            pos: self.pos
            size: self.size
    
    Button:
        text: 'Continue!!!'
        background_color: 1, 0, 0, 1
        size_hint: .2, .1
        pos_hint: {'center_x':.5, 'center_y': .3}
        
''')
 
class MainApp(App):
 
    def build(self):
        return root
 
if __name__ == '__main__':
    MainApp().run()