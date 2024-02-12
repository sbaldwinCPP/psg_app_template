# %%
# base lib
import os

# 3rd party lib
import PySimpleGUI as sg

# low level module, avoid cross imports

INPUT_SIZE = 10


# %% window
def make_window(name, version, **kwargs):
    icon_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data", "icon.ico"
    )
    window = sg.Window(
        name,
        create_layout(name, version),
        finalize=True,
        icon=icon_path,
        **kwargs,
    )
    set_led(window, "status_LED", "grey")
    window.set_min_size(window.size)
    return window


# %%
def update_theme(values, window, name, version):
    theme = values["theme"]
    sg.theme(theme)
    location = window.current_location()
    window.close()
    window = make_window(name, version, location=location)
    # update values to what they were before
    for k, v in values.items():
        # only try to update element types that can & should be updated
        if isinstance(window[k], (sg.Checkbox, sg.Input, sg.Combo)):
            window[k].update(v)

    window["Extras"].select()  # type: ignore
    window["theme"].SetFocus()

    return window


# %% elements
def led_indicator(key=None, radius=30):
    return sg.Graph(
        canvas_size=(radius, radius),
        graph_bottom_left=(-radius, -radius),
        graph_top_right=(radius, radius),
        pad=(0, 0),
        key=key,
    )


def set_led(window, key, color):
    graph = window[key]
    graph.erase()
    graph.draw_circle((0, 0), 12, fill_color=color, line_color=color)


def create_layout(name, version):
    header = [[sg.T(name, k="name", font=("Cascadia Code", 20))]]

    version = sg.T(
        f"v{version}",
        k="version",
        enable_events=True,
        tooltip="click here for version info",
        font=("Cascadia Code", 8),
    )

    status = sg.T(
        "status",
        # enable_events=True,
        tooltip="Status: None",
        font=("Cascadia Code", 8),
        k="status",
    )

    help = sg.T(
        "help",
        enable_events=True,
        tooltip="click here for instructions",
        font=("Calibri", 8, "underline"),
    )

    footer = [[led_indicator("status_LED"), status, sg.Push(), version, help]]

    file_browse = [
        sg.FileBrowse(
            button_text="...",
            target="input_file",
            file_types=[
                ("Specific Input File", "*SpecificInput.csv"),
                ("All Files", "*"),
            ],
        ),
        sg.In(
            "file path",
            k="input_file",
            enable_events=True,
            disabled=True,
            s=INPUT_SIZE,
        ),
        sg.T("File"),
    ]

    folder_browse = [
        sg.FolderBrowse(button_text="...", target="folder_path"),
        sg.In(
            "folder path",
            k="folder_path",
            enable_events=True,
            disabled=True,
            s=INPUT_SIZE,
        ),
        sg.T("Folder"),
    ]

    inputs = [
        folder_browse,
        file_browse,
    ]

    settings = [
        [sg.In("1.0", enable_events=True, k="float", s=INPUT_SIZE), sg.T("float")],
        [sg.In("-91", enable_events=True, k="int", s=INPUT_SIZE), sg.T("int")],
        [
            sg.Combo(
                [1, 2, 3, "a", "b", "c"],
                k="combo",
                s=INPUT_SIZE,
                enable_events=True,
            ),
            sg.T("combo"),
        ],
        [sg.Checkbox("checkbox", key="checkbox")],
        [sg.Button("GO", key="go", s=INPUT_SIZE, tooltip="this is a tooltip")],
    ]

    extras = [
        [
            sg.Combo(sg.theme_list(), sg.theme(), enable_events=True, k="theme"),
            sg.T("Theme"),
        ],
        [sg.Checkbox("Custom Theme", False, enable_events=True, k="enable_theme")],
        [sg.Checkbox("Logging", False, k="logging")],
        [sg.Button("Test"), sg.Button("Values"), sg.Button("Elements")],
    ]

    tabs = sg.TabGroup(
        [
            [
                sg.Tab("Inputs", inputs),
                sg.Tab("Settings", settings),
                sg.Tab("Extras", extras),
            ]
        ],
        k="tab_group",
    )
    layout = [header, [tabs], footer]
    return layout


# %% basic event logic for quick test/debug
if __name__ == "__main__":
    # sg.theme("hot dog stand")
    sg.theme("bright colors")
    window = make_window("FP Test", "99.99.99")
    while True:
        event, values = window.read()  # type: ignore

        # exit methods
        if event in ("Exit", sg.WIN_CLOSED):
            print("Exit")
            break
