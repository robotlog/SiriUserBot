# Copyright (C) 2020 Yusuf Usta.
#
# Licensed under the  GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# SiriUserBot - Berceste



import asyncio
import time
from telethon.tl import functions

from userbot import CMD_HELP, ASYNC_POOL
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from .autovideo import *

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("auto")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.auto ?(.*)")
async def auto(event):
    metod = event.pattern_match.group(1).lower()
    
    if str(metod) != "isim" and str(metod) != "bio" and str(metod) != "pp":
        await event.edit(LANG['INVALID_TYPE'])
        return

    if metod in ASYNC_POOL:
        await event.edit(LANG['ALREADY'] % metod)
        return

    await event.edit(LANG['SETTING'] % metod)
    if metod == "isim":
        HM = time.strftime("%H:%M")

        await event.client(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
            last_name=LANG['NAME'] % HM
        ))

    elif metod == "bio":
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M")

        Bio = LANG['BIO'].format(tarih=DMY, saat=HM) + LANG['NICK'] 
        await event.client(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
            about=Bio
        ))

    elif str(metod) == "pp":
        FONT_FILE_TO_USE = await get_font_file(event.client, "@FontDunyasi")

        downloaded_file_name = "./userbot/eskipp.png"
        r = requests.get(AUTO_PP)
    
        with open(downloaded_file_name, 'wb') as f:
            f.write(r.content)    
        photo = "yenipp.png"

    ASYNC_POOL.append(metod)

    await event.edit(LANG['SETTED'] % metod)

    while metod in ASYNC_POOL:
        try:
            if metod == "isim":
                HM = time.strftime("%H:%M")

                await event.client(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    last_name=LANG['NAME'] % HM
                ))
            elif metod == "bio":
                DMY = time.strftime("%d.%m.%Y")
                HM = time.strftime("%H:%M")

                Bio = LANG['BIO'].format(tarih=DMY, saat=HM) + LANG['NICK'] 
                await event.client(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    about=Bio
                ))

            elif metod == 'pp':
                shutil.copy(downloaded_file_name, photo)
                current_time = datetime.now().strftime("%H:%M")
                img = Image.open(photo)
                drawn_text = ImageDraw.Draw(img)
                fnt = ImageFont.truetype(FONT_FILE_TO_USE, 70)
                size = drawn_text.multiline_textsize(current_time, font=fnt)
                drawn_text.text(((img.width - size[0]) / 2, (img.height - size[1])),
                               current_time, font=fnt, fill=(255, 255, 255))
                img.save(photo)
                file = await event.client.upload_file(photo)  # pylint:disable=E0602
                try:
                    await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                        file
                    ))
                    os.remove(photo)
                    await asyncio.sleep(60)
                except:
                    return


            await asyncio.sleep(60)
        except:
            return




async def get_font_file(client, channel_id):
    # Önce yazı tipi mesajlarını al
    font_file_message_s = await client.get_messages(
        entity=channel_id,
        filter=InputMessagesFilterDocument,
        # Bu işlem çok fazla kullanıldığında
        # "FLOOD_WAIT" yapmaya neden olabilir
        limit=None
    )
    # Yazı tipi listesinden rastgele yazı tipi al
    # https://docs.python.org/3/library/random.html#random.choice
    font_file_message = random.choice(font_file_message_s)
    # Dosya yolunu indir ve geri dön
    return await client.download_media(font_file_message)

CmdHelp('auto').add_command(
    'auto', 'isim ,pp ya da bio', 'Otomatik saate göre Değişir', '.auto isim(isminiz değil "isim" Kelimesi)'
).add()
