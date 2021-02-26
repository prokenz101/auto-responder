from pyautogui import typewrite
import sys

data = " ".join(sys.argv[1:]).lower()

aternosissues = {
    'verify username': "!article verify username",
    'invalid session': "!article verify username",
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
    'lag': r"check https://www.spigotmc.org/threads/guide-server-optimization%E2%9A%A1.283181/",
    'essentialsx': "With over 130 commands, EssentialsX provides one of the most comprehensive feature sets out there, providing teleportation, moderation tools, gameplay enhancements and more. Just want the homes and warps? Great. Need a sign shop? Done. Want complex and rich kits with enchantments, custom books and lore? Sorted. Whether you're a small group of friends or a huge server with hundreds of players, we've got the basics covered.",
    'hello': "hello",
    'hi': "hello",
    'hey': "hello",
    'add datapacks': "!article datapacks",
    'install datapacks': "!article datapacks",
    'show coordinates': "!article coordinates",
    'show coords': "!article coordinates",
    'dynip': "!article connect",
    'suggest': '!article suggest',
    'ask a question': "Get support. Please don't ask to ask: JUST ASK.",
    'ask question': "Get support. Please don't ask to ask: JUST ASK.",
    'account suspended': 'yes, that suspension is permanent and it is because you used an afkbot or something',
    'help': "**We can't help you if you don't state your problem.**",
    'more ram': 'you cant do it in aternos but there is a different server hosting service called exaroton which is paid and has better ram etc.'
}
for i in aternosissues:
    if i in data.lower():
        typewrite(aternosissues[i] + "\n")