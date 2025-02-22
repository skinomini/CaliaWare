@echo off
:open
color 5d
echo +==============[ Welcome to Edgeware Setup~ ]==============+
echo Python Version:
py --version 
if NOT %errorlevel%==0 goto pyInstall
goto pip
:pyInstall
echo Could not find Python.
echo Now downloading installer from python.org, please wait...
reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" > NUL && set OS=32BIT || set OS=64BIT
if %OS%==32BIT powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.11.3/python-3.11.3.exe', 'pyinstaller.exe')"
if %OS%==64BIT powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe', 'pyinstaller.exe')"
echo Done downloading executable.
echo Please complete installation through the installer before continuing.
start %CD%\pyinstaller.exe
pause
:verifyInstallation
py --version
if NOT %errorlevel%==0 goto quit
goto pip
:pip
echo Installing pip packages.
pip install -r requirements.txt
goto run
:run
echo Edgeware is ready to start.
pause
start "Edgeware" "%CD%/EdgeWare/start.pyw"
exit
:quit
echo Python still could not be found.
pause
