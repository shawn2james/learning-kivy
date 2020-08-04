from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.app import App

import time

class MyClock(Label):
    def update(self, *args):
        self.font_size = '40sp'
        # time.asctime() gives date and time in nice format
        self.text = time.asctime()

class TimeApp(App):
    def build(self):
        my_clock = MyClock()
        # run my_clock.update every second
        Clock.schedule_interval(my_clock.update, 1)
        return my_clock

if __name__=="__main__":
    TimeApp().run()
