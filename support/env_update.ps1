# change directory two levels up
$scriptpath = $MyInvocation.MyCommand.Path
$dir1 = Split-Path $scriptpath   # parent folder
$dir2 = Split-Path $dir1         # up second level
Set-Location $dir2

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