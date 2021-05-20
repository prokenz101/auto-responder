from sys import argv
from pyautogui import typewrite
import json

if argv[1] == "CreatingResponse":
    with open("tandr.json", "r") as outfile:
        keysandvalues = json.loads(outfile.read())
    keysandvalues[argv[2]] = argv[3:]
    with open("tandr.json", "w") as outfile:
        json.dump(keysandvalues, outfile)

elif argv[1] == "DeleteResponse":
    with open("tandr.json", "r") as outfile:
        keysandvalues = json.loads(outfile.read())
        keysandvalues.pop(argv[2]) 

    with open("tandr.json", "w") as outfile:
        json.dump(keysandvalues, outfile)
    
    print(f'Response successfully deleted!')

elif argv[1] == "Use":
    with open("tandr.json", "r") as outfile:
        keysandvalues = json.loads(outfile.read())
    data = " ".join(argv[2:])
    for i in keysandvalues:
        if i in data.lower():
            typewrite(keysandvalues[i])

input()