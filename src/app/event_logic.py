# %%
# base lib
import os

# 3rd party lib
import PySimpleGUI as sg

# custom lib (this app)
# high level module, import low level modules
import functions as fun
import front_panel as fp

# constants
FLOATS = ["float_1", "float_2"]
INTS = ["int_1", "int_2"]


# %%
def run(window, name, version):
    while True:
        event, values = window.read()  # type: ignore

        # exit methods
        if event in ("Exit", sg.WIN_CLOSED):
            print("[LOG] Exit")
            break

        # theme
        if values["enable_theme"] and values["theme"] != sg.theme():
            theme = values["theme"]
            window = fp.update_theme(theme, window, name, version)

        # basic logging
        if event not in (sg.TIMEOUT_EVENT):
            msg = f"Event: {event}, Value: {values.get(event, 'N/A')}"
            if values["logging"]:
                sg.Print(msg)
            else:
                print(msg)

        # info, usually in footer
        if event == "version":
            fun.version_info(window, version)
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
        if event in FLOATS:
            fun.enforce_input_type(event, values, window, float)
        # integer inputs
        if event in INTS:
            fun.enforce_input_type(event, values, window, int)

        if event == "Test":
            fp.set_led(window, "update_status", "lime")

    window.close()


# %%
if __name__ == "__main__":
    sg.theme("bright colors")
    name, version = "Logic Test", "-1"
    window = fp.make_window(name="Logic Test", version="-1")
    run(window, name, version)
