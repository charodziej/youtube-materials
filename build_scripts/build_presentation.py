from manim.cli.render.commands import render
from .helpers import call_click_command


def build_presentation(file_path):
    call_click_command(
        render,
        file_path,
        "-a",
        media_dir=".media",
        quality="h",
        frame_rate="30",
    )
