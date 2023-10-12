# main.py
import os
import discord
from discord.ext import commands
import system
import messages
import config

# Bot Setup
INTENTS = discord.Intents.default()
INTENTS.messages = True
INTENTS.message_content = True

USERID_SELF = config.USERID_RAURUBOT
RauruBot = commands.Bot(command_prefix=[f'<@&{USERID_SELF}> ', f'<@{USERID_SELF}> ', f'<@&{USERID_SELF}>', f'<@{USERID_SELF}>', '?'], intents=INTENTS, case_insensitive=True, help_command=None)

@RauruBot.event
async def on_ready():

    print(system.console_base('System') + f'{RauruBot.user.name} is online')
    print(system.console_base('System') + f'Current File Directory: {system.DIR_ROOT}')
    
    # Online Message
    try:
        channel = RauruBot.get_channel(system.ACTIVEBOTSYSTEMCHANNELID)
        
        await channel.send(messages.BOT_ONLINESIMPLE)
    except:
        print(system.console_base('Error') + f'Unable to send Online Message to channel: {system.ACTIVEBOTSYSTEMCHANNELID}')
    
    system.load_blacklist()

    await loadextensions()
    
#@RauruBot.event
#async def on_command_error(ctx, error):
#    if isinstance(error, commands.NoPrivateMessage):
#        await ctx.send(messages.ERROR_NODM)
#    elif isinstance(error, commands.errors.CheckFailure):
#        await ctx.send(messages.ERROR_BADROLE)
#    elif isinstance(error, commands.MissingRequiredArgument):
#        if str(ctx.command) == 'blacklist':
#            await ctx.send(messages.ERROR_BLACKLIST)
#            #print(error)
#        else:
#            await ctx.send(messages.ERROR_UNKNOWNCMD)
#    elif system.ERRORLOGGING == True:
#        print(error)


#Cogs
async def loadextensions():
    for cog in os.listdir(system.DIR_COGS):
        if cog.endswith('.py') == True:
            await RauruBot.load_extension(f'cogs.{cog[:-3]}')
            print(system.console_base('System') + f'cogs.{cog} loaded')

@RauruBot.command(name='reloadcog', aliases=['rldcog'])
@commands.is_owner()
async def reloadcog(ctx, arg):

    ARG = arg.lower().replace(" ", "")
    ANSWER = ''

    try:
        await RauruBot.reload_extension(f'cogs.{ARG}')
        ANSWER = f'Reloaded Cog: `{arg}`'
        print(system.console_base('System') + f'cogs.{arg} reloaded by: {ctx.author}')
    except:
        ANSWER = 'Unable to reload Cog!'
        print(system.console_base('Error') + f'cogs.{arg} failed to be reloaded by: {ctx.author}')
    
    await ctx.send(ANSWER)

@RauruBot.command(name='reloadallcogs', aliases=['rldallcogs'])
@commands.is_owner()
async def reloadallcogs(ctx):
    ANSWER = 'Reloaded Cogs: `'
    ANSWER2 = 'Loaded Cogs: `'

    for cog in os.listdir(system.DIR_COGS):
        if cog.endswith('.py') == True:
            try:
                await RauruBot.reload_extension(f'cogs.{cog[:-3]}')
                ANSWER += cog + '`, `'
                print(system.console_base('System') + f'cogs.{cog} reloaded by: {ctx.author}')
            except:
                await RauruBot.load_extension(f'cogs.{cog[:-3]}')
                ANSWER2 += cog + '`, `'
                print(system.console_base('System') + f'cogs.{cog} loaded by: {ctx.author}')
    
    await ctx.send(ANSWER)
    await ctx.send(ANSWER2)


system.setactivebot()
RauruBot.run(system.ACTIVEBOTTOKEN)