@ECHO off
IF EXIST %1% (
ECHO %1% > /Users/DaBros/Desktop/Reverie-Programming-Language-main/main/Assetlist/toexec.txt
START %1%
) ELSE (
ECHO '$1' doesn't exist! Are you sure you typed the right path?
)
