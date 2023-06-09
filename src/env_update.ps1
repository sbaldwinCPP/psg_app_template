# change directory to location of this script
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
Set-Location $dir

# Create the Python virtual environment
$pythonExecutable = "py"
$venvPath = ".\env-app"
& $pythonExecutable -m venv $venvPath

# Activate the virtual environment
& $venvPath\Scripts\activate

# update pip
& $venvPath\Scripts\python.exe -m pip install --upgrade pip

# reset environment
& pip freeze > freeze.txt
pip uninstall -r freeze.txt -y
Remove-Item freeze.txt

# install & update dependencies with pip
& pip install --upgrade pysimplegui
& pip install --upgrade pyinstaller
& pip install --upgrade pyinstaller_versionfile

# update requirements file
& pip freeze > requirements.txt

# deactivate environment
& deactivate