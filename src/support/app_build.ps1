# change directory two levels up (to /src folder from src/support/this_file path)
$scriptpath = $MyInvocation.MyCommand.Path
$dir1 = Split-Path $scriptpath   # parent folder
# Set-Location $dir1
$dir2 = Split-Path $dir1         # up second level
Set-Location $dir2


# Activate the virtual environment
$venvPath = ".\env-app"
& $venvPath\Scripts\activate

# update version info file
$versionScript = ".\support\create_version_file.py"
& $venvPath\Scripts\python.exe $versionScript

# Run the pyinstaller command
$launcherFile = ".\app\main.py"
$pyInstallerExecutable = "pyinstaller"
$appName = "template_app"
$versionFile = ".\support\app_version_info.txt"
$iconFile = ".\src\icons\icon.ico"
$addIcon = ".\src\icons\icon.ico;."

& $pyInstallerExecutable $launcherFile --add-data $addIcon --version-file $versionFile -w -n $appName -i $iconFile --noconfirm --onefile

# deactivate environment
& deactivate