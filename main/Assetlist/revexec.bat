@ECHO off
IF "%1%"=="execute" do (
IF EXIST %2% (
ECHO %1% > /Users/DaBros/Desktop/Reverie-Programming-Language-main/main/Assetlist/toexec.txt
START /Users/DaBros/Desktop/Reverie-Programming-Language-main/main/Reverie.py
) ELSE (
ECHO '$1' doesn't exist! Are you sure you typed the right path?
)
)
IF "%1%"=="install" (
if NOT EXIST /Users/$USER/Desktop/Reverie-Programming-Language-main/main/struct (
MKDIR /Users/$USER/Desktop/Reverie-Programming-Language-main/main/struct
)
IF NOT EXIST C:\Users\%USERNAME%\Desktop\Reverie-Programming-Language-main\main\struct\%1% (
MKDIR C:\Users\%USERNAME%\Desktop\Reverie-Programming-Language-main\main\struct\%1%
)
CURL https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/main/struct/%1%/%2% > C:\Users\%USERNAME%\Desktop\Reverie-Programming-Language-main\main\struct%1%\%2%
if %ERRORLEVEL%==6 (
cls
ECHO The function or structure you tried to install doesn't exist! Check your spelling.
)
)
