# Alvin Gans

from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern="^.bee$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥🟥⬜️⬜️🟥⬜️⬜️🟥🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥🟥⬜️⬜️🟥⬜️⬜️🟥🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥🟥⬜️⬜️🟥⬜️⬜️🟥🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥 𝙇𝙀𝘽𝘼𝙃-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ⬜️🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥🟥⬜️⬜️🟥⬜️⬜️🟥🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥 𝙇𝙀𝘽𝘼𝙃-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ⬜️🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥🟥⬜️⬜️🟥⬜️⬜️🟥🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥 𝙇𝙀𝘽𝘼𝙃-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ⬜🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥🟥⬜️⬜️🟥⬜️⬜️🟥🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥 𝙇𝙀𝘽𝘼𝙃-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ⬜🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥🟥⬜️⬜️🟥⬜️⬜️🟥🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥 𝙇𝙀𝘽𝘼𝙃-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ⬜🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥🟥⬜️⬜️🟥⬜️⬜️🟥🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥 𝙇𝙀𝘽𝘼𝙃-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ⬜🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥     -𝙁𝙊𝙍𝙆 𝙇𝙊𝙍𝘿 -   ⬜🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥🟥⬜️⬜️🟥⬜️⬜️🟥🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥 𝙇𝙀𝘽𝘼𝙃-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ⬜🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥     -𝙁𝙊𝙍𝙆 𝙇𝙊𝙍𝘿 -   ⬜🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥🟥⬜️⬜️🟥⬜️⬜️🟥🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥 𝙇𝙀𝘽𝘼𝙃-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ⬜🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥     -𝙁𝙊𝙍𝙆 𝙇𝙊𝙍𝘿 -   ⬜🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥🟥⬜️⬜️🟥⬜️⬜️🟥🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥 𝙇𝙀𝘽𝘼𝙃-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ⬜🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥     -𝙁𝙊𝙍𝙆 𝙇𝙊𝙍𝘿 -   ⬜🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥")
        await e.edit("🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥🟥⬜️⬜️🟥⬜️⬜️🟥🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥 𝙇𝙀𝘽𝘼𝙃-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ⬜🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🔲🟥🟥🔲🟥🟥🔲🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥 \n🟥     -𝙁𝙊𝙍𝙆 𝙇𝙊𝙍𝘿 -   ⬜🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥⬜️🟥🟥⬜️🟥🟥⬜️🟥 \n🟥🟥🟥🟥🟥🟥🟥🟥🟥")


@register(outgoing=True, pattern='^.huh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />❤️ *Ini Buat Kamu`")
    sleep(3)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n/>💔  *Aku Ambil Lagi`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n💔<\\  *Terimakasih`")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "ceritacinta":

        await event.edit(input_str)

        animation_chars = [
            "`Cerita ❤️ Cinta` ",
            "  😐             😕 \n/👕\\         <👗\\ \n 👖               /|",
            "  😉          😳 \n/👕\\       /👗\\ \n  👖            /|",
            "  😚            😒 \n/👕\\         <👗> \n  👖             /|",
            "  😍         ☺️ \n/👕\\      /👗\\ \n  👖          /|",
            "  😍          😍 \n/👕\\       /👗\\ \n  👖           /|",
            "  😘   😊 \n /👕\\/👗\\ \n   👖   /|",
            " 😳  😁 \n /|\\ /👙\\ \n /     / |",
            "😈    /😰\\ \n<|\\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\\   /(👶)\\ \n  /!\\   / \\ ",
            "`TAMAT 😅`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "canda":

        await event.edit(input_str)

        animation_chars = [
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Kamu    ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Pasti   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__|⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Belum   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀(x)⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Mandi  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Bwhaha  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__| ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Canda   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀****⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@register(outgoing=True, pattern='^.nah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />💖 *Ini Buat Kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n💖<\\  *Tapi Bo'ong`")
# Alpinnnn Gans


@register(outgoing=True, pattern='^.usagee(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Mengecek Sisa Kuota...`")
    sleep(1)
    await typew.edit("╭┈──────────────────┈╮ \n    ⚡️ 𝗙 𝗟 𝗔 𝗦 𝗛 - 𝗞 𝗨 𝗢 𝗧 𝗔 💢  \n╭┈──────────────────┈╯ \n➥ **Kuota Terpakai :**\n➥ 0 Jam - 0 Menit - 0%\n┈───────────────────┈\n➥ **Kuota Tersisa :**\n➥ 8888 Jam - 8888 Menit - 100%\n╰┈────────────────┈─➤"
                     )
# @BluueBlueSky

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "owner":

        await event.edit(input_str)

        animation_chars = [
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬜⬜⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])
# Alvin Imut
# Alvin Gans
# Lord
CMD_HELP.update({
    "animasi":
    "`.nah` ; `.usagee` ; `.huh` ; `.owner`\
    \nUsage: cobain.\
    \n\n`.bunga` ; `.buah`\
    \nUsage: animasi.\
    \n\n`.waktu`\
    \nUsage: animasi.\
    \n\n`.hua`\
    \nUsage: nangis.\
    \n\n`.ceritacinta` ; `.canda`\
    \nUsage: liat sendiri"
})
