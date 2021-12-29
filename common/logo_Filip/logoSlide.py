import manim
from colour import Color

from common.utils import Slide
from os import path
from manim import FadeIn, FadeOut, ImageMobject, AnimationGroup, Text, Write, \
    Unwrite, UP, DOWN, Circle, Create, Uncreate


class IntroLogo(Slide):

    def construct(self):
        current_dir = path.dirname(__file__)

        red = Color("#ff3838")

        circle = Circle(
            radius=2.4,
            color=red
        )

        logo = ImageMobject(f"{current_dir}/avatar.png")
        logo.shift(UP * 0.5)

        nickname = Text(
            "Filip",
            font="Candara Light",
            font_size=60,
            color=Color("#ff3838")
        )
        nickname.shift(DOWN * 1.5)

        self.pause()

        self.play(
            AnimationGroup(
                Create(circle),
                AnimationGroup(
                    Write(nickname),
                    FadeIn(logo)
                ),
                lag_ratio=0.75
            )
        )

        self.pause()

        self.play(
            AnimationGroup(
                AnimationGroup(
                    Unwrite(nickname),
                    FadeOut(logo)
                ),
                Uncreate(circle),
                lag_ratio=0.75
            )
        )
