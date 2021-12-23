import argparse

from build_scripts.build_presentation import build_presentation
from build_scripts.run_presentation import run_presentation
from build_scripts.helpers import get_slide_names


def main():
    parser = argparse.ArgumentParser(
        description='Tool to create and run manim presentations')
    parser.add_argument('presentation_folder', type=str,
                        help='folder of the presentation')

    args = parser.parse_args()

    file_path = f"./presentations/{args.presentation_folder}/slides.py"
    slide_names = get_slide_names(file_path)

    build_presentation(file_path)
    run_presentation(slide_names)


if __name__ == "__main__":
    main()
