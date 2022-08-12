# put([type], [str/int/var])
if [ $1 -eq 1 ];then
	if [[ "$3" == "" ]];then
		sh /Users/$USER/Reverie/src/error.sh 3 $2
	else
		if [[ "$3" == "-d" ]];then
			if [ $# -eq 4 ];then
				echo $4
			else
				sh /Users/$USER/Reverie/src/error.sh 1 $2
			fi
		fi
		if [[ "$3" == "-f" ]];then
			if [ $# -eq 5 ];then
				if [[ -f $5 ]];then
					echo $4 > $5
				else
					sh /Users/$USER/Reverie/src/error.sh 4 $2
				fi
			else
				sh /Users/$USER/Reverie/src/error.sh 1 $2
			fi
		fi
	fi
fi
# pause([int/var])
if [ $1 -eq 2 ];then
	if [ $# -eq 3 ];then
		sleep $3
		if ! [ $? -eq 0 ];then
			sh /Users/$USER/Reverie/src/error.sh 2 $2
		fi
	else
		sh /Users/$USER/Reverie/src/error.sh 1 $2
	fi
fi
# open(str)
if [ $1 -eq 3 ];then
	if [ $# -eq 3 ];then
		if [ -f $3 ];then
			open $3
		else
			sh /Users/$USER/Reverie/src/error.sh 4 $2
		fi
		if ! [ $? -eq 0 ];then
			sh /Users/$USER/Reverie/src/error.sh 6 $2
		fi
	else
		sh /Users/$USER/Reverie/src/error.sh 1 $2
	fi
fi
# move([type], [str/var])
if [ $1 -eq 4 ];then
	if [[ "$3" == "" ]];then
		sh /Users/$USER/Reverie/src/error.sh 3 $2
	else
		if [[ "$3" == "-d" ]];then
			if [ $# -eq 4 ];then
				if [ -f $3 ];then
					if [ -d $4 ];then
						mv $3 $4
					else
						sh /Users/$USER/Reverie/src/error.sh 4 $2
					fi
				else
					sh /Users/$USER/Reverie/src/error.sh 4 $2
				fi
			else
				sh /Users/$USER/Reverie/src/error.sh 1 $2
			fi
		fi
		if [[ "$3" == "-r" ]];then
			if [ $# -eq 5 ];then
				if [ -f $4 ];then
					if ! [ -f $5 ];then
						mv $4 $5
					else
						sh /Users/$USER/Reverie/src/error.sh 7 $2
					fi
				else
					sh /Users/$USER/Reverie/src/error.sh 4 $2
				fi
			else
				sh /Users/$USER/Reverie/src/error.sh 1 $2
			fi
		fi
	fi
fi
