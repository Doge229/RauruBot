# generalslash.py

import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Greedy
import system
import messages
import random


class generalslash(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()

    @app_commands.command(name='help', description='See what commands I have!')
    @commands.guild_only()
    @app_commands.check(system.slashcheck_banned)
    async def helpgeneral(self, interaction: discord.Interaction, option: str = '1'):
        ANSWER = ''
        EPHEMERAL = False

        arg = option.lower().replace("s ", "")
        arg = arg.replace(" ", "")
        if arg[-1] == 's':
            arg = arg[:-1]
        
        match arg:
            case '':
                EPHEMERAL = True
                ANSWER = messages.HELP_GENERAL
            case '1':
                EPHEMERAL = True
                ANSWER = messages.HELP_GENERAL
            case 'show':
                ANSWER = messages.HELP_GENERAL
            case 'show1':
                ANSWER = messages.HELP_GENERAL
            case 'showpage1':
                ANSWER = messages.HELP_GENERAL
            
            case _:
                ANSWER = messages.ERROR_UNKNOWNCMD
        
        await interaction.response.send_message(ANSWER, ephemeral=EPHEMERAL)

    @app_commands.command(name='find', description='Create an Object Map link with your search terms integrated into it')
    @commands.guild_only()
    @app_commands.check(system.slashcheck_banned)
    async def objmaplinkcreator(self, interaction: discord.Interaction, *, searchterms: str):
        ANSWER = ''
        LAYER = 'Surface'

        TERMS = searchterms
        TERMS = TERMS.replace(" ", "%20")
        TERMS = TERMS.replace('"', "%22")
        TERMS = TERMS.replace(":", "%3A")
        TERMS = TERMS.replace("'", "%20")
        TERMS = TERMS.replace("-", "%20")


        if 'sky' in TERMS.lower() and not 'not sky' in searchterms.lower():
            LAYER = 'Sky'
        elif 'depths' in TERMS.lower() and not 'not depths' in searchterms.lower():
            LAYER = 'Depths'


        LINK = messages.COMMAND_OBJMAPBASELINK + LAYER + '?q=' + TERMS
        ANSWER = messages.COMMAND_OBJMAPTERMS + '`' + searchterms + '`:\n' + LINK + '\n' + messages.COMMAND_OBJMAPNOTE

        await interaction.response.send_message(ANSWER)

    @app_commands.command(name='coordconvert', description='Convert the coordinates of an object on the Object Map to in-game coordinates')
    @commands.guild_only()
    @app_commands.check(system.slashcheck_banned)
    async def coordconverter(self, interaction: discord.Interaction, *, coordinates: str):
        ANSWER = ''

        try:
            OBJMAPCOORDS = coordinates.lower().strip()
            objcoords = OBJMAPCOORDS.split(", ")

            Xcoord = round(float(objcoords[0]))
            Zcoord = round(float(objcoords[1])) - 105
            Ycoord = round(float(objcoords[2]))

            showncoords = str(Xcoord) + ', ' + str(Ycoord) + ', ' + str(Zcoord)

            ANSWER = messages.CONVERT_COORD1 + '`' + coordinates + '`' + messages.CONVERT_COORD2 + '`' + showncoords + '`'
        except:
            ANSWER = messages.ERROR_BADCOORDS

        await interaction.response.send_message(ANSWER)

    @app_commands.command(name='findpristine', description='Create an Object Map link that shows all the Depths Ghosts that can spawn a specific weapon')
    @commands.guild_only()
    @app_commands.check(system.slashcheck_banned)
    async def findpristine(self, interaction: discord.Interaction, *, weaponname: str):
        ANSWER = ''

        TERMS = weaponname
        TERMS = TERMS.replace(" ", "%20")
        TERMS = TERMS.replace('"', "%22")
        TERMS = TERMS.replace(":", "%3A")
        TERMS = TERMS.replace("'", "%20")
        TERMS = TERMS.replace("-", "%20")

        LINK = messages.COMMAND_OBJMAPBASELINK +'Depths?q=minusfieldghost%20' + TERMS
        ANSWER = messages.COMMAND_FINDPRISTINE1 + '`' + weaponname + '`:\n' + LINK

        await interaction.response.send_message(ANSWER)
    
    @app_commands.command(name='finddispenser', description='See which Device Dispensers can dispense a specific Zonai Device capsule')
    @commands.guild_only()
    @app_commands.check(system.slashcheck_banned)
    async def finddispenser(self, interaction: discord.Interaction, *, device: str):
        ANSWER = ''
        DISPENSERS = ''
        VALID = True

        TERM = device
        device = device.lower().replace("s ", "")
        device = device.replace(" ", "")
        if device[-1] == 's':
            device = device[:-1]

        match device:
            case 'fan':
                DISPENSERS = messages.DISP_FAN
            case 'wing':
                DISPENSERS = messages.DISP_WING
            case 'cart':
                DISPENSERS = messages.DISP_CART
            case 'balloon':
                DISPENSERS = messages.DISP_BALLOON
            case 'rocket':
                DISPENSERS = messages.DISP_ROCKET
            case 'timebomb':
                DISPENSERS = messages.DISP_TIMEBOMB
            case 'portablepot':
                DISPENSERS = messages.DISP_PORTABLEPOT
            case 'flameemitter':
                DISPENSERS = messages.DISP_FLAMEEMITTER
            case 'frostemitter':
                DISPENSERS = messages.DISP_FROSTEMITTER
            case 'shockemitter':
                DISPENSERS = messages.DISP_SHOCKEMITTER
            case 'beamemitter':
                DISPENSERS = messages.DISP_BEAMEMITTER
            case 'hydrant':
                DISPENSERS = messages.DISP_HYDRANT
            case 'steeringstick':
                DISPENSERS = messages.DISP_STEERINGSTICK
            case 'bigwheel':
                DISPENSERS = messages.DISP_BIGWHEEL
            case 'smallwheel':
                DISPENSERS = messages.DISP_SMALLWHEEL
            case 'sled':
                DISPENSERS = messages.DISP_SLED
            case 'battery':
                DISPENSERS = messages.DISP_BATTERY
            case 'bigbattery':
                VALID = False
                ANSWER = messages.DISP_BIGBATTERY
            case 'spring':
                DISPENSERS = messages.DISP_SPRING
            case 'cannon':
                DISPENSERS = messages.DISP_CANNON
            case 'stabilizer':
                DISPENSERS = messages.DISP_STABILIZER
            case 'hoverstone':
                DISPENSERS = messages.DISP_HOVERSTONE
            case 'light':
                DISPENSERS = messages.DISP_LIGHT
            case 'stake':
                DISPENSERS = messages.DISP_STAKE
            case 'mirror':
                DISPENSERS = messages.DISP_MIRROR
            case 'homingcart':
                DISPENSERS = messages.DISP_HOMINGCART
            case 'constructhead':
                DISPENSERS = messages.DISP_CONSTRUCTHEAD

            case _:
                VALID = False
                ANSWER = messages.ERROR_UNKNOWNCMD

        if VALID:
            ANSWER = messages.DISP_BASE + f'`{TERM}`' + messages.DISP_BASE2 + f'\n' + DISPENSERS

        await interaction.response.send_message(ANSWER)

    @app_commands.command(name='hi')
    @commands.guild_only()
    @app_commands.check(system.slashcheck_banned)
    async def hello(self, interaction: discord.Interaction):
        ANSWER = ''

        CHOICE = random.randint(1, 6)

        match CHOICE:
            case 1:
                ANSWER = messages.COMMAND_HELLO1
            case 2:
                ANSWER = messages.COMMAND_HELLO2
            case 3:
                ANSWER = messages.COMMAND_HELLO3
            case 4:
                ANSWER = f'{messages.COMMAND_HELLO1[:-1]} <@{interaction.user.id}>!'
            case 5:
                ANSWER = f'{messages.COMMAND_HELLO2[:-1]} <@{interaction.user.id}>!'
            case 6:
                ANSWER = f'{messages.COMMAND_HELLO3[:-1]} <@{interaction.user.id}>!'
        
        await interaction.response.send_message(ANSWER)

async def setup(bot):
    await bot.add_cog(generalslash(bot))