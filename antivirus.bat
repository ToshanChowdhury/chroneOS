@echo off
color 0f

:mainpage
cls
echo Antivirus
echo.
echo 1. Search For Viruses
echo 2. Exit
set /p option=:
if %option% == 1 goto detection
if %option% == 2 exit
cls
goto mainpage

:detection
cls
echo Antivirus
echo.
echo Scanning . . .
if exist virus.bat goto warning
if not exist virus.bat goto safe
cls
goto detection

:warning
cls
echo Antivirus
echo.
echo WARNING!! VIRUS DETECTED !!!
echo Deleting Virus . . .
del virus.bat
cls
exit

:safe
cls
echo SYSTEM SECURE!!
exit
cls
