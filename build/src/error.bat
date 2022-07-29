CLS
IF "%1"=="1" (
	ECHO [!] Line %2 - Insufficient amount of parameters
)
IF "%1"=="2" (
	ECHO [!] Line %2 - Expected integer
)
IF "%1"=="3" (
	ECHO [!] Line %2 - No type assigned
)
IF "%1"=="4" (
	ECHO [!] Line %2 - File/Directory does not exist
)
IF "%1"=="5" (
	ECHO [!] Line %2 - Invalid syntax: Please close parenthesis
)
IF "%1"=="6" (
	ECHO [!] Line %2 - Expected string
)
