import PySimpleGUI as sg


def enforce_input_type(event, values, window, type):
    try:
        type(values[event])
        window[event].update(values[event].strip())
    except ValueError:
        window[event].update(values[event][:-1])


def version_info(window, app_version):
    sg.popup_scrolled(
        f"App version: {app_version}\n" + sg.get_versions(),
        location=window.current_location(),
    )


def help_info(window):
    sg.popup("WIP, no instructions yet :(", location=window.current_location())


def app_update(window):
    sg.popup("WIP, no updater yet :(", location=window.current_location())
