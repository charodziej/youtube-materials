from manim import *
from common.utils import Slide

from common.logo_Adam.logoSlide import IntroLogo

from os import path


class IntroScene(IntroLogo):
    pass


class GitIntro(Slide):
    def construct(self):
        curr_dir = path.dirname(__file__)
        git_logo = SVGMobject(f"{curr_dir}/git_logo.svg")
        git_text = Text("git")
        git = Group(git_logo, git_text)

        self.play(Write(git_text))
        self.play(
            AnimationGroup(
                git_text.animate.next_to(git_logo, DOWN),
                DrawBorderThenFill(git_logo),
                lag_ratio=0.5,
            )
        )

        self.pause()

        kontrola_wersji = Text("System kontroli wersji")
        kontrola_wersji.to_edge(edge=UP, buff=1)

        self.play(Write(kontrola_wersji))

        self.pause()

        subversion_logo = SVGMobject(f"{curr_dir}/subversion_logo.svg")
        subversion_text = Text("Subversion").next_to(
            subversion_logo, direction=DOWN
        )
        subversion = Group(subversion_logo, subversion_text)
        mercurial_logo = SVGMobject(f"{curr_dir}/mercurial_logo.svg")
        mercurial_text = Text("Mercurial").next_to(
            mercurial_logo, direction=DOWN
        )
        mercurial = Group(mercurial_logo, mercurial_text).shift(4 * RIGHT)

        self.play(
            AnimationGroup(
                git.animate.shift(4 * LEFT),
                Transform(
                    kontrola_wersji,
                    Text("Systemy kontroli wersji").to_edge(edge=UP, buff=1),
                ),
                DrawBorderThenFill(subversion_logo),
                Write(subversion_text),
                DrawBorderThenFill(mercurial_logo),
                Write(mercurial_text),
                lag_ratio=0.3,
            )
        )
        self.pause()

        git_chart = AnnularSector(
            0,
            2,
            0.73 * TAU,
            stroke_width=5,
            start_angle=0,
            color=RED,
            fill_opacity=0.5,
        ).shift(UL / 4)
        subversion_chart = AnnularSector(
            0,
            2,
            0.23 * TAU,
            stroke_width=5,
            start_angle=0.73 * TAU,
            color=BLUE,
            fill_opacity=0.5,
        ).shift(DOWN / 4)
        mercurial_chart = AnnularSector(
            0,
            2,
            0.02 * TAU,
            stroke_width=5,
            start_angle=0.96 * TAU,
            color=GREEN,
            fill_opacity=0.5,
        ).shift(RIGHT / 4)

        self.play(
            AnimationGroup(
                git.animate.scale(0.5).next_to(git_chart, direction=LEFT),
                subversion.animate.scale(0.5).next_to(
                    subversion_chart, direction=DOWN
                ),
                mercurial.animate.scale(0.5).next_to(
                    mercurial_chart, direction=RIGHT
                ),
                AnimationGroup(
                    DrawBorderThenFill(mercurial_chart),
                    DrawBorderThenFill(subversion_chart),
                    DrawBorderThenFill(git_chart),
                    lag_ratio=0.2,
                ),
                lag_ratio=0.2,
            )
        )

        self.pause()

        self.play(
            AnimationGroup(
                Unwrite(kontrola_wersji),
                AnimationGroup(
                    Uncreate(git_chart),
                    Uncreate(subversion_chart),
                    Uncreate(mercurial_chart),
                ),
                AnimationGroup(
                    Unwrite(git_text),
                    Unwrite(subversion_text),
                    Unwrite(mercurial_text),
                    FadeOut(git_logo),
                    FadeOut(subversion_logo),
                    FadeOut(mercurial_logo),
                ),
                lag_ratio=0.2,
            )
        )
