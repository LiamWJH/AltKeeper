###############
#	Imports
###############
import argparse
import os
import shutil



#####################
#           argparse
#####################
argparser = argparse.ArgumentParser()
argparser.add_argument("--init", action = "store_true")
argparser.add_argument("--uninit", action = "store_true")
argparser.add_argument("--makealt", type=str, default=None)
argparser.add_argument("--switchalt", type=str, default=None)
argparser.add_argument("--deletealt", default = None)
argparser.add_argument("--update", type=str, default=None)


args = argparser.parse_args()

#archived
#print(f"Passed in arguments: , {args.initsetup} ,{args.makealt} ,{args.switchalt} ,{args.deletealt} ,{args.update}")

###############
#	Error handle
###############
errorlogs = {}

class Error:
    def __init__(self, error, details):
        self.error = error
        self.errordetail = details
    def stateandstore(self):
        self.errorlog()
        self.storeerror()
    def errorlog(self):
        print("ERROR: " + "'" + self.error + "': "+ self.errordetail)
    def storeerror(self):
        global errorlogs
        errorlogs[f"{self.error}:{len(errorlogs)+1}"] = self.errordetail
    def graberror(self, option):
        global errorlogs

        if option == "ALL":
            for log in errorlogs:
                print("ERROR: ", log)
        else:
            try:
                print(list(errorlogs)[int(option)])
            except IndexError as IE:
                _e_IE = Error("IndexError", "The index user has given is not in the errorlog")
                _e_IE.stateandstore()

###############
#	File management
###############
class Filemanager:
    def __init__(self, projectname):
        self.projectname = projectname

    def initAK(self):
        if not os.path.exists(f"{self.projectname}_AK"):
            os.mkdir(f"{self.projectname}_AK")
        else:
            _e_FEE = Error("File Exist Error", "The folder that user has tried to init alt keeper already exists!")
            _e_FEE.stateandstore()

    def makealt(self, alternativename):

        cwd = os.getcwd()
        path = os.path.join(cwd, f"{self.projectname}_AK", alternativename)

        if os.path.exists(path):
            _e_FEE = Error("Folder Exists Error", "The folder that user has tried to make a alt already exists!")
            _e_FEE.stateandstore()
        else:
            os.mkdir(path)

            self.updatealt(alternativename)
    
    def updatealt(self, altname):
        path = os.path.join(os.getcwd(), f"{self.projectname}_AK", altname)
        for file in os.listdir(os.getcwd()):
            filepath = os.path.join(os.getcwd(), file)

            if os.path.isfile(filepath):
                shutil.copy(filepath, path)

    def switchalt(self, altname):
        path = os.path.join(os.getcwd())
        for file in os.listdir(os.path.join(os.getcwd(), f"{self.projectname}_AK", altname)):
            filepath = os.path.join(os.getcwd(), f"{self.projectname}_AK", altname, file)

            if os.path.isfile(filepath):
                shutil.copy(filepath, path)

    def deletealt(self, altname):
        if not altname == "main":
            path = os.path.join(os.getcwd(), f"{self.projectname}_AK", altname)
            shutil.rmtree(path)
        else:
            _e_DME = Error("Delete Main Error", "User tried to delete main alt!")
            _e_DME.stateandstore()

    def uninit(self):
        if input("Are you sure?:[Y/N]").lower() == "y":
            shutil.rmtree(os.path.join(os.getcwd(), f"{self.projectname}_AK"))
        else:
            pass

###############
#	Main
###############

filemanager = Filemanager(os.path.basename(os.getcwd()))

if args.init == True:
    filemanager.initAK()
    filemanager.makealt("main")

if args.uninit == True:
    filemanager.uninit()

if args.makealt != None:
    filemanager.makealt(args.makealt)

if args.update != None:
    filemanager.updatealt(args.update)

if args.switchalt != None:
    filemanager.switchalt(args.switchalt)

if args.deletealt != None:
    filemanager.deletealt(args.deletealt)