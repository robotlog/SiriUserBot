from userbot import MYID

async def bana_mi_diyo(ups):
    if ups.is_reply:
        reply = await ups.get_reply_message()
        reply_user = await ups.client.get_entity(reply.from_id)
        ren = reply_user.id
        if ren == MYID:
            return True
        return False
    return False

