# %% imports
import os.path
from pyinstaller_versionfile import create_versionfile

from psg_app_template.front_panel import APP_VERSION, NAME


# %% build path for version info file output
folder = os.path.dirname(os.path.abspath(__file__))
filename = "app_version_info.txt"
filepath = os.path.join(folder, filename)


# %% generate file
create_versionfile(
    output_file=filepath,
    version=APP_VERSION,
    # company_name="ACME Inc.",
    file_description=NAME,
    product_name=NAME,
    # internal_name="Simple App",
    # legal_copyright="© Scott Baldwin 2023. All rights reserved.",
    # original_filename="SimpleApp.exe",
)
print(f"version file created/updated: {filepath}")
