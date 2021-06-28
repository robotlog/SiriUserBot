from userbot.events import register
from userbot import AUTODISPOSAL
from asyncio import sleep

@register(groups_only=True, notifyoff=True)
async def destruction(event):
    if AUTODISPOSAL > 1:
        await sleep(AUTODISPOSAL)
        await event.delete()
    return
