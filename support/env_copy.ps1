# change directory two levels up to project folder
$scriptpath = $MyInvocation.MyCommand.Path
$dir1 = Split-Path $scriptpath   # parent folder
$dir2 = Split-Path $dir1         # up second level
Set-Location $dir2

# define paths
$pythonExecutable = "py"
$venvPath = ".\env-app"
$requirementsFile = ".\requirements.txt"

# Create the Python virtual environment
& $pythonExecutable -m venv $venvPath

# Activate the virtual environment
& $venvPath\Scripts\activate

# update pip
& $venvPath\Scripts\python.exe -m pip install --upgrade pip

# Install packages from requirements.txt
& pip install -r $requirementsFile

# deactivate environment
& deactivate