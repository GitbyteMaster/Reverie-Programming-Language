IF "%1"=="exec" (
  IF EXIST "%1" (
    ECHO %2 > C:\Users\%USERNAME%\Reverie\src\run
    python C:\Users\%USERNAME%\Reverie\main.py
  ) ELSE (
    ECHO '%2' Doesn't seem to exist! Check your spelling.
  )
)
