from .heroku import heroku_var, app
from userbot.cmdhelp import CmdHelp
from userbot.events import register
from userbot import SEVGILI
import heroku3

@register(pattern='^.adddarling$', replyneeded=True)
async def adddarling(e):
    global SEVGILI
    reply = await e.get_reply_message()
    reply_user = await e.client.get_entity(reply.from_id)
    SEVGILI = int(reply_user.id)
    await e.edit('`Sevgiliniz eklendi.. ❤️\nGlobal değerlere işlenmesi için lütfen 2 dakika bekleyin!`')
    if heroku_var and app:
        heroku_var["SEVGILI"] = reply_user.id
    return True

@register(pattern='^.rmdarling$')
async def adddarling(e):
    global SEVGILI
    SEVGILI = None
    await e.edit('`Sevgiliniz Silindi💔`')
    if heroku_var and app:
        del heroku_var["SEVGILI"]
    return True



@register(sevgili=True,pattern='^!darling')
async def darlingonly(e):
    await e.reply('✨ **Love u!**')


a = CmdHelp('darling')
a.add_command('adddarling',None,'Yanıt verdiğiniz kişiyi botta sevgiliniz yapar').add_command('rmdarling',None,'Bottaki sevgilinizi siler').add()
