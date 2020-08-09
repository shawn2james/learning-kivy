from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongBall(Widget):
    # set initial velocity to 0
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # creating a list property containing x and y velocities
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(PongBall())

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()

        if self.ball.y < 0 or self.ball.top > self.height:
            self.ball.velocity_y *= -1
        elif self.ball.x < 0 or self.ball.right > self.width:
            self.ball.velocity_x *= -1

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1/60)
        return game


if __name__=="__main__":
    PongApp().run()
