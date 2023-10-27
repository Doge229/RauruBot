# general.py

import discord
from discord.ext import commands
import system
import messages
import random


class General(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()

    async def generalhelp(context, arg):
        ANSWER = ''
        EPHEMERAL = False

        arg = system.argcleanup(arg)
        
        match arg:
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
        
        await system.respond(context, ANSWER, hidden=EPHEMERAL)


    async def objmaplinkcreator(context, arg):
        ANSWER = ''
        LAYER = 'Surface'

        TERMS = arg
        TERMS = TERMS.replace(" ", "%20")
        TERMS = TERMS.replace('"', "%22")
        TERMS = TERMS.replace(":", "%3A")
        TERMS = TERMS.replace("'", "%20")
        TERMS = TERMS.replace("-", "%20")

        if 'sky' in TERMS.lower() and not 'not sky' in arg.lower():
            LAYER = 'Sky'
        elif 'depths' in TERMS.lower() and not 'not depths' in arg.lower():
            LAYER = 'Depths'

        LINK = messages.COMMAND_OBJMAPBASELINK + LAYER + '?q=' + TERMS
        ANSWER = messages.COMMAND_OBJMAPTERMS + '`' + arg + '`:\n' + LINK + '\n' + messages.COMMAND_OBJMAPNOTE

        await system.respond(context, ANSWER)

    async def coordconverter(context, arg):
        ANSWER = ''

        try:
            OBJMAPCOORDS = arg.lower().strip()
            objcoords = OBJMAPCOORDS.split(", ")

            Xcoord = round(float(objcoords[0]))
            Zcoord = round(float(objcoords[1])) - 105
            Ycoord = round(float(objcoords[2]))

            showncoords = str(Xcoord) + ', ' + str(Ycoord) + ', ' + str(Zcoord)

            ANSWER = messages.CONVERT_COORD1 + '`' + arg + '`' + messages.CONVERT_COORD2 + '`' + showncoords + '`'
        except:
            ANSWER = messages.ERROR_BADCOORDS

        await system.respond(context, ANSWER)

    async def findpristine(context, arg):
        ANSWER = ''

        TERMS = arg
        TERMS = TERMS.replace(" ", "%20")
        TERMS = TERMS.replace('"', "%22")
        TERMS = TERMS.replace(":", "%3A")
        TERMS = TERMS.replace("'", "%20")
        TERMS = TERMS.replace("-", "%20")

        LINK = messages.COMMAND_OBJMAPBASELINK +'Depths?q=%22Npc_MinusFieldGhost_000%22%20' + TERMS
        ANSWER = messages.COMMAND_FINDPRISTINE1 + '`' + arg + '`:\n' + LINK

        await system.respond(context, ANSWER)

    async def finddispenser(context, arg):
        ANSWER = ''
        DISPENSERS = ''
        VALID = True
        TERM = arg

        arg = system.argcleanup(arg)

        match arg:
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

        await system.respond(context, ANSWER)

    async def hello(context):
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
                if type(context) == discord.ext.commands.Context:
                    ANSWER = f'{messages.COMMAND_HELLO1[:-1]} <@{context.author.id}>!'
                elif type(context) == discord.Interaction:
                    ANSWER = f'{messages.COMMAND_HELLO1[:-1]} <@{context.user.id}>!'
            case 5:
                if type(context) == discord.ext.commands.Context:
                    ANSWER = f'{messages.COMMAND_HELLO2[:-1]} <@{context.author.id}>!'
                elif type(context) == discord.Interaction:
                    ANSWER = f'{messages.COMMAND_HELLO2[:-1]} <@{context.user.id}>!'
            case 6:
                if type(context) == discord.ext.commands.Context:
                    ANSWER = f'{messages.COMMAND_HELLO3[:-1]} <@{context.author.id}>!'
                elif type(context) == discord.Interaction:
                    ANSWER = f'{messages.COMMAND_HELLO3[:-1]} <@{context.user.id}>!'
        
        await system.respond(context, ANSWER)


async def setup(bot):
    await bot.add_cog(General(bot))