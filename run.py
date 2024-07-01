import os,platform
os.system('git pull')
os.system("clear")
print('\033[92;1m WELCOME TO CLONING TOOL')
fbd=platform.architecture()[0]
if fbd=="32bit":
    __import__("run2")
elif fbd=="64bit":
    __import__("run2")