from typing import final
from pyautogui import typewrite
from sys import argv

data = " ".join(argv[1:]).lower()

aternosissues = {
    'verify username': r"!article verify username",
    'invalid session': r"!article verify username",
    'cracked': r"!article cracked",
    'backup': r"!article backup",
    'invalid token': r"!article verify username",
    'custom plugin': r"!article ftp",
    'my own plugin': r"!article ftp",
    'custom mod': r"!article ftp",
    'my own mod': r"!article ftp",
    'forcibly closed': r"!article forcibly closed",
    'i lost my password': r"!article lost",
    'forgot password': r"!article lost",
    'cant remember password': r"!article lost",
    'tlauncher': r"!article tlauncher",
    'geyser': r"!article geyser",
    'crash': r"share your log",
    'lag': r"read this https://bluewyechache.gitbook.io/aternos/articles/lag",
    'took too long to start': r"you have too many mods, try removing some",
    'texture': r"!video resourcepacks",
    'hello': r"hello",
    'add datapacks': r"!article datapacks",
    'install datapacks': r"!article datapacks",
    'show coordinates': r"!article coordinates",
    'show coords': r"!article coordinates",
    'coordinates': r"!article coodinates",
    'dynip': r"!article connect",
    'superflat': r"!article superflat",
    'skyfactory 4': r"https://aternos.org/software/v/modpacks/curse_skyfactory4 and https://www.curseforge.com/minecraft/modpacks/skyfactory-4 to install it on the client",
    'sky factory 4': r"https://aternos.org/software/v/modpacks/curse_skyfactory4 and https://www.curseforge.com/minecraft/modpacks/skyfactory-4 to install it on the client",
    'biomes o plenty': r"!article o",
    'suggest': r'!article suggest',
    'mods': r"!video mods",
    'more ram': r'you cant do it in aternos but there is a different server hosting service called exaroton which is paid and has better ram etc.',
    'increase ram': r'you cant do it in aternos but there is a different server hosting service called exaroton which is paid and has better ram etc.',
    'increase the ram': r'you cant do it in aternos but there is a different server hosting service called exaroton which is paid and has better ram etc.',
    'all commands': r"https://minecraft.gamepedia.com/Commands",
    'cheat': r"!article op",
    'unban': r"!article unban",
    'cant join': r'"could you be more specific, like "I cant join because its saying {some error idk}"',
    "can't join": r'"could you be more specific, like "I cant join because its saying {some error idk}"',
    'cannot join': r'"could you be more specific, like "I cant join because its saying {some error idk}"',
    'stopping': r"!article stop countdown",
    'more than 1 server': r"https://www.youtube.com/watch?v=Q5oB8k_lyk8&feature=youtu.be",
    '2 servers': r"https://www.youtube.com/watch?v=Q5oB8k_lyk8&feature=youtu.be",
    'multiple servers': r"https://www.youtube.com/watch?v=Q5oB8k_lyk8&feature=youtu.be",
    'kicked': r"what does it say when you get kicked?",
    'login plugin': r"https://aternos.org/addons/a/spigot/19362",
    'discordsrv': r"https://www.youtube.com/watch?v=xKETqmm3yHY",
    'luckperms': r"https://aternos.org/addons/a/spigot/28140 and https://luckperms.net/wiki/Home if you want to know how to use it",
    'permission plugin': r"https://aternos.org/addons/a/spigot/28140",
    'modpacks': r"https://aternos.org/software/modpacks/",
    'dns': r"https://developers.google.com/speed/public-dns/docs/using",
    'dynip': r"https://www.youtube.com/watch?v=yrxSzL0NiwY",
    'geyser': r"https://www.youtube.com/watch?v=J-ixVe840M4",
    'schem': r"https://www.youtube.com/watch?v=w_anhj0ZTPI",
    'skin': r"https://www.youtube.com/watch?v=dlFJxI6qX-E",
    'move': r"https://support.exaroton.com/hc/en-us/articles/360017142438-Move-your-Aternos-server-to-exaroton",
    'hardcore': r"go to https://aternos.org/worlds, then press the green button called `Generate` **NOTE: This will delete your current world so make a backup** and at the very bottom there should be a setting called `Hardcore` like this https://photos.app.goo.gl/uKeUPMeWmQSVTa7F7",
    'hack': r"Hacking cracked servers: People often come into the discord server or forums and say their servers were hacked. However, these are just as often cracked servers. Cracked servers often get 'hacked' through players suddenly gaining OP. Cracked servers do not actually get 'hacked'. Cracked servers also have more security risks, one of these being the possibility that anyone can log in using any name, and the playerdata bound to that name would be given to anyone using that specific name, making it really easy to get OP that way. Always make sure to use login security plugins like AuthMe Reloaded and/or to use the whitelist. (Reminder that the whitelist may not always work as people can use this same loophole to cheat the whitelist.) Other servers that are not cracked have barely any chance of getting hacked, as the only form for that would be using hack clients like wurst or aristois which can be countered using anticheat plugins, or simply getting staff.",
    'seed': r"go to https://aternos.org/worlds then click the generate button and type in the seed (NOTE: This will delete your world) after you did that press Generate and start the server",
    'protect': r"worldguard download link: https://aternos.org/addons/a/bukkit/worldguard (NOTE: make sure you get the required dependancies) heres the wiki https://worldguard.enginehub.org/en/latest/",
    'worldguard': r"worldguard download link: https://aternos.org/addons/a/bukkit/worldguard (NOTE: make sure you get the required dependancies) heres the wiki https://worldguard.enginehub.org/en/latest/",
    'worldedit': r"download link https://aternos.org/addons/a/bukkit/worldedit use `//` to do commands and heres a wiki https://minecraft-worldedit.fandom.com/wiki/Worldedit_Commands",
    'claim': r"https://aternos.org/addons/a/bukkit/grief-prevention and this https://dev.bukkit.org/projects/grief-prevention",
    'griefprevention': r"https://aternos.org/addons/a/bukkit/grief-prevention and this https://dev.bukkit.org/projects/grief-prevention"
}
    
finalresult = data.format(**aternosissues)
typewrite(finalresult, interval=0.02)