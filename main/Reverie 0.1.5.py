import os
import getpass
import time
import subprocess

path = f"/Users/{getpass.getuser()}/Desktop/Reverie-Programming-Language-main/main/"
sdir = os.listdir(path)
file = ""
filen = 0
pathstr = ""
while not filen == len(sdir)-1:
    filen += 1
    pathstr = f"{pathstr}{sdir[filen-1]}"
filen = 0
if ".rev" in pathstr:
    while not ".rev" in sdir[filen-1]:
        filen += 1
else:
    path = f"/Users/{getpass.getuser()}/Desktop/"
    sdir = os.listdir(path)
    while not ".rev" in sdir[filen-1]:
        filen += 1
file = f"{path}{sdir[filen-1]}"

script = []
for line in open(file, "r+"):
    script.append(line)
print(file)
mainum = 0
numone = 0
val = []
vals = []
line = ""
closers = ["\"", ")", ">", ","]
var = ["*","",""]
cond = False
lby = 0
sl = False

err = open(f"/Users/{getpass.getuser()}/Desktop/Reverie-Lang/Assetlist/error.txt","r")
errlist = []
for line in err:
    errlist.append(str(line))
def err(errnum):
    print(f"[!] {errlist[errnum]} Line ({mainum})")
    line = script[len(script)-1]
def getval():
    numone = line.index("(")
    while not line[numone+1] == ")":
        numone += 1
        if line[numone] == "\"":
            vals.append("")
            numone += 1
            while not line[numone] == "\"":
                vals[len(vals)-1] = f"{vals[len(vals)-1]}{line[numone]}"
                numone += 1
        if line[numone] == "<":
            vals.append("")
            while not line[numone+1] == ">":
                numone += 1
                vals[len(vals)-1] = f"{vals[len(vals)-1]}{line[numone]}"
            if vals[len(vals)-1] in var:
                i = var[var.index(vals[len(vals)-1])+1]
                if var[var.index(val[len(vals)-1])+2] == "int":
                    i = int(var[var.index(val[len(vals)-1])+1])
                vals[len(vals)-1] = i
            else:
                err(0)
        if line[numone] == "0":
            vals.append("")
            while line[numone] in "1234567890":
                vals[len(vals)-1] = f"{vals[len(vals)-1]}{line[numone]}"
                numone += 1
            i = int(vals[len(vals)-1])
            vals[len(vals)-1] = i
