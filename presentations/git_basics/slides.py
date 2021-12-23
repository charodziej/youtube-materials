from manim import *
from common.utils import Slide

from common.logo_Adam.logoSlide import IntroLogo


class IntroScene(IntroLogo):
    pass


class TestSlide(Slide):
    def construct(self):
        circle = Circle(fill_opacity=1, fill_color=BLUE, stroke_color=BLUE)

        self.start_loop()
        self.play(Create(circle))

        self.play(Uncreate(circle))
        self.end_loop()


class GitIntro(Slide):
    def construct(self):
        circle = Circle(fill_opacity=1, fill_color=ORANGE, stroke_color=YELLOW)

        self.play(Create(circle))

        self.pause()

        self.play(Uncreate(circle))
