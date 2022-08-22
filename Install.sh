echo "Creating Directories.."
if ! [ -d "/Users/$USER/Reverie" ];then
    mkdir "/Users/$USER/Reverie"
fi
if ! [ -d "/Users/$USER/Reverie/src" ];then
    mkdir "/Users/$USER/Reverie/src"
fi

echo "Creating Files.."
echo > "/Users/$USER/Reverie/src/run"

echo "Downloading Files.."
curl -s "https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/Reverie3%2B/build/main.py" > "/Users/$USER/Reverie/main.py"
curl -s "https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/Reverie3%2B/build/src/func.sh" > "/Users/$USER/Reverie/src/func.sh"
curl -s "https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/Reverie3%2B/build/src/error.sh" > "/Users/$USER/Reverie/src/error.sh"
curl -s "https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/Reverie3%2B/build/reverie.sh" > "/Users/$USER/reverie.sh"
status="Installation Finished! Thank You for Downloading the Reverie Programming Language!"
if ! [ -d "/Users/$USER/Reverie" ];then
    status="Failed to Create '/Users/$USER/Reverie'"
fi
if ! [ -d "/Users/$USER/Reverie/" ];then
    status="Failed to Create '/Users/$USER/Reverie/src'"
fi


if ! [ -f "/Users/$USER/Reverie/main.py" ];then
    status="Failed to Create '/Users/$USER/Reverie/main.py'"
fi

if ! [ -f "/Users/$USER/Reverie/src/run" ];then
    status="Failed to Create '/Users/$USER/Reverie/src/run'"
fi
if ! [ -f "/Users/$USER/Reverie/src/func.sh" ];then
    status="Failed to Create '/Users/$USER/Reverie/src/func.sh'"
fi
if ! [ -f "/Users/$USER/Reverie/src/run/error.sh" ];then
    status="Failed to Create '/Users/$USER/Reverie/src/error.sh'"
fi
echo $status
