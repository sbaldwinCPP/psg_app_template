import PySimpleGUI as sg

# highest level module, entry point for build scripts
# import other high & low level modules
import front_panel as fp
import event_logic as logic


APP_NAME = "TemplateApp"
APP_VERSION = "0.0.0.999"


def main():
    sg.theme("reddit")
    window = fp.make_window(name=APP_NAME, version=APP_VERSION)
    logic.run(window, APP_NAME, APP_VERSION)


if __name__ == "__main__":
    main()
