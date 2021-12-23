from manim import *
from ..utils import Slide
from os import path


class IntroLogo(Slide):
    def construct(self):
        curr_dir = path.dirname(__file__)

        logo_border = SVGMobject(f"{curr_dir}/minimal_logo_border.svg")
        logo_border.scale(2)
        logo_border.set_stroke(width=10)
        logo_text = SVGMobject(f"{curr_dir}/minimal_logo_text.svg")
        logo_text.scale(2)

        self.pause()

        self.play(
            AnimationGroup(
                DrawBorderThenFill(logo_border, run_time=4),
                DrawBorderThenFill(logo_text, run_time=2.5, lag_ratio=0.1),
                lag_ratio=0.2,
            )
        )

        self.pause()

        self.play(
            Uncreate(logo_border, run_time=2), Uncreate(logo_text, run_time=2)
        )
