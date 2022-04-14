import getpass
import os
import platform
import time
	
path = f"/Users/{getpass.getuser()}/Desktop/"
if platform.system() == "darwin":
    print("Reverie is now ready! Thank you for downloading. More can be found here: https://github.com/GitbyteMaster/Reverie-Programming-Language/")
else:
    print("Now downloading.. Please wait.")
    if "Reverie-Lang.zip" in os.listdir(path):
        if not "revfixed" in os.listdir(path):
            print("Creating directories..")
            os.rename(f"{path}Reverie-Lang",f"{path}revfixed")
            os.mkdir(f"{path}Reverie-Lang")
	    os.mkdir(f"{path}Reverie-Lang/struct")
            print("Creating files..")
            mfile = open(f"{path}Reverie-Lang/Reverie 0.1.3.1.py","w+")
            sfile = open(f"{path}/revfixed/Reverie 0.1.3.1.py","r")
            mfile.write(sfile.read())
            os.mkdir(f"{path}Reverie-Lang/Assetlist")
            sfile = open(f"{path}/revfixed/Assetlist/error.txt","r")
            mfile = open(f"{path}/Reverie-Lang/Assetlist/error.txt","w+")
            mfile.write(sfile.read())
            print("Reverie is now ready! Thank you for downloading. More can be found here: https://github.com/GitbyteMaster/Reverie-Programming-Language/")
        else:
            print("Reverie is already built!")
    else:
        print("Please extract \'Reverie.zip\'")
time.sleep(1)
