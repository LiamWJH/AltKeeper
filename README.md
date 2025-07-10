# AltKeeper
Alt Keeper a git like *version control* still in work

# Introduction

Alt-Keeper is a program written in python that handles version controls and more, it has the git equvialant features that resembles,
 - commit
 - branch
 - switch
 - commit
 - init
 - and _ETC_
it is designed for the simplicity of use and hack-able features

# IMPORTANRT
If you want use the Altkeeper globally system wide _(Which i *Strongly* recommend)_ follow these steps
1. find the system enviornments on your computer(Search in search bar cmd prompt whatever)
2. make a folder in the C:\ named whatever you want (e.g.) Altkeeper and place the exe there
3. in the system variables in the path section add the path to to the folder where you have placed the Altkeeper1.x.x.exe
4. GOODY NOW IT WORKS!

# Basic Use

**--init**
this is similar to the git feature: _git init_, it intializes the folders where all your versions will be kept, and data and more,it generates a default of the _main_ branch which has all the content of the user's orginal files.
>*!* I do not recommend changing files directly in this folder. *!*

**--uninit**
this flag is the opposite of the *--init* flag, it deletes the folder that contains all the other _alternatives_
>*!* There will be a user affirmation prompt, after that there is no restorage. *!*

**--makealt**
this flag is the feature equivalant to the git feature: _git branch (BranchName)_, it makes a _alternative_ that can store versions and more about it.
>*!* This will automatically copy all the files from your current alternatives and change the _current alternative_ *!*

**--switchalt**
this flag switches the _alternative_ your on to the name given by you, it is also the equivalant of the git command: _git switch (BranchName)_
>*!* auto saving for _alternatives_ are done by default when changing the _alternative_ your on *!*

**--desc**
this flag adds or replaces the _description_ for the _alternative_, the _description_ can be used to know the use or agenda of the _alternative_ you are using
>*!* the _description_ can be seen using the *--showdesc*

**--showdesc**
this flag literally shows the _description_ for the _alternative_
>*!* this shows the description for the _alternative_ YOU ARE ON

**deletealt**
this flag deletes the _alternative_ you are on
>*!* be careful when deleting _alts_! *!*

**update**
this flag updates the content of your _alternative_ that your on
>*!* also be careful when updating the _alternative_! *!*

**alts**
shows the list of _alternatives_
>*!* Nothing to fear here xD *!*

# Terms

_alternative_: the other version of what it origins from.

_description_: a short paragraph that tells what you are doing for the _alternative_

_main_: a _alternative_ name that is the base of all version
