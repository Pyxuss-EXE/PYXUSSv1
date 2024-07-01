import os
import platform
import time
import sys
os.system('pkg install espeak -y')
try:
    import requests
except:
    os.system("pip uninstall requests -y; pip install requests")

print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mChecking For Update...')
os.system('git pull --quiet 2>/dev/null')
ranaxd = platform.architecture()[0]
if ranaxd == '64bit':
    print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Device is 64bit')
    import run2.cpython_311 as run2
elif ranaxd == '32bit':
    print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Device is 32bit')
    import run2.cpython_311 as run2
