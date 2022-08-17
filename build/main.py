import os
import getpass
import time
import subprocess
import os.path
import sys
import platform

script = []
for line in open(open(f"/Users/{getpass.getuser()}/Reverie/src/run", "r+").read(),"r+"):
    script.append(line)
vals = ""
def paramcollect():
    global vals
    vals = ""
    exval = ""
    numone = line.index("(")
    if ")" in line:
        while not numone == line.index(")"):
            numone += 1
            if line[numone] == "\"":
                vals = f"{vals} \""
                numone += 1
                while not line[numone] == "\"":
                    vals = f"{vals}{line[numone]}"
                    numone += 1
                vals = f"{vals}\""            
    else:
        if platform.system() != "Windows":
            os.system("sh /Users/{getpass.getuser()/Reverie/src/error.sh 5 {mainum}")
        else:
            os.system("CALL C:\Users\{getpass.getuser()}\Reverie\src\error.sh 5 {mainum}")
mainum = 0
literal = False
if platform.system() != "":
    os.system("clear")
else:
    os.system("cls")
if platform.system() != "Darwin":
    os.system(f"title {sdir[filen-1]}")
note = False
var = []
data = []
while not mainum == len(script):
    literal = False
    mainum += 1
    line = script[mainum-1]
    if not "//" in line or note:
        callnum = 0
        
        # Functions in engine
        if "put(" in line:
            callnum = 1
        if "pause(" in line:
            callnum = 2
        if "open(" in line:
            callnum = 3
        if "move(" in line:
            callnum = 4
            
        # Call function through engine (func.bat/sh)
        if callnum != 0:
            paramcollect()
            if platform.system() != "Windows":
                os.system(f"sh /Users/$USER/Reverie/src/func.sh {callnum} {mainum} {vals}")
            else:
                os.system(f"CALL C:\Users\%USERNAME\Reverie\func.bat {callnum} {mainum} {vals}")
            
        # Functions in Python
        if "var " in line and "=" in line:
            paramcollect()
            numone = line.index("var")+5
            data = [""]
            while not line[numone] == " ":
                data[len(data)-1] = f"{data[len(data)-1]}{line[numone]}"
            
            
    vals = ""
time.sleep(1)
