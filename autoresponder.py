from pyautogui import typewrite
from sys import argv

data = " ".join(argv[1:]).lower()

keysandvalues = {
}

for i in keysandvalues:
    if i in data.lower():
        typewrite(keysandvalues[i], interval=0)
