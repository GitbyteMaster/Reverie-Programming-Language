clear
if [ $1 -eq 1 ];then
	echo [!] Line $2 - Insufficient amount of parameters
fi
if [ $1 -eq 2 ];then
	echo [!] Line $2 - Expected integer
fi
if [ $1 -eq 3 ];then
	echo [!] Line $2 - No type assigned
fi
if [ $1 -eq 4 ];then
	echo [!] Line $2 - File/Directory does not exist
fi
if [ $1 -eq 5 ];then
	echo [!] Line $2 - Invalid syntax: Please close parenthesis
fi
if [ $1 -eq 6 ];then
	echo [!] Line $2 - Expected string
fi
if [ $1 -eq 7 ];then
	echo [!] Line $2 - File already exist
fi
