function reverie {
  if [[ "$1"=="exec" ]];then
    if [[ -f "$2" ]];then
      echo $2 > /Users/$USER/Reverie/src/run
      python3 /Users/$USER/Reverie/main.py
    else
      echo "'$2' Doesn't seem to exist! Check your spelling."
  fi
}
