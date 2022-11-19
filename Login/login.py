from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
 
class LoginScreen(GridLayout):
 
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.padding: 150

        self.add_widget(Label(text='Username',color='aqua'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username) 

        self.add_widget(Label(text='Password',color='aqua'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.add_widget(Button(text= 'Login',background_color='teal'))
        self.add_widget(Button(text= 'Register',background_color='teal'))
        self.Button = 5, .5
        
        
        

 
class LoginApp(App):
 
    def build(self):
        return LoginScreen()
 
if __name__ == '__main__':
    LoginApp().run()