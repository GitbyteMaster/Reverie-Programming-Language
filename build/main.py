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
mainum = 0
literal = False
if platform.system() == "Darwin":
    os.system("clear")
else:
    os.system("cls")
if platform.system() != "Darwin":
    os.system(f"title {sdir[filen-1]}")
note = False
while not mainum == len(script):
    literal = False
    mainum += 1
    line = script[mainum-1]
    if not "//" in line or note:
        if "put" in line:
            if platform.system() != "Windows":
                paramcollect()
                os.system(f"sh /Users/{getpass.getuser()}/Reverie/src/func.sh 1 {mainum} {vals}")

    vals = ""
time.sleep(1)
