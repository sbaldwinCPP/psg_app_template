# %%

# 3rd party lib
import PySimpleGUI as sg

# custom lib (this app)
# high level module, import low level modules
import functions as fun
import front_panel as fp

# list of element keys with specific types to enforce
FLOATS = ["float", "float_2"]
INTS = ["int", "int_2"]


# %%
def run(window, name, version):
    while True:
        # get event and values
        read = window.read()
        if read is None:
            raise ValueError("window.read() returned None")
        else:
            event, values = read

        # exit methods
        if event in ("Exit", sg.WIN_CLOSED):
            print("Exit")
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

        # clickable texts in footer
        if event == "version":
            fun.version_info(window, version)
        if event == "help":
            fun.help_info(window)

        # float inputs
        if event in FLOATS:
            fun.enforce_input_type(event, values, window, float)
        # integer inputs
        if event in INTS:
            fun.enforce_input_type(event, values, window, int)
        # test button
        if event == "Test":
            window["status"].set_tooltip("updated tooltip!")
            fp.set_led(window, "status_LED", "lime")

    window.close()


# %%
if __name__ == "__main__":
    sg.theme("bright colors")
    name, version = "Logic Test", "-1"
    window = fp.make_window(name="Logic Test", version="-1")
    run(window, name, version)
