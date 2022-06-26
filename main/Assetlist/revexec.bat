IF EXIST %1% (
@ECHO off
ECHO %1% > /Users/DaBros/Desktop/Reverie-Programming-Language-main/main/Assetlist/toexec.txt
) ELSE (
ECHO '$1' doesn't exist! Are you sure you typed the right path?
)
