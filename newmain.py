from kivy.app import App
# kivy.require("1.8.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from mydb import mydb
from kivy.uix.filechooser import FileChooserIconView
from kivy.garden.filebrowser import FileBrowser
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from counselling import counselling
class Painter(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud["line"].points += [touch.x, touch.y]


class MainScreen(Screen):

    def to_allotment(self):
        self.manager.current = 'allotment'
    pass

blockname = ""
class AnotherScreen(Screen):
    def getback(self):
        self.manager.current = 'main'
    def getblockname(self,c):

        global blockname
        blockname = c
        print  blockname,c
        self.manager.current = 'third'

    pass


class ScreenManagement(ScreenManager):
    pass

class ThirdScreen(Screen):
    def getback(self):
        self.manager.current = 'other'
    def up(self,v):
        print v
        self.manager.current='final'
        self.manager.get_screen('final').dump(v,blockname)
    pass

class AllotmentScreen(Screen):
    def getback(self):
        self.manager.current = 'main'
    def allot(self,a,b,c,d,e):
        list=[a,b,c,d,e]
        print list
        self.manager.current = 'allotedresult'
        self.manager.get_screen('allotedresult').settinglayout(list)
    pass

class allotedresult(Screen):
    def getback(self):
        self.manager.current = 'allotment'
    def settinglayout(self,list):
        result=counselling().getsdata(list)
        layout = self.ids['gd']
        layout.bind(minimum_height=layout.setter("height"))
        a=0;b=0;c=0;d=0;e=0
        a_length=len(result[0])
        b_length = len(result[1])
        c_length = len(result[2])
        d_length = len(result[3])
        e_length = len(result[4])
        print a_length, b_length, c_length, d_length, e_length

        m=max(a_length,b_length,c_length,d_length,e_length)
        for x in xrange(m):
            i=0
            if(x>=a_length):
                yu=Label(text = "", size=(150, 40), size_hint=(None, None), font_size="15dp", color=(0, 1, 1))
            else:
                yu = Label(text=str(result.__getitem__(i)[x][0])+str(" "+result.__getitem__(i)[x][1]+" ")+str(result.__getitem__(i)[x][2]), size=(150, 40), size_hint=(None, None), font_size="15dp", color=(0, 1, 1))
            layout.add_widget(yu)
            i+=1
            if (x >= b_length):
                yu = Label(text="", size=(150, 40), size_hint=(None, None), font_size="15dp", color=(0, 1, 1))
            else:
                yu = Label(text=str(result.__getitem__(i)[x][0]) + str(" " + result.__getitem__(i)[x][1] + " ") + str(result.__getitem__(i)[x][2]), size=(150, 40), size_hint=(None, None), font_size="15dp", color=(0, 1, 1))
            layout.add_widget(yu)
            i += 1
            if (x >= c_length):
                yu = Label(text="", size=(150, 40), size_hint=(None, None), font_size="15dp", color=(0, 1, 1))
            else:
                yu = Label(text=str(result.__getitem__(i)[x][0]) + str(" " + result.__getitem__(i)[x][1] + " ") + str(result.__getitem__(i)[x][2]), size=(150, 40), size_hint=(None, None), font_size="15dp", color=(0, 1, 1))
            layout.add_widget(yu)
            i += 1
            if (x >= d_length):
                yu = Label(text="", size=(150, 40), size_hint=(None, None), font_size="15dp", color=(0, 1, 1))
            else:
                yu = Label(text=str(result.__getitem__(i)[x][0])+str(" "+result.__getitem__(i)[x][1]+" ")+str(result.__getitem__(i)[x][2]), size=(150, 40), size_hint=(None, None), font_size="15dp", color=(0, 1, 1))
            layout.add_widget(yu)
            i+=1
            if (x >= e_length):
                yu = Label(text="", size=(150, 40), size_hint=(None, None), font_size="15dp", color=(0, 1, 1))
            else:
                yu = Label(text=str(result.__getitem__(i)[x][0])+str(" "+result.__getitem__(i)[x][1]+" ")+str(result.__getitem__(i)[x][2]), size=(150, 40), size_hint=(None, None), font_size="15dp", color=(0, 1, 1))
            layout.add_widget(yu)
            i+=1
        print list
    pass
layout=""
arr=[]
class FinalScreen(Screen):
    def getback(self):
        global arr
        global layout
        for x in arr:
            layout.remove_widget(x)
        self.manager.current = 'third'

    def dump(self,v,bname):
        global layout
        global arr
        arr=[]
        d=mydb()
        data=d.getsdata(v,bname)
        layout=self.ids['gd']


        layout.bind(minimum_height=layout.setter("height"))
        y=0
        for x in xrange(len(data)):

            arr.append(Label(text=str(data[x][0]),size=(100,40),size_hint=(None,None),font_size="20dp",color=(0,1,1)))
            layout.add_widget(arr[y])
            y+=1
            arr.append(Label(text=str(data[x][1]), size=(250, 40), size_hint=(None, None), font_size="20dp", color=(0, 1, 1)))
            layout.add_widget(arr[y])
            y+=1
            arr.append(Label(text=str(data[x][2]), size=(150, 40), size_hint=(None, None), font_size="20dp", color=(0, 1, 1)))
            layout.add_widget(arr[y])
            y+=1
            arr.append(Label(text=str(data[x][3]), size=(150, 40), size_hint=(None, None), font_size="20dp", color=(0, 1, 1)))
            layout.add_widget(arr[y])
            y+=1
            arr.append(Label(text=str(data[x][4]), size=(150, 40), size_hint=(None, None), font_size="20dp", color=(0, 1, 1)))
            layout.add_widget(arr[y])
            y+=1
        #self= ScrollView(size_hint=(1,None), size =(Window.width, Window.height))
        #self.add_widget(layout)
    #pass




presentation = Builder.load_file("main3.kv")

class MainApp(App):
    def build(self):
        return presentation


if __name__ == "__main__":
    MainApp().run()

