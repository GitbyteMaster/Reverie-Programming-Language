function revexec {
if [[ -f $1 ]]; then
echo $1 > /Users/$USER/Desktop/Reverie-Programming-Language-main/main/Assetlist/toexec.txt
open /Users/DaBros/Desktop/Reverie-Programming-Language-main/main/Reverie\ 0.2.1.py
else
echo "'$1' doesn't exist! Are you sure you typed the right path?"
fi
}
function revinstall {
if [[ ! -d /Users/$USER/Desktop/Reverie-Programming-Language-main/main/struct ]]; then
mkdir /Users/$USER/Desktop/Reverie-Programming-Language-main/main/struct
fi
if [[ ! -d /Users/$USER/Desktop/Reverie-Programming-Language-main/main/struct/$1 ]]; then
mkdir /Users/$USER/Desktop/Reverie-Programming-Language-main/main/struct/$1
fi
curl https://raw.githubusercontent.com/GitbyteMaster/Reverie-Programming-Language/main/struct/$1/$2 > /Users/$USER/Desktop/Reverie-Programming-Language-main/main/struct/$1/$2
if [[ $? -eq 6 ]]; then
clear
echo "The function or structure you tried to install doesn't exist! Check your spelling."
fi
}
