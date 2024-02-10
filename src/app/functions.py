import PySimpleGUI as sg

# low level module, avoid cross imports


def enforce_input_type(event, values, window, type):
    try:
        type(values[event])
        window[event].update(values[event].strip())
    except ValueError:
        print(f"Input must be compatible with type: {type}")
        window[event].update(values[event][:-1])


def version_info(window, app_version):
    sg.popup_scrolled(
        f"App version: {app_version}\n" + sg.get_versions(),
        location=window.current_location(),
        title="Version Info",
    )


def help_info(window):
    sg.popup("WIP, no instructions yet :(", location=window.current_location())
