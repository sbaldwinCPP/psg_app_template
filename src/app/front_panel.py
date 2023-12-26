import os

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
    set_led(window, "update_status", "grey")
    window.set_min_size(window.size)
    return window


# %%
def update_theme(theme, window, name, version):
    sg.theme(theme)
    location = window.current_location()
    window.close()
    window = make_window(name, version, location=location)
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

    update = sg.T(
        "update",
        enable_events=True,
        tooltip="click here to check for updates",
        font=("Cascadia Code", 8),
        k="update",
    )

    help = sg.T(
        "help",
        enable_events=True,
        tooltip="click here for instructions",
        font=("Calibri", 8, "underline"),
    )

    footer = [[version, led_indicator("update_status"), update, sg.Push(), help]]

    file_browse = [
        sg.In(k="input_file", enable_events=True, visible=False),
        sg.FileBrowse(
            target="input_file",
            file_types=[
                ("Specific Input File", "*SpecificInput.xlsx"),
                ("All Files", "*"),
            ],
        ),
        sg.T("Select input file"),
    ]
    inputs = [
        file_browse,
        [sg.In("Indicator 1", disabled=True, s=INPUT_SIZE, k="indicator_1")],
        [sg.In("Indicator 2", disabled=True, s=INPUT_SIZE, k="indicator_2")],
        [sg.Checkbox("...SpecificInput.xlsx", disabled=True, k="input_bool")],
        [sg.Checkbox("...Save_file.pkl", disabled=True, k="save_bool")],
    ]

    fig_settings = [
        [sg.In("1.0", enable_events=True, k="float_1", s=INPUT_SIZE), sg.T("float 1")],
        [sg.In("0.2", enable_events=True, k="float_2", s=INPUT_SIZE), sg.T("float 2")],
        [sg.In("-91", enable_events=True, k="int_1", s=INPUT_SIZE), sg.T("int 1")],
        [sg.In("57", enable_events=True, k="int_2", s=INPUT_SIZE), sg.T("int 2")],
        [sg.Combo([1, 2, 3], k="combo_1", s=INPUT_SIZE), sg.T("Combo 1")],
        [sg.Combo(["a", "b", "c"], k="combo_2", s=INPUT_SIZE), sg.T("Combo 2")],
        [sg.Button("GO", key="go", s=INPUT_SIZE, tooltip="this is a tooltip")],
    ]

    extras = [
        [
            sg.Combo(sg.theme_list(), sg.theme(), enable_events=True, k="theme"),
            sg.T("Theme"),
        ],
        [sg.Checkbox("Custom Theme", False, enable_events=True, k="enable_theme")],
        [sg.Checkbox("Logging", False, k="logging")],
        [sg.Button("Test")],
    ]

    tabs = sg.TabGroup(
        [
            [
                sg.Tab("Extras", extras),
                # sg.Tab("Columns", columns),
                sg.Tab("Inputs", inputs),
                sg.Tab("Settings", fig_settings),
            ]
        ],
        k="tab_group",
    )
    layout = [header, [tabs], footer]
    return layout


# %% basic event logic for quick debug
if __name__ == "__main__":
    sg.theme("hot dog stand")
    window = make_window("FP Test", "99.99.99")
    while True:
        event, values = window.read()  # type: ignore

        # exit methods
        if event in ("Exit", sg.WIN_CLOSED):
            print("[LOG] Exit")
            break
