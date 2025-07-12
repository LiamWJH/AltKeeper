####################################
#	Imports
####################################

import argparse
import os
import shutil



####################################
#	argparse setup
####################################

argparser = argparse.ArgumentParser()
argparser.add_argument("--init", action = "store_true")
argparser.add_argument("--uninit", action = "store_true")

argparser.add_argument("--makealt", type=str, default=None)
argparser.add_argument("--switchalt", type=str, default=None)
argparser.add_argument("--deletealt", action = "store_true")
argparser.add_argument("--update", action = "store_true")
argparser.add_argument("--official", action = "store_true")

argparser.add_argument("--desc", type=str, default=None)
argparser.add_argument("--showdesc", action = "store_true")
argparser.add_argument("--alts", action = "store_true")

args = argparser.parse_args()


####################################
#	error class
####################################

class Error:
    def __init__(self, error, resolve):
        self.error = error
        self.resolve = resolve
        
    def __call__(self):
        print(f"ERR: '{self.error}' => '{self.resolve}'")
        print("")


####################################
#	Filemanager class
####################################

class Filemanager:
    def __init__(self, projectname):
        self.projectname = projectname

    def initAK(self):
        if not os.path.exists(f"{self.projectname}_AK"):
            os.mkdir(f"{self.projectname}_AK")
            
        else:
            e = Error("AK folder exists", "use --uninit or keep the folder")
            e()

    def makealt(self, alternativename):

        cwd = os.getcwd()
        path = os.path.join(cwd, f"{self.projectname}_AK", alternativename)

        if os.path.exists(path):
            e = Error("Alternative already exists", "Use the alternative or do --deletealt on the alternative wanted")
            e()
        
        else:
            os.mkdir(path)

            try:
                with open(os.path.join(os.getcwd(), f"{self.projectname}_AK", "currentbranch.txt"), "w") as f:
                    f.write(f"CurrentBranch:{os.path.basename(path)}")
                self.updatealt()
            except Exception as e:
                e = Error("Internal file loading Failed", "Do --uninit and then do --init")
                e()
                        
    
    def updatealt(self):
        try:
            with open(os.path.join(os.getcwd(), f"{self.projectname}_AK", "currentbranch.txt"), "r") as f:
                altname = f.read().split(":")[1]
            
                path = os.path.join(os.getcwd(), f"{self.projectname}_AK", altname)
            for file in os.listdir(os.getcwd()):
                filepath = os.path.join(os.getcwd(), file)

                if os.path.isfile(filepath):
                    shutil.copy(filepath, path)
            
            for file in os.listdir(path):
                if not file in os.listdir(os.getcwd()):
                    os.remove(os.path.join(path, file))
                    
        except Exception as e:
            e = Error("Internal file loading Failed", "Do --uninit and then do --init")
            e()
        
        

    def switchalt(self, altname):
        try:
            with open(os.path.join(os.getcwd(), f"{self.projectname}_AK", "currentbranch.txt"), "w") as f:
                f.write(f"CurrentBranch:{altname}")
            
            
            path = os.path.join(os.getcwd())
            for file in os.listdir(os.path.join(os.getcwd(), f"{self.projectname}_AK", altname)):
                filepath = os.path.join(os.getcwd(), f"{self.projectname}_AK", altname, file)

                if os.path.isfile(filepath):
                    shutil.copy(filepath, path)
        
        except Exception as e:
            e = Error("Internal file load error", "Do --uninit then --init")
            e()
            
    def deletealt(self):
        try:
            with open(os.path.join(os.getcwd(), f"{self.projectname}_AK", "currentbranch.txt"), "r") as f:
                altname = f.read().split(":")[1]
                
            if not altname == "main":
                path = os.path.join(os.getcwd(), f"{self.projectname}_AK", altname)
                shutil.rmtree(path)
                with open(os.path.join(os.getcwd(), f"{self.projectname}_AK", "currentbranch.txt"), "w") as f:
                    f.write(f"CurrentBranch:main")
            else:
                e = Error("User tried to delete main alt", "Do not delete the main alternative")
                e()
        except Exception as e:
            e = Error("Internal file load error","Do --uninit then --init")
            e()
            
    def uninit(self):
        if input("Are you sure?:[Y/N]").lower() == "y":
            try:
                shutil.rmtree(os.path.join(os.getcwd(), f"{self.projectname}_AK"))
            except Exception as e:
                e = Error("Alt keeper folder does not exist in this directory", "Make one by --init")
                e()
        else:
            pass
    
    def showalts(self):
        try:
            path = os.path.join(os.getcwd(), f"{self.projectname}_AK")
            for thing in os.listdir(path):
                if not os.path.isfile(os.path.join(path, thing)):
                    print("-> ", thing)
        except Exception as e:
            e = Error("Alt keeper folder does not exist in this directory", "Make one by --init")
            e()
                    
####################################
#	Main
####################################

prjNAME = os.path.basename(os.getcwd())

filemanager = Filemanager(prjNAME)

if args.init == True:
    filemanager.initAK()
    filemanager.makealt("main")
    
    with open(os.path.join(os.getcwd(), f"{prjNAME}_AK", "currentbranch.txt"), "w") as f:
        f.write(f"CurrentBranch:main")

if args.uninit == True:
    filemanager.uninit()

if args.makealt != None:
    filemanager.makealt(args.makealt)

if args.update == True:
    filemanager.updatealt()

if args.switchalt != None:
    filemanager.updatealt()
    filemanager.switchalt(args.switchalt)

if args.deletealt == True:
    filemanager.deletealt()

if args.alts == True:
    filemanager.showalts()

if args.desc != None:
    try:
        with open(os.path.join(os.getcwd(), f"{prjNAME}_AK", "currentbranch.txt"), "r") as f:
            alt = f.read().split(":")[1]
        with open(os.path.join(os.getcwd(), f"{prjNAME}_AK", alt, "description.txt"), "w") as f:
            f.write(args.desc)

            
    except Exception as e:
        e = Error("Internal file load error", "do --uninit then --init")
        e()
    
if args.showdesc == True:
    try:
        with open(os.path.join(os.getcwd(), f"{prjNAME}_AK", "currentbranch.txt"), "r") as f:
            alt = f.read().split(":")[1]
        with open(os.path.join(os.getcwd(), f"{prjNAME}_AK", alt, "description.txt"), "r") as f:
            print("->",f.read())
    except Exception as e:
        e = Error("Internal file load error", "do --uninit then --init")
        e()
        
if args.official == True:
    try:
        with open(os.path.join(os.getcwd(), f"{prjNAME}_AK", "currentbranch.txt"), "r") as f:
            alt = f.read().split(":")[1]
        
        try:
            shutil.rmtree(os.path.join(os.path.join(os.getcwd(), f"{prjNAME}_AK", "main")))
            shutil.copytree(os.path.join(os.path.join(os.getcwd(), f"{prjNAME}_AK", alt)), os.path.join(os.path.join(os.getcwd(), f"{prjNAME}_AK", "main")))
            filemanager.switchalt("main")
        except Exception as e:
            e = Error("Main alternative does not exist", "Make main again by doing --makealt main or do --uninit then --init")
            e()
            
    except Exception as e:
        e = Error("Internal file load error", "do --uninit then --init")
        e()
        