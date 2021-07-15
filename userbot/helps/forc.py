from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from userbot import bot

async def force_send_message(event, text, chat=None):
    cHat = chat if chat else event.chat_id
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
    return e

