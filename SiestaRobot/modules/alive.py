import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://te.legra.ph/file/f95ebea77c1488dd21938.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Fantastic manager Bot.** \n\n"
  TEXT += "π  **I'm Working Properly** \n\n"
  TEXT += f"π  **My Master : [π°ππΈππ΄πΊ](https://t.me/DUSHMANxRONIN)** \n\n"
  TEXT += f"π  **Library Version :** `{telever}` \n\n"
  TEXT += f"π  **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"π  **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here π**"
  BUTTON = [[Button.url("Help", "https://t.me/FANTASTICFIGHTERBOT?start=help"), Button.url("Support", "https://t.me/Ronin_Fighters_FD")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
