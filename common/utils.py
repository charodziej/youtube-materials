from manim_presentation import Slide as SlideOrg


class Slide(SlideOrg):
    def __init__(self, *args, **kwargs):
        super().__init__(output_folder=".presentation", *args, **kwargs)

    def pause(self, *args, **kwargs):
        self.wait(0.1)
        super().pause(*args, **kwargs)

    def tear_down(self):
        self.wait(0.1)
