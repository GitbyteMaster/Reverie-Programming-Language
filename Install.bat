@ECHO OFF
ECHO Creating Directories..
IF NOT EXIST C:\Users\%USERNAME%\Reverie (
  MKDIR C:\Users\%USERNAME%\Reverie
)
IF NOT EXIST C:\Users\%USERNAME%\Reverie\src (
 MKDIR C:\Users\%USERNAME%\Reverie\src
)

ECHO Creating Files..
ECHO > C:\Users\%USERNAME%\Reverie\src\run

ECHO Downloading Files..
CURL https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/Reverie3%2B/build/main.py > C:\Users\%USERNAME%\Reverie\main.py
CURL https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/Reverie3%2B/build/src/func.bat > C:\Users\%USERNAME%\Reverie\src\func.bat
CURL https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/Reverie3%2B/build/src/error.bat > C:\Users\%USERNAME%\Reverie\src\error.bat
CURL https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/Reverie3%2B/build/reverie.bat > C:\Users\%USERNAME%\reverie.bat

SET status = Installation Finished! Thank You for Downloading the Reverie Programming Language!
if NOT EXIST C:\Users\$%USERNAME%\Reverie (
    SET status = Failed to Create 'C:\Users\%USERNAME%\Reverie'
)
if NOT EXIST C:\Users\$%USERNAME%\Reverie\src (
    SET status = Failed to Create 'C:\Users\%USERNAME%\Reverie\src'
)

if NOT EXIST C:\Users\$%USERNAME%\Reverie\main.py (
    SET status = Failed to Create 'C:\Users\%USERNAME%\Reverie\main.py'
)
if NOT EXIST C:\Users\$%USERNAME%\Reverie\src\run (
    SET status = Failed to Create 'C:\Users\%USERNAME%\Reverie\run'
)
if NOT EXIST C:\Users\$%USERNAME%\Reverie\src\func.bat (
    SET status = Failed to Create 'C:\Users\%USERNAME%\Reverie\src\func.bat'
)
if NOT EXIST C:\Users\$%USERNAME%\Reverie\src\error.bat (
    SET status = Failed to Create 'C:\Users\%USERNAME%\Reverie\src\error.bat'
)
echo $status