mainum = 0
while not mainum == len(script):
    mainum += 1
    line = script[mainum-1]
    if "system.write(" in line:
        getval()
        if len(vals) == 1:
            print(vals[0])
        else:
            err(7)

    if "var " in line:
        val = [""]
        numone = 8
        while not line[numone] == " ":
            numone += 1
            val[0] = f"{val[0]}{line[numone-1]}"
        if not val[0] in var:
            var.append(val[0])
            var.append("")
            var.append(line[4]+line[5]+line[6])
        vals = []
        getval()
        numone += 5
        if len(vals) == 1:
            var[var.index(val[0])+1] = vals[0]
        else:
            err(7)

    if "time.delay(" in line:
        vals = []
        getval()
        try:
            i = vals[0]+0
        except TypeError:
            err(4)
        else:
            time.sleep(vals[0])
        
                
    if "system.input(" in line:
        numone = 14
        val = [""]
        vals = []
        getval()
        while not line[numone] == "<":
            numone += 1
        val.append("")
        if line[numone] == "<":
            numone += 1
            while not line[numone] in closers:
                numone += 1
                val[1] = f"{val[1]}{line[numone-1]}"
            if val[len(val)-1] in var:
                var[var.index(val[len(val)-1])+1] = i
            else:
                err(0)

    if "if(" in line:
        val = [""]
        if "==" in line:
            numone = 4
            if line[numone-1] == "\"":
                while not line[numone] == closers[0]:
                    numone += 1
                    val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
            else:
                if line[numone-1] == "<":
                    while not line[numone] == closers[2]:
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = var[var.index(val[0])+1]
                    if var[var.index(val[0])+2] == "int":
                        i = int(var[var.index(val[0])+1])
                    val = [i]
                else:
                    while line[numone] in "0123456789":
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = int(val[0])
                    val = [i]
            numone += 4
            val.append("")
            if line[numone-1] == "\"":
                while not line[numone] == closers[0]:
                    numone += 1
                    val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
            else:
                if line[numone-1] == "<":
                    while not line[numone] == closers[2]:
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = var[var.index(val[0])+1]
                    if var[var.index(val[0])+2] == "int":
                        i = int(var[var.index(val[0])+1])
                    val[0] = i
                else:
                    while line[numone] in "0123456789":
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = int(val[0])
                    val = [i]
            cond = True
            if not val[0] == val[1]:
                cond = False
                while not "}" in script[mainum]:
                    mainum += 1
                    
        if "!=" in line:
            numone = 4
            if line[numone-1] == "\"":
                while not line[numone] == closers[0]:
                    numone += 1
                    val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
            else:
                if line[numone-1] == "<":
                    while not line[numone] == closers[2]:
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = var[var.index(val[0])+1]
                    if var[var.index(val[0])+2] == "int":
                        i = int(var[var.index(val[0])+1])
                    val = [i]
                else:
                    while line[numone] in "0123456789":
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = int(val[0])
                    val = [i]
            numone += 4
            val.append("")
            if line[numone-1] == "\"":
                while not line[numone] == closers[0]:
                    numone += 1
                    val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
            else:
                if line[numone-1] == "<":
                    while not line[numone] == closers[2]:
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = var[var.index(val[0])+1]
                    if var[var.index(val[0])+2] == "int":
                        i = int(var[var.index(val[0])+1])
                    val[0] = i
                else:
                    while line[numone] in "0123456789":
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = int(val[0])
                    val = [i]
            cond = True
            if not val[0] != val[1]:
                cond = False
                while not "}" in script[mainum-1]:
                    mainum += 1

        if "in" in line:
            numone = 4
            if line[numone-1] == "\"":
                while not line[numone] == closers[0]:
                    numone += 1
                    val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
            else:
                if line[numone-1] == "<":
                    while not line[numone] == closers[2]:
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = var[var.index(val[0])+1]
                    if var[var.index(val[0])+2] == "int":
                        i = int(var[var.index(val[0])+1])
                    val = [i]
                else:
                    while line[numone] in "0123456789":
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = int(val[0])
                    val = [i]
            numone += 4
            val.append("")
            if line[numone-1] == "\"":
                while not line[numone] == closers[0]:
                    numone += 1
                    val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
            else:
                if line[numone-1] == "<":
                    while not line[numone] == closers[2]:
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = var[var.index(val[0])+1]
                    if var[var.index(val[0])+2] == "int":
                        i = int(var[var.index(val[0])+1])
                    val[0] = i
                else:
                    while line[numone] in "0123456789":
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = int(val[0])
                    val = [i]
            cond = True
            if not val[0] in val[1]:
                cond = False
                while not "}" in script[mainum]:
                    mainum += 1

        if "!i" in line:
            numone = 4
            if line[numone-1] == "\"":
                while not line[numone] == closers[0]:
                    numone += 1
                    val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
            else:
                if line[numone-1] == "<":
                    while not line[numone] == closers[2]:
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = var[var.index(val[0])+1]
                    if var[var.index(val[0])+2] == "int":
                        i = int(var[var.index(val[0])+1])
                    val = [i]
                else:
                    while line[numone] in "0123456789":
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = int(val[0])
                    val = [i]
            numone += 4
            val.append("")
            if line[numone-1] == "\"":
                while not line[numone] == closers[0]:
                    numone += 1
                    val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
            else:
                if line[numone-1] == "<":
                    while not line[numone] == closers[2]:
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = var[var.index(val[0])+1]
                    if var[var.index(val[0])+2] == "int":
                        i = int(var[var.index(val[0])+1])
                    val[0] = i
                else:
                    while line[numone] in "0123456789":
                        numone += 1
                        val[len(val)-1] = f"{val[len(val)-1]}{line[numone-1]}"
                    i = int(val[0])
                    val = [i]
            cond = True
            if val[0] in val[1]:
                cond = False
                while not "}" in script[mainum]:
                    mainum += 1

    if "else" in line:
        if cond:
            mainum += 1
            while not "}" in script[mainum]:
                mainum += 1

    if "[" in line:
        numone = 1
        val = ["",""]
        if "+" in line:
            if line[numone] == "0":
                while line[numone+1] in "0123456789":
                    numone += 1
                    val[0] = f"{val[0]}{line[numone]}"
                i = int(val[0])
                val[0] = i
            else:
                if line[numone] == "<":
                    while line[numone+1] in "0123456789":
                        numone += 1
                        val[0] = f"{val[0]}{line[numone]}"
                    if val[0] in var:
                        print(val[0])
                        i = int(var[var.index(val[0])+1])
                        val[0] = i
                    else:
                        err(0)
            numone += 3
            if line[numone] == "0":
                while line[numone+1] in "0123456789":
                    numone += 1
                    val[1] = f"{val[1]}{line[numone]}"
                i = int(val[1])
                val[1] = i
            else:
                if line[numone] == "<":
                    while line[numone+1] in "0123456789":
                        numone += 1
                        val[1] = f"{val[1]}{line[numone]}"
                    if val[1] in var:
                        i = int(var[var.index(val[1])+1])
                        val[1] = i
                    else:
                        err(0)

        if "-" in line:
            if line[numone] == "0":
                while line[numone+1] in "0123456789":
                    numone += 1
                    val[0] = f"{val[0]}{line[numone]}"
                i = int(val[0])
                val[0] = i
            else:
                if line[numone] == "<":
                    while line[numone+1] in "0123456789":
                        numone += 1
                        val[0] = f"{val[0]}{line[numone]}"
                    if val[0] in var:
                        i = int(var[var.index(val[0])+1])
                        val[0] = i
                    else:
                        err(0)
            numone += 3
            if line[numone] == "0":
                while line[numone+1] in "0123456789":
                    numone += 1
                    val[1] = f"{val[1]}{line[numone]}"
                i = int(val[1])
                val[1] = i
            else:
                if line[numone] == "<":
                    while line[numone+1] in "0123456789":
                        numone += 1
                        val[1] = f"{val[1]}{line[numone]}"
                    if val[1] in var:
                        i = int(var[var.index(val[1])+1])
                        val[1] = i
                    else:
                        err(0)
            var[var.index("*")+1] = int(val[0])-int(val[1])

        if "x" in line:
            if line[numone] == "0":
                while line[numone+1] in "0123456789":
                    numone += 1
                    val[0] = f"{val[0]}{line[numone]}"
                i = int(val[0])
                val[0] = i
            else:
                if line[numone] == "<":
                    while line[numone+1] in "0123456789":
                        numone += 1
                        val[0] = f"{val[0]}{line[numone]}"
                    if val[0] in var:
                        i = int(var[var.index(val[0])+1])
                        val[0] = i
                    else:
                        err(0)
            numone += 3
            if line[numone] == "0":
                while line[numone+1] in "0123456789":
                    numone += 1
                    val[1] = f"{val[1]}{line[numone]}"
                i = int(val[1])
                val[1] = i
            else:
                if line[numone] == "<":
                    while line[numone+1] in "0123456789":
                        numone += 1
                        val[1] = f"{val[1]}{line[numone]}"
                    if val[1] in var:
                        i = int(var[var.index(val[1])+1])
                        val[1] = i
                    else:
                        err(0)
            var[var.index("*")+1] = int(val[0])*int(val[1])
            
        if "of" in line:
            if line[numone] == "0":
                while line[numone+1] in "0123456789":
                    numone += 1
                    val[0] = f"{val[0]}{line[numone]}"
            else:
                err(4)
            numone += 3
            while not line[numone+1] in closers:
                numone += 1
                val[1] = f"{val[1]}{line[numone]}"
            if line[numone+1] == ">":
                if val[1] in var:
                    i = var[var.index(val[1])+1]
                    var[1] = 1
                else:
                    var[1] = val[1][int(val[0])-1]

        if "len(" in line:
            vals = []
            getval()
            if len(vals) == 1:
                var[1] = len(vals[0])
            else:
                err(7)
                    

    if "file.open(" in line:
        vals = []
        getval()
        if len(vals) == 1:
            os.system(f"open {vals[0]}")
        else:
            err(7)
                
    if "file.read(" in line:
        numone = 11
        val = [""]
        while not line[numone] in closers:
            val[0] = f"{val[0]}{line[numone]}"
            numone += 1
        if not "\"" == line[numone]:
            if ">" == line[numone]:
                if val[0] in var:
                    if var[var.index(val[0])+2] == "str":
                        i = var[var.index(val[0])+1]
                        val[0] = i
                else:
                    print(f"[!] Variable Doesn't Exist ({mainum})")
            else:
                print(f"[!] Function doesn't support int. ({mainum})")
        numone += 3
        val.append("")
        while not line[numone] in closers:
            val[1] = f"{val[1]}{line[numone]}"
            numone += 1
        if line[numone] == ">":
            if val[1] in var:
                var[var.index(val[1])+1] = open(val[0],"r+").read()
            else:
                print(f"[!] Variable Doesn't Exist ({mainum})")
        else:
            print(f"[!] Function only supports var. ({mainum})")

    if "file.addln(" in line:
        numone = 12
        val = [""]
        while not line[numone] in closers:
            val[0] = f"{val[0]}{line[numone]}"
            numone += 1
        if not "\"" == line[numone]:
            if ">" == line[numone]:
                if val[0] in var:
                    if var[var.index(val[0])+2] == "str":
                        i = var[var.index(val[0])+1]
                        val[0] = i
                else:
                    err(0)
        numone += 3
        val.append("")
        while not line[numone] in closers:
            val[1] = f"{val[1]}{line[numone]}"
            numone += 1
        if line[numone] == ">":
            if val[1] in var:
                if var[var.index(val[1])+2] == "str":
                    i = var[var.index(val[1])+1]
                    val[1] = i
            else:
                err(0)
        for line in open(val[1], "a+"):
            open(val[1], "a+").write(line)
        open(val[1], "a+").write(val[0])

    if "arr" in line:
        numone = 4
        val = []
        while not numone == line.index("}"):
            numone += 1
            if line[numone] == "\"":
                numone += 1
                val.append("")
                while not line[numone] == "\"":
                    val[len(val)-1] = f"{val[len(val)-1]}{line[numone]}"
                    numone += 1
                numone += 1
            if line[numone] == "0":
                numone += 1
                val.append("")
                while line[numone] in "1234567890":
                    val[len(val)-1] = f"{val[len(val)-1]}{line[numone]}"
                    numone += 1
                numone += 1
            if line[numone] == "<":
                numone += 1
                val.append("")
                while not line[numone] == ">":
                    val[len(val)-1] = f"{val[len(val)-1]}{line[numone]}"
                    numone += 1
                if val[len(val)-1] in var:
                    i = var[var.index(val[len(val)-1])+1]
                    val[len(val)-1] = i
                else:
                    err(0)
                numone += 1
        numone += 3
        val.append("")
        while not numone+1 == line.index("\n"):
            numone += 1
            val[len(val)-1] = f"{val[len(val)-1]}{line[numone]}"
        if not val[len(val)-1] in var:
            var.append(val[len(val)-1])
            var.append("")
            var.append("arr")
        numone = -1
        while not numone == len(val)-2:
            numone += 1
            var[var.index(val[len(val)-1])+1] = f"{var[var.index(val[len(val)-1])+1]}{val[numone]},"

    if "add(" in line:
        numone = 5
        val = [""]
        while not line[numone] in closers:
            val[len(val)-1] = f"{val[len(val)-1]}{line[numone]}"
            numone += 1
        if line[numone] == ">":
            if val[0] in var:
                i = var[var.index(val[0])+1]
                val[0] = i
            else:
                err(0)
        numone += 2
        val.append("")
        if line[numone] == "<":
            while not line[numone+1] in closers:
                numone += 1
                val[1] = f"{val[1]}{line[numone]}"
            if val[1] in var:
                if var[var.index(val[1])+2] == "arr":
                    var[var.index(val[1])+1] = f"{var[var.index(val[1])+1]}{val[0]},"
                else:
                    var[var.index(val[1])+1] = f"{var[var.index(val[1])+1]}{val[0]}"
            else:
                err(0)
        else:
            err(6)

    if "file.create(" in line:
        vals = []
        getval()
        if len(vals) == 2:
            try:
                i = vals[0]+0
            except TypeError:
                try:
                    i = os.listdir(os.listdir(vals[1]))
                except FileNotFoundError:
                    err(10)
                else:
                    if vals[0] in os.listdir(vals[1]):
                        err(9)
                    else:
                        i = open(f"{vals[1]}{vals[0]}","w+")
                        i.close()
            else:
                err(4)
        else:
            err(7)

    if "goto(" in line:
        getval()
        try:
            i = vals[0]+0
        except TypeError:
            err(1)
        else:
            if len(vals) == 1:
                mainum = vals[0]-1
            else:
                err(7)

    if "waituntil(" in line:
        getval()
        if "==" in line:
            if len(vals) == 2:
                while not vals[0] == vals[1]: time.sleep(0)
            else:
                err(7)
        if "!=" in line:
            if len(vals) == 2:
                while not vals[0] != vals[1]: time.sleep(0)
            else:
                err(7)
        if "in" in line:
            if len(vals) == 2:
                while not vals[0] in vals[1]: time.sleep(0)
            else:
                err(7)
        if "!i" in line:
            if len(vals) == 2:
                while vals[0] in vals[1]: time.sleep(0)
            else:
                err(7)
    vals = []
time.sleep(1)
