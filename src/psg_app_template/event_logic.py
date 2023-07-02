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
    sg.theme("BrightColors")
    window = fp.make_window()
    while True:
        event, values = window.read()  # type: ignore

        # exit methods
        if event in ("Exit", sg.WIN_CLOSED):
            print("[LOG] Exit")
            break

        # theme
        if values["enable_theme"] and values["theme"] != sg.theme():
            window = fun.change_theme(window, theme=values["theme"])

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
        # integer inputs
        if event in fp.INTS:
            fun.enforce_input_type(event, values, window, int)

        if event == "Test":
            fp.SetLED(window, "update_status", "lime")

    window.close()


# %%

if __name__ == "__main__":
    run()
