import PySimpleGUI as sg

try:
    # if running from this file
    import front_panel as fp
except ModuleNotFoundError:
    # if this script has been imported elsewhere
    from . import front_panel as fp


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


def change_theme(window, values):
    location = window.current_location()
    freeze = window.AllKeysDict
    window.close()
    window = fp.make_window(location=location)
    for k in freeze:
        if k not in ["Browse", "tab_group"]:
            try:
                window[k].update(values[k])
            except KeyError:
                pass
    return window
