import unittest.mock
from lib.manim_presentation.present import main as present_main


def run_presentation(slide_names):
    with unittest.mock.patch(
        "sys.argv",
        ["manim_presentation", "--folder", ".presentation"] + slide_names,
    ):
        present_main()
