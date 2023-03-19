#import kivyclra
#from tkinter import Button, Widget
from re import U
from tkinter import scrolledtext
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import StringProperty,BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy .uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.metrics import dp

class navi(Widget):
    pass

class WidgetsLayoutExample(GridLayout):
    count=0
    s=BooleanProperty(False)
    #sl=BooleanProperty(False)
    #my=StringProperty("50")
    text_input_str=StringProperty("hello !")
    my_text=StringProperty("hello !")
    def on_Button_Click(self):
            if self.s:
                self.count+=1
                self.my_text=str(self.count)
        
    
    def on_toggle_button_state(self,widget):
        print("toggle"+widget.state+str(self.s))
        if widget.state=="normal":
            widget.text="off"
            self.s=False
        else:
            widget.text="oN"
            self.s=True
    def on_switch_active(self,widget):
        print("switch "+  str(widget.active))
        #self.sl=widget.active

    def on_slider_value(self,widget):
        print("slider: "+str(int(widget.value)))
        #self.my=str(int(widget.value))


    def on_text_validate(self,widget):
        self.text_input_str=widget.text



class stackLayoutExample (StackLayout):
      
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(1,100) :
            size=dp(100)
            b=Button(text=str(i),size_hint=(None,None),size=(size,size))
            self.add_widget(b)

# class zx (GridLayout):
#     pass



class  asw(AnchorLayout):   # علشان نحرك الزر
    pass







class BoxLayoutExample(BoxLayout):   #علشان نعمل زرار
    pass
"""    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"
        b1=Button(text="A")
        b2=Button(text="B")
        b3=Button(text="c")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""



class MainWidget(Widget):     #علشان نعمل  شاشه
    pass



class TheLabApp(App):
    pass

TheLabApp().run()

