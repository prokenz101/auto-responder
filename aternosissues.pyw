from pyautogui import typewrite
import sys

data = " ".join(sys.argv[1:]).lower()

aternosissues = {
    'verify username': "!article verify username",
    'invalid session': "!article verify username",
    'cracked': "!article cracked",
    'backup': "!article backup",
    'invalid token': "!article verify username",
    'custom plugin': "!article ftp",
    'my own plugin': "!article ftp",
    'custom mod': "!article ftp",
    'my own mod': "!article ftp",
    'forcibly closed': "!article forcibly closed",
    'i lost my password': "!article lost",
    'forgot password': "!article lost",
    'cant remember password': "!article lost",
    'tlauncher': "!article tlauncher",
    'geyser': "!article geyser",
    'crash': "share your log",
    'lag': r"check https://www.spigotmc.org/threads/guide-server-optimization%E2%9A%A1.283181/",
    'took too long to start': "you have too many mods, try removing some",
    'essentialsx': "With over 130 commands, EssentialsX provides one of the most comprehensive feature sets out there, providing teleportation, moderation tools, gameplay enhancements and more. Just want the homes and warps? Great. Need a sign shop? Done. Want complex and rich kits with enchantments, custom books and lore? Sorted. Whether you're a small group of friends or a huge server with hundreds of players, we've got the basics covered. To visit the wiki, go to https://essentialsx.net/wiki/Home.html.",
    'texture': "!video resourcepacks",
    'hello': "hello",
    'add datapacks': "!article datapacks",
    'install datapacks': "!article datapacks",
    'show coordinates': "!article coordinates",
    'show coords': "!article coordinates",
    'coordinates': "!article coodinates",
    'dynip': "!article connect",
    'superflat': "!article superflat",
    'skyfactory 4': r"check https://aternos.org/software/v/modpacks/curse_skyfactory4 and https://www.curseforge.com/minecraft/modpacks/skyfactory-4 to install it on the client",
    'sky factory 4': r"check https://aternos.org/software/v/modpacks/curse_skyfactory4 and https://www.curseforge.com/minecraft/modpacks/skyfactory-4 to install it on the client",
    "Biomes O' Plenty": "!article o",
    'biomes o plenty': "!article o",
    'suggest': '!article suggest',
    'mods': "!video mods",
    'ask a question': "Get support. Please don't ask to ask: JUST ASK.",
    'ask question': "Get support. Please don't ask to ask: JUST ASK.",
    'account suspended': 'yes, that suspension is permanent and it is because you used an afkbot or something',
    'help': "**We can't help you if you don't ask a question or state your problem.**",
    'more ram': 'you cant do it in aternos but there is a different server hosting service called exaroton which is paid and has better ram etc.',
    'increase ram': 'you cant do it in aternos but there is a different server hosting service called exaroton which is paid and has better ram etc.',
    'increase the ram': 'you cant do it in aternos but there is a different server hosting service called exaroton which is paid and has better ram etc.',
    'rule 1 ': "1. Be nice and respectful to everybody, this is not a place for hatred, insults etc.",
    'rule 2': "2. Don’t spam, one message is enough.",
    'rule 3': "3. Only tag somebody or a group if it’s really necessary.",
    'rule 4': "4. Listen to all team members and moderators, they can ban you and they will.",
    'rule 5': "5. Ask any support related questions only in the #support channel.",
    'rule 6': "6. Wait patiently for an answer and don’t tag anybody.",
    'rule 7': "7. Don’t repeat your question unless you are asked for it.",
    'rule 8': "8. Don’t send direct messages to team members and moderators unless they ask you to do that. Please note: You don’t get a guaranteed response here, better use https://support.aternos.org/ or email support@aternos.org for that.",
    'rule 9': "9. You are only allowed to advertise Aternos servers and related websites/Discord servers.",
    'rule 10': "10. Only post your server IP/link into the #servers channel.",
    'rule 11': "11. Your message in the #servers channel has to include a valid Aternos server IP.",
    'rule 12': "12. Your server has to be online (or at least starting) to advertise it.",
    'rule 13': "13. You are not allowed to post your server IP more than once per day.",
    'rule 14': "14. Advertising in direct messages without explicit consent is forbidden.",
    'rule 15': "15. Asking to join your server, to check the #servers channel etc. counts as advertising.",
    'rule 16': "16. Talking about the  q u e u e   l e n g t h  or asking any questions related to the  q u e u e   l e n g t h  is not allowed. You can read our support article about this and that's all the information we can give you on that: https://support.aternos.org/hc/en-us/articles/360026950812",
    'fuck': '**Your message contains words/phrases which are not allowed here!**',
    'shit': '**Your message contains words/phrases which are not allowed here!**',
    'stfu': "**Your message contains words/phrases which are not allowed here!**",
    'gay': "**Your message contains words/phrases which are not allowed here!**",
    'ㅤ': "hangul filler?",
    'all commands': r"https://minecraft.gamepedia.com/Commands",
    'cheat': "!article op",
    'forever': r"Running your server forever is not possible because Aternos is a 100% free service. They only have limited resources, and they want to make sure that these resources are used by active players. Trying to circumvent that will result in your server being deleted.",
    '24/7': r"Running your server forever is not possible because Aternos is a 100% free service. They only have limited resources, and they want to make sure that these resources are used by active players. Trying to circumvent that will result in your server being deleted.",
    'unban': "!article unban",
    'thank': "np",
    'can i ask': "Get support. Please don't asv to ask: JUST ASK",
    'cant join': r'"could you be more specific, like "I cant join because its saying {some error idk}"',
    "can't join": r'"could you be more specific, like "I cant join because its saying {some error idk}"',
    'cannot join': r'"could you be more specific, like "I cant join because its saying {some error idk}"',
    'stopping': "!article stop countdown",
    'seed': "`/seed`",
    'more than 1 server': "https://www.youtube.com/watch?v=Q5oB8k_lyk8&feature=youtu.be",
    '2 servers': "https://www.youtube.com/watch?v=Q5oB8k_lyk8&feature=youtu.be",
    'multiple servers': "https://www.youtube.com/watch?v=Q5oB8k_lyk8&feature=youtu.be",
    'kicked': "what does it say when you get kicked?",
    'login plugin': r"try this https://aternos.org/addons/a/spigot/19362",
    'discordsrv': r"https://www.youtube.com/watch?v=xKETqmm3yHY",
    'luckperms': "check https://aternos.org/addons/a/spigot/28140 and https://luckperms.net/wiki/Home if you want to know how to use it",
    'permission plugin': "check this, its called luckperms https://aternos.org/addons/a/spigot/28140",
    'for maintenance': "A common error player may face while trying to connect to Minecraft is that the game's authentication servers are down at the moment. This mostly indicates that the servers are offline at the moment due to maintenance. Usually, the only thing you can do is to  w a i t  for the servers to go back online.",
    'dynip': r"Try the DynIP, The DynIP is an alternative IP address for your server that helps you to directly connect to your server. Unlike the regular IP, the DynIP changes every time you start your server. To view the DynIP, click on the 'Connect' button (i icon when using bedrock or pocketmine) on the server page while your server is online. Copy it and use enter it as the ip to connect to your server.",
    'dyn-ip': r"Try the DynIP, The DynIP is an alternative IP address for your server that helps you to directly connect to your server. Unlike the regular IP, the DynIP changes every time you start your server. To view the DynIP, click on the 'Connect' button (i icon when using bedrock or pocketmine) on the server page while your server is online. Copy it and use enter it as the ip to connect to your server.",
    'all caps': "Please be more respectful, and avoid talking in all caps." 
}
for i in aternosissues:
    if i in data.lower():
        typewrite(aternosissues[i] + "\n")