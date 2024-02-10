# change directory two levels up to project folder
$scriptpath = $MyInvocation.MyCommand.Path
$dir1 = Split-Path $scriptpath   # parent folder
$dir2 = Split-Path $dir1         # up second level
Set-Location $dir2


# Activate the virtual environment
$venvPath = ".\env-app"
& $venvPath\Scripts\activate

# update version info file
$versionScript = ".\support\create_version_file.py"
& $venvPath\Scripts\python.exe $versionScript

# Run the pyinstaller command
$launcherFile = ".\src\app\main.py"
$pyInstallerExecutable = "pyinstaller"
$appName = "template_app"
$versionFile = ".\support\app_version_info.txt"
$iconFile = ".\src\app\data\icon.ico"
# $addIcon = ".\app\data\icon.ico;.\data" # use this to add specific file
$addDataFolder = ".\src\app\data;.\data" # use this to add entire folder

# build command with settings args
& $pyInstallerExecutable $launcherFile --add-data $addDataFolder --version-file $versionFile -w -n $appName -i $iconFile --noconfirm --onefile

# deactivate environment
& deactivate