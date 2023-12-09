# system.py

import os
import datetime
import inspect
import discord
from discord.ext import commands
from discord import app_commands
import messages
import config
import json
import random
import asyncio

DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
DIR_RESOURCE = os.path.join(DIR_ROOT, 'resources')
DIR_DATA = os.path.join(DIR_ROOT, 'data.json')
DIR_BLACKLIST = os.path.join(DIR_ROOT, 'blacklist.json')
DIR_COGS = os.path.join(DIR_ROOT, 'cogs')
DIR_ICONS = os.path.join(DIR_ROOT, 'boticons')

DICT_BLACKLIST = {}

ERRORLOGGING = True

ACTIVEBOTTOKEN = None
ACTIVEBOTSYSTEMCHANNELID = None

MESSAGEHISTORY = []

# Setup
def setactivebot():
    global ACTIVEBOTTOKEN
    global ACTIVEBOTSYSTEMCHANNELID
    if config.TESTMODE:
        ACTIVEBOTTOKEN = config.TESTRAURUBOT_TOKEN
        ACTIVEBOTSYSTEMCHANNELID = config.DEVSERVERCHANNELID_TSTRAURUSYS
    else:
        ACTIVEBOTTOKEN = config.RAURUBOT_TOKEN
        ACTIVEBOTSYSTEMCHANNELID = config.DEVSERVERCHANNELID_RAURUSYS

# Blacklist
def load_blacklist():
    global DICT_BLACKLIST
    
    print(console_base('System') + f'Loading blacklist...')
    
    try:
        with open(DIR_BLACKLIST, 'r') as inblacklist:
            DICT_BLACKLIST = json.load(inblacklist)
            
        print(DICT_BLACKLIST)
        print(console_base('System') + f'Blacklist loaded!')
        
    except FileNotFoundError:
        print(console_base('Error') + f'Unable to find blacklist file!')
        
    except:
        print(console_base('Error') + f'Unable to load blacklist!')

def save_blacklist():
    global DICT_BLACKLIST
    
    print(console_base('System') + f'Saving blacklist...')
    
    try:
        with open(DIR_BLACKLIST, 'w') as outfile:
            json.dump(DICT_BLACKLIST, outfile)
            
        print(DICT_BLACKLIST)
        print(console_base('System') + f'Blacklist saved!')
    
    except:
        print(console_base('Error') + f'Unable to save blacklist!')

# Logging
def console_base(logtype):
    return f'[{datetime.datetime.now()}] [{logtype}] '

# Checks
def check_admin(context, frombanned = False):
    if type(context) == discord.ext.commands.Context:
        if context.guild:
            for roleid in config.ADMINROLES:
                if discord.utils.get(context.guild.roles, id=roleid) in context.author.roles:
                    return True

            if context.author.id in config.BOT_AUTHADMINS:
                return True
            else:
                if not frombanned:
                    print(console_base('System') + f'{context.author} was blocked from using command: {context.message.content}; by: {inspect.currentframe().f_code.co_name}')
                    return False
                return False
        else:
            return False

    elif type(context) == discord.Interaction:
        if context.guild:
            for roleid in config.ADMINROLES:
                if discord.utils.get(context.guild.roles, id=roleid) in context.user.roles:
                    return True

            if context.user.id in config.BOT_AUTHADMINS:
                return True
            else:
                if not frombanned:
                    print(console_base('System') + f'{context.user} was blocked from using command: {context.command.name}; by: {inspect.currentframe().f_code.co_name}')
                    return False
                return False
        else:
            return False

def check_banned(context):
    if type(context) == discord.ext.commands.Context:
        if not check_admin(context, True):
            if not str(context.author.id) + str(context.guild.id) in DICT_BLACKLIST:
                return True
            else:
                print(console_base('System') + f'{context.author} was blocked from using command: {context.message.content}; by: {inspect.currentframe().f_code.co_name}')
                return False
        else:
            return True
    
    elif type(context) == discord.Interaction:
        if not check_admin(context, True):
            if not str(context.user.id) + str(context.guild.id) in DICT_BLACKLIST:
                return True
            else:
                print(console_base('System') + f'{context.user} was blocked from using command: {context.command.name}; by: {inspect.currentframe().f_code.co_name}')
                return False
        else:
            return True

# Error handling
async def on_command_error(ctx, error):
    global ERRORLOGGING
    if isinstance(error, commands.NoPrivateMessage):
        await respond(ctx, messages.ERROR_GUILDONLY)
    elif isinstance(error, commands.errors.CheckFailure):
        await respond(ctx, messages.ERROR_BADROLE)
    elif isinstance(error, commands.MissingRequiredArgument):
        if str(ctx.command) == 'blacklist':
            await respond(ctx, messages.ERROR_BLACKLIST)
        else:
            await respond(ctx, messages.ERROR_UNKNOWNCMD)
        
    elif ERRORLOGGING == True:
            print(error)

async def on_app_command_error(interaction, error):
    global ERRORLOGGING
    if isinstance(error, app_commands.CheckFailure):
        await respond(interaction, messages.ERROR_BADROLE)
        
    elif ERRORLOGGING == True:
        print(error)

