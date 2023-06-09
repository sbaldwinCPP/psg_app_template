# change directory to location of this script
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
Set-Location $dir

# Activate the virtual environment
$venvPath = ".\env-app"
& $venvPath\Scripts\activate

# update version info file
$versionScript = ".\create_version_file.py"
& $venvPath\Scripts\python.exe $versionScript

# Run the pyinstaller command
$pyInstallerExecutable = "pyinstaller"
$launcherFile = ".\launcher.py"
$appName = "app"
$versionFile = ".\app_version_info.txt"
$iconFile = ".\icon.ico"
$addIcon = ".\icon.ico;."

& $pyInstallerExecutable $launcherFile --add-data $addIcon --version-file $versionFile -w -n $appName -i $iconFile 

# deactivate environment
& deactivate