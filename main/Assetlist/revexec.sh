function revexec {
if [[ -f $1 ]];then
echo $1 > /Users/DaBros/Desktop/Reverie-Programming-Language-main/main/Assetlist/toexec.txt
open /Users/DaBros/Desktop/Reverie-Programming-Language-main/main/Reverie\ 0.2.1.py
else
echo "\'$1\' doesn't exist! Are you sure you typed the right path?"
}
