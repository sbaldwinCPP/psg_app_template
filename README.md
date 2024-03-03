pysimplegui has gone to a subscription model as of version 5. 
work on this template will be stopped.

# psg_app_template
<img src="icon.png" alt="icon" width="100"/>

Collection of useful things into a simple app template.

## Intro
This readme should serve as a quick start guide. Information on underlying details should be set up in the [docs](/docs) folder (WIP).

## Credit
List of open-source 3rd party libraries used for this tool, with links to more info:
* PySimpleGUI - used to make GUI windows and event logic - [docs](https://www.pysimplegui.org/en/latest/) | [github](https://github.com/PySimpleGUI/PySimpleGUI) 
    * Also, check out the [cookbook](https://www.pysimplegui.org/en/latest/cookbook/) for code examples
* PyInstaller - used to bundle the app as a portable executable file - [docs](https://www.pyinstaller.org/en/stable/index.html) | [github](https://github.com/pyinstaller/pyinstaller)
* Include any other 3rd party or custom resources here

See the [requirements](/src/requirements.txt) file for a comprehensive list of all binaries used in the app.

## Virtual Environments
The use of a virtual environment is strongly recommended, especially while building the app to an executable. See powershell [script](src/support/env_copy.ps1) in the support folder to automatically setup a virtual environment.  

## Future Improvements
* add docs template
* add tests template - still need to learn how to unit-test the GUI side of things