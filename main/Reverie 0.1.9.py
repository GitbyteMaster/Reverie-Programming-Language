import os
import getpass
import time
import subprocess
import os.path

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
numtwo = 0
val = []
vals = []
line = ""
closers = ["\"", ")", ">", ","]
var = ["*","","","LastErr","","str"]
cond = False
lby = 0
sl = False
exval = ""

err = open(f"/Users/{getpass.getuser()}/Desktop/Reverie-Programming-Language-main/main/Assetlist/error.txt","r")
cmdobj = open(f"/Users/{getpass.getuser()}/Desktop/Reverie-Programming-Language-main/main/Assetlist/cmdobj.txt","w+")
errlist = []
for line in err:
    errlist.append(str(line))
def err(errnum):
    print(f"[!] {errlist[errnum]} Line ({mainum})")
    exval = ""
    numtwo = 0
    while not errlist[errnum][numtwo] == " ":
        exval = f"{exval}{errlist[errnum][numtwo]}"
        numtwo += 1
    var[4] = exval
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
                if not literal:
                    i = var[var.index(vals[len(vals)-1])+1]
                    if var[var.index(vals[len(vals)-1])+2] == "int":
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
vals = []
literal = False
while not mainum == len(script):
    literal = False
    mainum += 1
    line = script[mainum-1]
    if "system.write" in line:
        getval()
        if len(vals) == 1:
            print(vals[0])
        else:
            err(7)

    if "var " in line:
        val = [""]
        numone = line.index("var")+8
        while not line[numone] == " ":
            numone += 1
            val[0] = f"{val[0]}{line[numone-1]}"
        if not val[0] in var:
            var.append(val[0])
            var.append("")
            var.append(line[line.index("var")+4]+line[line.index("var")+5]+line[line.index("var")+6])

        vals = []
        getval()
        numone += 5
        if len(vals) == 1:
            var[var.index(val[0])+1] = vals[0]
        else:
            err(7)

    if "time.delay" in line:
        vals = []
        getval()
        try:
            i = vals[0]+0
        except TypeError:
            err(4)
        else:
            time.sleep(vals[0])
        
                
    if "system.input" in line:
         literal = True
         getval()
         if len(vals) == 2:
            if vals[1] in var:
                var[var.index(vals[1])+1] = input(vals[0])
            else:
                err(0)
         else:
            err(7)

    if "if(" in line:
        getval()
        if "==" in line:
            cond = True
            if vals[0] != vals[1]:
                cond = False
                while not "}" in script[mainum]:
                    mainum += 1
        if "!=" in line:
            cond = True
            if vals[0] == vals[1]:
                cond = False
                while not "}" in script[mainum]:
                    mainum += 1
        if "in" in line:
            cond = True
            if not vals[0] in vals[1]:
                cond = False
                while not "}" in script[mainum]:
                    mainum += 1
        if "!i" in line:
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
                    

    if "file.open" in line:
        vals = []
        getval()
        if len(vals) == 1:
            os.system(f"open {vals[0]}")
        else:
            err(7)
                
    if "file.read" in line:
        literal = True
        getval()
        if len(vals) == 2:
            if vals[1] in var:
                var[var.index(vals[1])+1] = open(vals[0], "r+").read()
            else:
                err(0)
        else:
            err(7)

    if "file.addln" in line:
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

    if "add" in line:
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

    if "file.create" in line:
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

    if "goto" in line:
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

    if "time.dlyuntl" in line:
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

    if "file.delete(" in line:
        getval()
        if not os.path.exists(vals[0]):
            err(10)
        else:
            os.remove(vals[0])

    if "func." in line:
        numone = line.index(".")
        val = [""]
        if "(" in line:
            while not line[numone+1] == "(":
                numone += 1
                val[0] = f"{val[0]}{line[numone]}"
            if f"func {val[0]}"+"{\n" in script:
                exval = script.index(f"func {val[0]}"+"{\n")
                while not "}" in script[exval+1]:
                    exval += 1
                    script.insert(mainum, script[exval])
            else:
                print(script)
                err(8)
        else:
            err(12)

    if "func " in line:
        while not "}" in script[mainum-1]:
            mainum += 1
    '''
    if "complete(" in line:
        literal = True
        getval()
        if "|" == line[line.index("(")]:

    Finish Later.
    '''

    if "wp.harvest(" in line:
        getval()
        literal = True
        getval()
        vals[1] = vals[3]
        if vals[1] in var:
            if not var[var.index(vals[1])+2] == "int":
                if len(vals) == 4:
                    os.system(f"curl {vals[0]} > /Users/{getpass.getuser()}/Desktop/Reverie-Programming-Language-main/main/Assetlist/cmdobj.txt")
                    var[var.index(vals[1])+1] = cmdobj.read()
                    os.system(f"echo empty > /Users/{getpass.getuser()}/Desktop/Reverie-Programming-Language-main/main/Assetlist/cmdobj.txt")
                else:
                    err(7)
            else:
                err(13)
        else:
            err(0)
        
    vals = []
    val = []
time.sleep(1)
