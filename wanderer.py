# Work with Python 3.6
import discord
from dataPantone import *
from imgPantone import *

# USEFUL LINKS
# https://www.devdungeon.com/content/make-discord-bot-python
# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
# https://discordpy.readthedocs.io/en/latest/api.html#event-reference
# https://www.w3schools.com/python/ref_func_zip.asp

# pantone_aliases = []
# pantone_codes = []
# pantone_hex = []
# pantone_rgb = []
TOKEN = "TOKEN"
charCommand = "!"

client = discord.Client()
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith(charCommand+"wanderer"):
        msg = "Hello ~~Dave~~ {0.author.mention}".format(message)
        print("-----------------------------------------")
        print("Command WANDERER by "+message.author.mention)
        await client.send_message(message.channel, msg)

    if message.content.startswith(charCommand+"watts"):
        emb = discord.Embed(title='', description="The only way to make sense out of change is to plunge into it, move with it, and join the dance.",colour=0x72DEC2)
        emb.set_author(name="Alan Watts", icon_url=client.user.default_avatar_url)
        print("--------------------------------------")
        print("Command WATTS by "+message.author.mention)
        await client.send_message(message.channel, embed=emb)

    if message.content.startswith(charCommand+"pantone "):
        color = message.content[len(charCommand+"pantone"):].strip().lower()
        try:
            posAlias = pantone_aliases.index(color)
            pos = posAlias
        except ValueError:
            try:
                posCode = pantone_codes.index(color)
                pos = posCode
            except ValueError:
                pos = -1

        if pos == -1:   # Color doesn't exist
            embedTitle = ""
            embedStr = "I'm afraid I can't find that color. :slight_frown:"
        else:           # Color found
            rgbstr = ""
            for rgbchannel in pantone_rgb[pos]:
                rgbstr += rgbchannel + ", "

            if pantone_aliases[pos] == "no-alias":
                embedTitle = pantone_codes[pos].title()
                embedStr=("Alias: {alias}\n"
                    "Code: {code}\n"
                    "Hexadecimal: #{hex}\n"
                    "RGB: {rgb}").format(alias = "", \
                    code = pantone_codes[pos].title(), \
                    hex = pantone_hex[pos].upper(), \
                    rgb = rgbstr.rstrip(", "))
                colorAlias = ""
            else:
                embedTitle = pantone_aliases[pos].title()
                embedStr=("Alias: {alias}\n"
                    "Code: {code}\n"
                    "Hexadecimal: #{hex}\n"
                    "RGB: {rgb}").format(alias = pantone_aliases[pos].title(), \
                    code = pantone_codes[pos].title(), \
                    hex = pantone_hex[pos].upper(), \
                    rgb = rgbstr.rstrip(", "))
                colorAlias = pantone_aliases[pos].title()

            colorCode = pantone_codes[pos].title()
            colorHex = "#"+pantone_hex[pos].upper()
            colorRgb = rgbstr.rstrip(", ")

        print("----------------------------------------")
        print("Command PANTONE by "+message.author.mention)
        imagePantoneFilename = 'out_bot.png'
        imagePantone = drawPantone(colorAlias, colorCode, colorHex, colorRgb, imagePantoneFilename)
        print(embedStr)
        await client.send_file(message.channel, imagePantone)
        # await client.send_message(message.channel, embed=discord.Embed(title = embedTitle, description = embedStr, colour = 0x72DEC2))

    if message.content.startswith(charCommand+"pantonelist"):
        filePantoneName = "pantone-colors.txt"
        filePantone = open(filePantoneName,"w+")
        for th in zip(pantone_aliases, pantone_codes):
            if th[0] == "no-alias":
                filePantone.write(th[1].title()+"\r\n")
            else:
                filePantone.write(th[1].title()+" "+th[0].title()+"\r\n")
        filePantone.close()
        print("--------------------------------------------")
        print("Command PANTONELIST by "+message.author.mention)
        await client.send_file(message.author, filePantoneName)

    if message.content.startswith(charCommand+"help"):
        commandList = ("```\n"
            ""+charCommand+"help  -  I display this message.\n"
            ""+charCommand+"pantonelist  -  I send you a file with all the Pantone® colors in my database.\n"
            ""+charCommand+"pantone [code or alias]  -  I give you more information about that Pantone® color.\n"
            ""+charCommand+"wanderer  -   It's my name.\n"
            ""+charCommand+"watts  -  I'll quote Alan Watts\n"
            "```")
        await client.send_message(message.author, commandList)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
