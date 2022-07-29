REM put([type], [str/int/var])
IF "%1"=="1" (
IF "%3" == "" (
CALL C:\Users\%USERNAME%\Reverie\src\error.bat 3 %2
) ELSE (
IF "%3"=="-d" (
IF "%5"!="" (
ECHO %4
) ELSE (
CALL C:\User\%USERNAME%\Reverie\src\error.bat 1 %2
)
)
IF "%3"=="-f" (
IF "%6"=="" (
IF EXIST %5 (
ECHO %4 > %5
) ELSE (
CALL C:\Users\%USERNAME%\Reverie\src\error.bat 4 %2
)
) ELSE (
CALL C:\Users\%USERNAME%\Reverie\src\error.bat 1 $2
)
)
)
)
# pause([int])
if "%1"=="2" (
if "%4"!="" (
TIMEOUT %3
IF "%ERRORLEVEL%"!="0" (
CALL C:\Users\%USERNAME%\Reverie\src\error.bat 2 %2
)
) ELSE (
CALL C:\Users\%USERNAME%\Reverie\src\error.bat 1 $2
)
)
# open(str)
IF "%1"=="3" (
IF "%4"!="" (
START %3
IF "%ERRORLEVEL%"=="0" (
CALL C:\Users\%USERNAME%\Reverie\src\error.bat 6 %2
)
) ELSE (
CALL C:\Users\%USERNAME%\Reverie\src\error.bat 1 %2
)
)
