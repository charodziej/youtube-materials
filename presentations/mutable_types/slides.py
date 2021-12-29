from manim import *

from common.logo_Filip.logoSlide import IntroLogo
from common.utils import Slide


class IntroScene(IntroLogo):
    pass


class MutableIntro(Slide):
    def construct(self):
        circle = Circle(fill_opacity=0, stroke_color=BLUE)
        square = Square(fill_opacity=0, stroke_color=WHITE)

        self.play(Create(circle))
        self.pause()

        self.play(Create(square))
        self.pause()
