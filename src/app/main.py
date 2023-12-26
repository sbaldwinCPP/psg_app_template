# %%
import front_panel as fp
import event_logic as el


APP_NAME = "TemplateApp"
APP_VERSION = "0.0.0.0"


def main():
    window = fp.make_window(name=APP_NAME, version=APP_VERSION)
    el.run(window)


# %%
if __name__ == "__main__":
    main()
