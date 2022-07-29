ECHO Creating Directories..
MKDIR C:\Users\%USERNAME%\Reverie
MKDIR C:\Users\%USERNAME%\Reverie\src

ECHO Creating Files..
ECHO > C:\Users\%USERNAME%\Reverie\main.py\run

ECHO Downloading Files..
CURL https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/Reverie3\%2B/build/main.py > C:\Users\%USERNAME%\Reverie\main.py
CURL https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/Reverie3\%2B/build/src/func.sh > C:\Users\%USERNAME%\Reverie\src\func.sh
CURL https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/Reverie3\%2B/build/src/error.sh > C:\Users\%USERNAME%\Reverie\src\error.sh

ECHO Installation Finished! Thank You for Downloading the Reverie Programming Language!
