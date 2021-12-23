import click
import inspect
from pathlib import Path
from manim.utils.module_ops import get_scene_classes_from_module, get_module


# helper function from https://stackoverflow.com/a/48727139 to allow rendering
# manim from scripts
def call_click_command(cmd, *args, **kwargs):
    """Wrapper to call a click command

    :param cmd: click cli command function to call
    :param args: arguments to pass to the function
    :param kwargs: keywrod arguments to pass to the function
    :return: None
    """

    # Get positional arguments from args
    arg_values = {c.name: a for a, c in zip(args, cmd.params)}
    args_needed = {c.name: c for c in cmd.params if c.name not in arg_values}

    # build and check opts list from kwargs
    opts = {a.name: a for a in cmd.params if isinstance(a, click.Option)}
    for name in kwargs:
        if name in opts:
            arg_values[name] = kwargs[name]
        else:
            if name in args_needed:
                arg_values[name] = kwargs[name]
                del args_needed[name]
            else:
                raise click.BadParameter(
                    "Unknown keyword argument '{}'".format(name)
                )

    # check positional arguments list
    for arg in (a for a in cmd.params if isinstance(a, click.Argument)):
        if arg.required and arg.name not in arg_values:
            raise click.BadParameter(
                "Missing required positional" "parameter '{}'".format(arg.name)
            )

    # build parameter lists
    opts_list = sum(
        [
            [o.opts[0], str(arg_values[n])]
            for n, o in opts.items()
            if n in arg_values.keys()
        ],
        [],
    )
    args_list = [str(v) for n, v in arg_values.items() if n not in opts]

    print(opts_list + args_list)
    # call the command
    try:
        cmd(opts_list + args_list)
    except BaseException as exc:
        if str(exc) != "0" and not isinstance(
            exc, (click.ClickException, SystemExit)
        ):
            raise


# slightly modified function from 3b1b's video repository
def get_slide_names(file_path):
    module = get_module(Path(file_path))
    scene_classes = get_scene_classes_from_module(module)

    scenes_with_line_nums = []
    for scene in scene_classes:
        if inspect.getmodule(scene).__name__ != module.__name__:
            continue
        lines, line_num = inspect.getsourcelines(scene)
        scenes_with_line_nums.append((line_num, scene))

    scenes_with_line_nums.sort(key=lambda s: s[0])
    return [scene[1].__name__ for scene in scenes_with_line_nums]
