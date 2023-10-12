# system.py
import os
import datetime
import inspect
import discord
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

def setactivebot():
    global ACTIVEBOTTOKEN
    global ACTIVEBOTSYSTEMCHANNELID
    if config.TESTMODE:
        ACTIVEBOTTOKEN = config.TESTBOT_TOKEN
        ACTIVEBOTSYSTEMCHANNELID = config.DEVSERVER_TESTRAURUSYSTEMID
    else:
        ACTIVEBOTTOKEN = config.RAURUBOT_TOKEN
        ACTIVEBOTSYSTEMCHANNELID = config.DEVSERVER_RAURUSYSTEMID

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


def console_base(logtype):
    return f'[{datetime.datetime.now()}] [{logtype}] '


def check_admin(ctx, frombanned = False):
    if ctx.guild:
        for roleid in config.ADMINROLES:
            if discord.utils.get(ctx.guild.roles, id=roleid) in ctx.author.roles:
                return True
        
        if ctx.author.id in config.BOT_AUTHADMINS:
            return True
        else:
            if not frombanned:
                print(console_base('System') + f'{ctx.author} was blocked from using command: {ctx.message.content}; by: {inspect.currentframe().f_code.co_name}')
                return False
            return False
    else:
        return False
    
def check_banned(ctx):
    if not check_admin(ctx, True):
        if not str(ctx.author.id) in DICT_BLACKLIST:
            return True
        else:
            print(console_base('System') + f'{ctx.author} was blocked from using command: {ctx.message.content}; by: {inspect.currentframe().f_code.co_name}')
            return False
    else:
        return True

def slashcheck_admin(interaction, frombanned = False):
    if interaction.guild:
        for roleid in config.ADMINROLES:
            if discord.utils.get(interaction.guild.roles, id=roleid) in interaction.user.roles:
                return True
        
        if interaction.user.id in config.BOT_AUTHADMINS:
            return True
        else:
            if not frombanned:
                print(console_base('System') + f'{interaction.user} was blocked from using command: {interaction.command}; by: {inspect.currentframe().f_code.co_name}')
                return False
            return False
    else:
        return False
    
def slashcheck_banned(interaction):
    if not slashcheck_admin(interaction, True):
        if not str(interaction.user.id) in DICT_BLACKLIST:
            return True
        else:
            print(console_base('System') + f'{interaction.user} was blocked from using command: {interaction.command}; by: {inspect.currentframe().f_code.co_name}')
            return False
    else:
        return True