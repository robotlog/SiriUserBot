from userbot import MYID, SEVGILI, SUDO_ID

async def edit_or_reply(event, text):
    try:
        THISSUDO = SUDO_ID or [0]
        THISSEW = SEVGILI or [0]
        if event.from_id in THISSUDO or event.from_id in THISSEW:
            reply_to = await event.get_reply_message()
            if reply_to:
                return await reply_to.reply(text)
            return await event.reply(text)
        return await event.edit(text)
    except:
        return await event.edit(text)


async def bana_mi_diyo(ups):
    if ups.is_reply:
        reply = await ups.get_reply_message()
        reply_user = await ups.client.get_entity(reply.from_id)
        ren = reply_user.id
        if ren == MYID:
            return True
        return False
    return False

