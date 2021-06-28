"""
               SİRİUSERBOT  -  BERCE
"""
import os
from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from userbot import BOTLOG_CHATID

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("botfather")

# ████████████████████████████████ #


@register(pattern="^.newbot ?(.*)")
async def newbot(event):
    if event.pattern_match.group(1):
        text, username= event.pattern_match.group(1).split()
        
    else:
        await event.edit(LANG["ERROR"])
        return

    async with event.client.conversation("@BotFather") as conv:
        try:
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            if BOTLOG_CHATID:
                await event.client.forward_messages(BOTLOG_CHATID, audio)
                await event.edit('✅ Send to Botlog')
            else:
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            if BOTLOG_CHATID:
                await event.client.forward_messages(BOTLOG_CHATID, audio)
                await event.edit('✅ Send to Botlog')
            else:
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()



add_ = CmdHelp('botyap')
add_.add_command("newbot", "<bot_name> <bot_username>", "Yeni Bot Oluşturun").add()
