# Ported by Fariz (Flicks-Userbot)
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot, CMD_HELP, CMD_HANDLER as i
from userbot.utils import flicks_cmd


@flicks_cmd(pattern="truth(?: |$)(.*)")
async def _(event):
    await event.edit("Mengirim pesan truth...")
    async with bot.conversation("@truthordares_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1335899453)
            )
            await conv.send_message("/truth")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("Harap unblock `@truthordares_bot` dan coba lagi")
            return
        await event.edit(f"**Pesan truth**\n\n{response.message.message}")


@flicks_cmd(pattern="dare(?: |$)(.*)")
async def _(event):
    await event.edit("Mengirim pesan dare...")
    async with bot.conversation("@truthordares_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1335899453)
            )
            await conv.send_message("/dare")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("Harap unblock `@truthordares_bot` dan coba lagi")
            return
        await event.edit(f"**Pesan dare**\n\n{response.message.message}")


@flicks_cmd(pattern="spill(?: |$)(.*)")
async def _(event):
    await event.edit("Mengirim pesan spill...")
    async with bot.conversation("@Spillgame_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1361222893)
            )
            await conv.send_message("/spill")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("Harap unblock `@Spillgame_bot` dan coba lagi")
            return
        await event.edit(f"**Pesan spill**\n\n{response.message.message}")


CMD_HELP.update(
    {
        "truth_dare": f"** Plugin :** truth_dare\
        \n\n  •  Perintah : `{i}truth`\
        \n  •  Function : Untuk mengirim pesan truth\
        \n\n  •  Perintah : `{i}dare`\
        \n  •  Function : Untuk mengirim pesan dare\
        \n\n  •  Perintah : `{i}spill`\
        \n  •  Function : Untuk Pertanyaan\
    "
    }
)
