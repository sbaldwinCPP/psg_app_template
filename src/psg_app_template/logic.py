# %%
import os

import PySimpleGUI as sg

# custom
from . import functions as fun
from . import front_panel as fp


# %% run
def run():
    window = fp.make_window()
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
            fun.version_info(window)
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

    window.close()


# %%

if __name__ == "__main__":
    run()
