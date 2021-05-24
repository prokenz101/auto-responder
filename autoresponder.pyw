from pyautogui import typewrite
from sys import argv
from time import sleep
from json.decoder import JSONDecodeError
from json import dumps, loads
from pathlib import Path


def readjson():
    file = Path('tandr.json')
    file.touch(exist_ok=True)
    keysandvalues = {}
    try:
        keysandvalues = loads(file.read_text())
    except JSONDecodeError:
        file.write_text('{}')
    return keysandvalues


def writejson(data):
    file = Path('tandr.json')
    file.touch(exist_ok=True)
    file.write_text(dumps(data, indent=2))


if argv[1] == "CreatingResponse":
    keysandvalues = readjson()
    n = argv.index("|") # Index of the seperator
    trigger = " ".join(argv[2:n])
    response = " ".join(argv[n+1:])
    keysandvalues[trigger] = response
    writejson(keysandvalues)

if argv[1] == "DeleteResponse":
    keysandvalues = readjson()
    keysandvalues.pop(" ".join(argv[2]))
    writejson(keysandvalues)

elif argv[1] == "Use":
    keysandvalues = readjson()
    data = " ".join(argv[2:])
    for i in keysandvalues:
        if i in data.lower():
            typewrite(keysandvalues[i])