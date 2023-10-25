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

DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
DIR_RESOURCE = os.path.join(DIR_ROOT, 'resources')
DIR_DATA = os.path.join(DIR_ROOT, 'data.json')
DIR_BLACKLIST = os.path.join(DIR_ROOT, 'blacklist.json')
DIR_COGS = os.path.join(DIR_ROOT, 'cogs')

DICT_BLACKLIST = {}

ERRORLOGGING = True

ACTIVEBOTTOKEN = None
ACTIVEBOTSYSTEMCHANNELID = None

# Setup
def setactivebot():
    global ACTIVEBOTTOKEN
    global ACTIVEBOTSYSTEMCHANNELID
    if config.TESTMODE:
        ACTIVEBOTTOKEN = config.TESTBOT_TOKEN
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
            if not str(context.author.id) in DICT_BLACKLIST:
                return True
            else:
                print(console_base('System') + f'{context.author} was blocked from using command: {context.message.content}; by: {inspect.currentframe().f_code.co_name}')
                return False
        else:
            return True
    
    elif type(context) == discord.Interaction:
        if not check_admin(context, True):
            if not str(context.user.id) in DICT_BLACKLIST:
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
        await ctx.send(messages.ERROR_NODM)
    elif isinstance(error, commands.errors.CheckFailure):
        await ctx.send(messages.ERROR_BADROLE)
    elif isinstance(error, commands.MissingRequiredArgument):
        if str(ctx.command) == 'blacklist':
            await ctx.send(messages.ERROR_BLACKLIST)
        else:
            await ctx.send(messages.ERROR_UNKNOWNCMD)
        
    elif ERRORLOGGING == True:
            print(error)

async def on_app_command_error(interaction, error):
    global ERRORLOGGING
    if isinstance(error, app_commands.CheckFailure):
        await interaction.response.send_message(messages.ERROR_BADROLE)
        
    elif ERRORLOGGING == True:
        print(error)

# Other System functions
async def respond(context: discord.Object, message: str, image = None, hidden: bool = False):
    
    if type(context) == discord.ext.commands.Context:
        if hidden:
            USER = context.author
            if image:
                try:
                    await USER.send(message, file=image)
                    NOTIFY = f'{messages.HELP_NOTIFY} {context.author.name}!'
                    await context.reply(NOTIFY)
                except:
                    NOTIFY = f'{messages.HELP_NOTIFYERROR1} {context.author.name}{messages.HELP_NOTIFYERROR2}'
                    await context.reply(NOTIFY)
            else:
                try:
                    await USER.send(message)
                    NOTIFY = f'{messages.HELP_NOTIFY} {context.author.name}!'
                    await context.reply(NOTIFY)
                except:
                    NOTIFY = f'{messages.HELP_NOTIFYERROR1} {context.author.name}{messages.HELP_NOTIFYERROR2}'
                    await context.reply(NOTIFY)
            return

        else:
            if image:
                await context.send(message, file=image)
            else:
                await context.send(message)
            return
    
    elif type(context) == discord.Interaction:
        if image:
            await context.response.send_message(message, file=image, ephemeral=hidden)
        else:
            await context.response.send_message(message, ephemeral=hidden)
        return

def argcleanup(arg: str):
    arg2 = arg.lower().replace("s ", "")
    arg2 = arg2.replace(" ", "")
    if arg2[-1] == 's':
        arg2 = arg2[:-1]

    return arg2
