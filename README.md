# Welcome to the Auto-Responder!
## This is a small python-ahk script that I made which autoresponds to messages.
## Modules Required: [AHK](https://www.autohotkey.com/) and [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
It's designed for discord but might work with other apps.

Run the ahk file to start.

Simply press `Alt + F7` to add a response.
It will prompt you for a trigger and then a response.
You cannot use multiple words for the trigger, but you can with the response. (I am working on fixing this)
Then hover over the message and press `F7`.

If you want to delete responses, then press `Shift + F7` and enter the trigger of the response that you want to delete.

You can also view the .json file in your default editor using `Alt + Shift + F7`

NOTE: Putting `autoresponder.ahk` in `shell:startup` may not work.

I'm not sure why this happens, but click [here](https://gist.github.com/prokenz101/82c25bffde8ecdb992403f610ded5e0b) if you want a bat file which auto-runs the ahk.

Just put that bat file in in `shell:startup` and it should work.

Also another note: **All of this only works on Windows.**

I might work on a linux/mac version later on, but its not one of my priorities right now.

Report bugs [here](https://github.com/prokenz101/auto-responder/issues).
