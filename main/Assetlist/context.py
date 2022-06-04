import getpass
class give:
    def givecontext(c):
        n = -1
        errs = []
        args = 0
        err = [""]
        ga = []
        vis = ""
        f = "none"
        if c == "system.write":
            args = 1
            errs = [0,7]
            ga = ["str/int/var"]
            f = "Displays Text"
        else:
            if c == "time.delay":
                args = 1
                errs = [0,4,7]
                f = "Pauses Program by Seconds"
            else:
                if c == "wp.harvest":
                    args = 2
                    errs = [0,7,13]
                    ga = ["str/var", "var"]
                    f = "Returns Web Data to Existing Variable"
                else:
                    if c == "file.delete":
                        args = 1
                        errs = [0, 3, 7, 10]
                        f = "Deletes Existing File"
                        ga = ["str/var"]
                        


        for x in ga:
            vis = f"{vis}[{x}],"
        print(f"{c}()\n=========\n[{args} Parameter(s) Needed:]\n=========\n{c}({vis})\n=========\n[Function:]\n{f}\n=========\n[Possible Errors:]")
        v = open(f"/Users/{getpass.getuser()}/Desktop/Reverie-Programming-Language-main/main/Assetlist/error.txt", "r+").read()
        while not n == len(v)-1:
            n += 1
            if v[n] == "\n":
                err.append("")
            err[len(err)-1] = f"{err[len(err)-1]}{v[n]}"
        for x in errs:
            print(err[x])
