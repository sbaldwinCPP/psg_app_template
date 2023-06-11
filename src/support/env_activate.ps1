# change directory two levels up (to /src folder)
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath   # up one level
$dir = Split-Path $dir          # up second level
Set-Location $dir

# Activate the virtual environment
$venvPath = ".\env-app"
& $venvPath\Scripts\activate