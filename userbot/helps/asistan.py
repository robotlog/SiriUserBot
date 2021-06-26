from userbot import SEVGILI, SUDO_ID
from userbot.main import idim
async def edit_or_reply(event, text):
    m = event
    try:
        THISSUDO = SUDO_ID or [0]
        THISSEW = SEVGILI or [0]
        if event.from_id in THISSUDO or event.from_id in THISSEW:
            reply_to = await event.get_reply_message()
            if reply_to:
                m = await reply_to.reply(text)
                return m
            m = await event.reply(text)
            return m 
        await event.edit(text)
        return m
    except:
        await event.edit(text)
        return m


async def bana_mi_diyo(ups):
    if ups.is_reply:
        reply = await ups.get_reply_message()
        reply_user = await ups.client.get_entity(reply.from_id)
        ren = reply_user.id
        if ren == idim:
            return True
        return False
    return False

