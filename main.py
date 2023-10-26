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
    system.load_blacklist()
    await loadextensions()


    print(system.console_base('System') + f'{RauruBot.user.name} is online')
    print(system.console_base('System') + f'Current File Directory: {system.DIR_ROOT}')
    # Online Message
    try:
        channel = RauruBot.get_channel(system.ACTIVEBOTSYSTEMCHANNELID)
        
        await system.send(RauruBot, system.ACTIVEBOTSYSTEMCHANNELID, f'{RauruBot.user.name}' + messages.BOT_ONLINESIMPLE)
    except:
        print(system.console_base('Error') + f'Unable to send Online Message to channel: {system.ACTIVEBOTSYSTEMCHANNELID}')

@RauruBot.event
async def on_guild_join(guild):
    if not guild.id in config.AUTHSERVERS:
        await system.send(RauruBot, guild.system_channel.id, f'Unauthorized server detected!\nLeaving unauthorized server: {guild.name}!')
        print(system.console_base('System') + f'Detected unauthorized guild: {guild.name}')
        await guild.leave()
        print(system.console_base('System') + f'Unauthtorized guild left: {guild.name}')

    return

# Error listeners
@RauruBot.event
async def on_command_error(ctx, error):
    await system.on_command_error(ctx, error)

@RauruBot.tree.error
async def on_app_command_error(interaction, error):
    await system.on_app_command_error(interaction, error)


# Cogs
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
    
    await system.respond(ctx, ANSWER)

@RauruBot.command(name='reloadallcogs', aliases=['rldallcogs'])
@commands.is_owner()
async def reloadallcogs(ctx):
    ANSWER = 'Reloaded Cogs: `'
    ANSWER2 = 'Loaded Cogs: `'
    LOADED = False

    for cog in os.listdir(system.DIR_COGS):
        if cog.endswith('.py') == True:
            try:
                await RauruBot.reload_extension(f'cogs.{cog[:-3]}')
                ANSWER += cog + '`, `'
                print(system.console_base('System') + f'cogs.{cog} reloaded by: {ctx.author}')
            except:
                LOADED = True
                await RauruBot.load_extension(f'cogs.{cog[:-3]}')
                ANSWER2 += cog + '`, `'
                print(system.console_base('System') + f'cogs.{cog} loaded by: {ctx.author}')
    
    await system.respond(ctx, ANSWER)
    if LOADED:
        await system.respond(ctx, ANSWER2)


system.setactivebot()
RauruBot.run(system.ACTIVEBOTTOKEN)