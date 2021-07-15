from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from userbot import bot

async def force_send_message(event, text, forward=False, chat=None):
    cHat = chat if chat else event.chat_id
    if not forward:
        try:
            e = await event.client.send_message(
                cHat,
                text
            )
        except YouBlockedUserError:
            await event.client(UnblockRequest(cHat)) 
            e = await event.client.send_message(
                cHat,
                text
            )
    else:
        try:
            e = await event.client.forward_messages(cHat, text)
            e = await e
        except YouBlockedUserError:
            await event.client(UnblockRequest(cHat)) 
            e = await event.client.forward_messages(cHat, text)
            e = await e
    return e