# Other System functions
async def setprofilepic(bot, option):
    IMAGEPATH = ''
    PRIDEPATH = 'prideicons'
    IMAGENAME = ''
    PRIDE = False

    OPTION = argcleanup(option)

    match OPTION:
        case 'default':
            if not config.TESTMODE:
                IMAGENAME = 'rauruicon.jpg'
            else:
                IMAGENAME = 'testrauruicon.jpg'

        case 'rauru':
            IMAGENAME = 'rauruicon.jpg'
        case 'testrauru':
            IMAGENAME = 'testrauruicon.jpg'
        
        case 'funny':
            IMAGENAME = 'rauruiconfunny.jpg'

        case 'pride':
            PRIDE = True
            OPTIONS = os.listdir(os.path.join(DIR_ICONS, PRIDEPATH))
            CHOICE = random.randint(1, len(OPTIONS))

            IMAGENAME = OPTIONS[CHOICE - 1]
        
        case 'prideace':
            PRIDE = True
            IMAGENAME = 'rauruacepride.jpg'
        case 'pridebi':
            PRIDE = True
            IMAGENAME = 'raurubisexualpride.jpg'
        case 'pridegay':
            PRIDE = True
            IMAGENAME = 'raurugaypride.jpg'
        case 'pridegenderfluid':
            PRIDE = True
            IMAGENAME = 'raurugenderfluidpride.jpg'
        case 'pridelesbian':
            PRIDE = True
            IMAGENAME = 'raurulesbianpride.jpg'
        case 'pridenb':
            PRIDE = True
            IMAGENAME = 'raurunonbinarypride.jpg'
        case 'pridepan':
            PRIDE = True
            IMAGENAME = 'raurupansexualpride.jpg'
        case 'pridegeneral':
            PRIDE = True
            IMAGENAME = 'raurupride.jpg'
        case 'pridetran':
            PRIDE = True
            IMAGENAME = 'raurutransgenderpride.jpg'


        case _:
            if not config.TESTMODE:
                IMAGENAME = 'rauruicon.jpg'
            else:
                IMAGENAME = 'testrauruicon.jpg'
    
    if PRIDE:
        IMAGEPATH = os.path.join(DIR_ICONS, PRIDEPATH, IMAGENAME)
    else:
        IMAGEPATH = os.path.join(DIR_ICONS, IMAGENAME)
    
    with open(IMAGEPATH, 'rb') as image:
        await bot.user.edit(avatar=image.read())
    await send(bot, ACTIVEBOTSYSTEMCHANNELID, f'{bot.user.name} profile picture set to: {IMAGENAME}')
    print(console_base('System') + f'{bot.user.name} profile picture set to: {IMAGENAME}')

    return IMAGENAME

async def respond(context: discord.Object, message: str, image = None, hidden: bool = False, silent: bool = False, time: int = 0):
    
    if type(context) == discord.ext.commands.Context:
        if hidden:
            USER = context.author
            if image:
                try:
                    await USER.send(message, file=image)
                    NOTIFY = f'{messages.HELP_NOTIFY} {context.author.name}!'
                    msg = await context.reply(NOTIFY, silent=True)
                except:
                    NOTIFY = f'{messages.HELP_NOTIFYERROR1} {context.author.name}{messages.HELP_NOTIFYERROR2}'
                    msg = await context.reply(NOTIFY, silent=True)
            else:
                try:
                    await USER.send(message)
                    NOTIFY = f'{messages.HELP_NOTIFY} {context.author.name}!'
                    msg = await context.reply(NOTIFY, silent=True)
                except:
                    NOTIFY = f'{messages.HELP_NOTIFYERROR1} {context.author.name}{messages.HELP_NOTIFYERROR2}'
                    msg = await context.reply(NOTIFY, silent=True)

        else:
            if image:
                msg = await context.send(message, file=image, silent=silent)
            else:
                msg = await context.send(message, silent=silent)
    
    elif type(context) == discord.Interaction:
        if image:
           await context.response.send_message(message, file=image, ephemeral=hidden, silent=silent)
           msg = await context.original_response()
        else:
           await context.response.send_message(message, ephemeral=hidden, silent=silent)
           msg = await context.original_response()

    if time == 0:
        storemessageid(context.channel.id, msg.id)
        return msg
    else:
        await asyncio.sleep(time)
        await msg.delete()


async def send(bot, channelid: int, message: str, image = None):
    channel = bot.get_channel(channelid)
    if image:
        msg = await channel.send(message, file=image)
    else:
        msg = await channel.send(message)
    
    storemessageid(channelid, msg.id)
    return msg

def storemessageid(channelid: int, messageid: int):
    global MESSAGEHISTORY

    if len(MESSAGEHISTORY) >= 25:
        MESSAGEHISTORY.pop(0)
    
    MESSAGEHISTORY.append([channelid, messageid])


def argcleanup(arg: str):
    arg2 = arg.lower().replace("s ", "")
    arg2 = arg2.replace(" ", "")
    if arg2[-1] == 's':
        arg2 = arg2[:-1]

    return arg2

def translate_to_url(arg: str):
    replacements = {" ": "%20", '"': "%22", ":": "%3A", "'": "%20", "?": "%3F", "/": "%2F"}
    translation_table = str.maketrans(replacements)
    return arg.translate(translation_table)