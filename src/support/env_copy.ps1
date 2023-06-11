# change directory two levels up (to /src folder)
$scriptpath = $MyInvocation.MyCommand.Path
# parent folder of this script
$dir = Split-Path $scriptpath   
Set-Location $dir  
# up second level
$dir = Split-Path $dir         
Set-Location $dir

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