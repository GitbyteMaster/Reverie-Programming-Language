ECHO Installing Reverie..
MKDIR /Users/$USER/Desktop/Reverie-Programming-Language-main/
MKDIR /Users/$USER/Desktop/Reverie-Programming-Language-main/main/
CURL https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/main/main/Reverie.py > /Users/$USER/Desktop/Reverie-Programming-Language-main/main/Reverie.py
MKDIR /Users/$USER/Desktop/Reverie-Programming-Language-main/main/Assetlist/

CURL https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/main/main/Assetlist/error.txt > /Users/$USER/Desktop/Reverie-Programming-Language-main/main/Assetlist/error.txt
ECHO empty > /Users/$USER/Desktop/Reverie-Programming-Language-main/main/Assetlist/cmdobj.txt
CURL https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/main/main/Assetlist/context.py > /Users/$USER/Desktop/Reverie-Programming-Language-main/main/Assetlist/context.py
ECHO empty > /Users/$USER/Desktop/Reverie-Programming-Language-main/main/Assetlist/toexec.txt
CURL https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/main/main/Assetlist/revexec.sh > /Users/$USER/Desktop/Reverie-Programming-Language-main/main/Assetlist/revexec.sh

ECHO Installation Finished! Thank You for Downloading the Reverie Programming Language!
