# change directory two levels up (to /src folder)
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath   # parent folder
Set-Location $dir
$dir = Split-Path $dir          # up second level
Set-Location $dir


# Activate the virtual environment
$venvPath = ".\env-app"
& $venvPath\Scripts\activate

# update version info file
$versionScript = ".\psg_app_template\create_version_file.py"
& $venvPath\Scripts\python.exe $versionScript

# Run the pyinstaller command
$launcherFile = ".\launcher.py"
$pyInstallerExecutable = "pyinstaller"
$appName = "app"
$versionFile = ".\psg_app_template\app_version_info.txt"
$iconFile = ".\icon.ico"
$addIcon = ".\icon.ico;."

& $pyInstallerExecutable $launcherFile --add-data $addIcon --version-file $versionFile -w -n $appName -i $iconFile --noconfirm --onefile

# deactivate environment
& deactivate