@echo off
color 0f

:main_page
cls
echo File Search
echo.
set /p file=File Name:
if EXIST %file% goto found
if NOT EXIST %file% goto not_found
goto main_page
cls

:found
cls
echo File Search
echo.
echo The file %file% was successfully indexed.
start %file%
goto main_page
cls

:not_found
cls
echo File Search
echo.
echo The file %file% was indexed but could not be found.
pause
goto main_page