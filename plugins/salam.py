from platform import uname

from userbot import ALIVE_NAME, CMD_HELP

from userbot.events import register

# ================= CONSTANT =================

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node

# ============================================

@register(outgoing=True, pattern='^P(?: |$)(.*)')

async def typewriter(typew):

    typew.pattern_match.group(1)

    await typew.edit("𝐀𝐬𝐬𝐚𝐥𝐚𝐦𝐮'𝐚𝐥𝐚𝐢𝐤𝐮𝐦...")

@register(outgoing=True, pattern='^.atg(?: |$)(.*)')

async def typewriter(typew):

    typew.pattern_match.group(1)

    await typew.edit("𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇.... 𝐆𝐎𝐁𝐋𝐎𝐊𝐊𝐊𝐊𝐊!!!!")

@register(outgoing=True, pattern='^L(?: |$)(.*)')

async def typewriter(typew):

    typew.pattern_match.group(1)

    await typew.edit("𝐖𝐚'𝐚𝐥𝐚𝐢𝐤𝐮𝐦𝐬𝐚𝐥𝐚𝐦...")

@register(outgoing=True, pattern='^.ast(?: |$)(.*)')

async def typewriter(typew):

    typew.pattern_match.group(1)

    await typew.edit("𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇......")

@register(outgoing=True, pattern='^K(?: |$)(.*)')

async def typewriter(typew):

    typew.pattern_match.group(1)

    await typew.edit("**𝐍𝐆𝐎𝐍𝐓𝐎𝐋𝐋𝐋𝐋𝐋𝐋**")

@register(outgoing=True, pattern='^N(?: |$)(.*)')

async def typewriter(typew):

    typew.pattern_match.group(1)

    await typew.edit("**𝐍𝐆𝐄𝐍𝐓𝐎𝐎𝐎𝐎𝐎𝐎𝐎𝐓𝐓𝐓𝐓𝐓𝐓𝐓𝐓𝐓𝐓𝐓𝐓**")

@register(outgoing=True, pattern='^B(?: |$)(.*)')

async def typewriter(typew):

    typew.pattern_match.group(1)

    await typew.edit("**𝐁𝐀𝐂𝐎𝐓 𝐃𝐀𝐇 𝐋𝐔, 
