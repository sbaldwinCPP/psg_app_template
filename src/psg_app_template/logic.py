# %%
import os

import PySimpleGUI as sg

# custom package
try:
    # if running from this file
    import functions as fun
    import front_panel as fp
except ModuleNotFoundError:
    # if this script has been imported elsewhere
    from . import functions as fun
    from . import front_panel as fp


# %% run
def run():
    icon_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "icon.ico"
    )
    window = fp.make_window(icon=icon_path)
    while True:
        event, values = window.read()  # type: ignore

        # exit methods
        if event in ("Exit", sg.WIN_CLOSED):
            print("[LOG] Exit")
            break

        # basic logging
        if event not in (sg.TIMEOUT_EVENT):
            msg = f"Event: {event}, Value: {values.get(event, 'N/A')}"
            if values["logging"]:
                sg.Print(msg)
            else:
                print(msg)

        # info
        if event == "version":
            fun.version_info(window, fp.APP_VERSION)
        if event == "help":
            fun.help_info(window)
        if event == "update":
            fun.app_update(window)

        # file selection
        if event == "input_file":
            file_name, file_extension = os.path.basename(values[event]).split(".")
            window["indicator_1"].update(file_name)
            window["indicator_2"].update(file_extension)

        # float inputs
        if event in fp.FLOATS:
            fun.enforce_input_type(event, values, window, float)

        # int inputs
        if event in fp.INTS:
            fun.enforce_input_type(event, values, window, int)

        if event == "Test":
            sg.popup(icon_path)

    window.close()


# %%

if __name__ == "__main__":
    run()
