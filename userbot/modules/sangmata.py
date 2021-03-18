# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Port to userbot by @MoveAngel

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register
from asyncio.exceptions import TimeoutError


@register(outgoing=True, pattern=r"^\.sa(?: |$)(.*)")
async def lastname(steal):
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await steal.edit("𝘔𝘰𝘩𝘰𝘯 𝘉𝘢𝘭𝘢𝘴 𝘒𝘦 𝘗𝘦𝘴𝘢𝘯 𝘗𝘦𝘯𝘨𝘨𝘶𝘯𝘢.")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await steal.edit("𝘉𝘢𝘭𝘢𝘴 𝘒𝘦 𝘗𝘦𝘴𝘢𝘯 𝘗𝘦𝘯𝘨𝘨𝘶𝘯𝘢 𝘠𝘢𝘯𝘨 𝘚𝘦𝘣𝘦𝘯𝘢𝘳𝘯𝘺𝘢.")
        return
    await steal.edit("𝘔𝘦𝘯𝘨𝘢𝘮𝘣𝘪𝘭 𝘪𝘯𝘧𝘰𝘳𝘮𝘢𝘴𝘪 𝘳𝘪𝘸𝘢𝘺𝘢𝘵 𝘱𝘦𝘳𝘨𝘢𝘯𝘵𝘪𝘢𝘯 𝘯𝘢𝘮𝘢 𝘰𝘳𝘢𝘯𝘨 𝘪𝘯𝘪...")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "Mohon Unblock @sangmatainfo_bot Dan Coba Lagi"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await steal.edit(f"`{r.message}`")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await steal.edit("𝘚𝘢𝘺𝘢 𝘛𝘪𝘥𝘢𝘬 𝘔𝘦𝘯𝘦𝘮𝘶𝘬𝘢𝘯 𝘐𝘯𝘧𝘰𝘳𝘮𝘢𝘴𝘪 𝘗𝘦𝘳𝘨𝘢𝘯𝘵𝘪𝘢𝘯 𝘕𝘢𝘮𝘢, 𝘖𝘳𝘢𝘯𝘨 𝘐𝘯𝘪 𝘉𝘦𝘭𝘶𝘮 𝘗𝘦𝘳𝘯𝘢𝘩 𝘔𝘦𝘯𝘨𝘨𝘢𝘯𝘵𝘪 𝘕𝘢𝘮𝘢𝘯𝘺𝘢.")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await steal.edit(f"```{response.message}```")
            await steal.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await steal.edit("𝘚𝘦𝘱𝘦𝘳𝘵𝘪𝘯𝘺𝘢 𝘵𝘦𝘳𝘫𝘢𝘥𝘪 𝘦𝘳𝘳𝘰𝘳, 𝘮𝘢𝘢𝘧.")


CMD_HELP.update({
    "sangmata":
        "`.sa`\
          \nUsage: Mendapatkan Riwayat Nama Pengguna."
})
