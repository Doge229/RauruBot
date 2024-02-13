# main.py

import os
import discord
from discord.ext import commands
import system
import messages
import config
from logger import Logger
import traceback

# Bot Setup
INTENTS = discord.Intents.default()
INTENTS.messages = True
INTENTS.message_content = True

USERID_SELF = config.USERID_RAURUBOT
RauruBot = commands.Bot(command_prefix=[f'<@&{USERID_SELF}> ', f'<@{USERID_SELF}> ', f'<@&{USERID_SELF}>', f'<@{USERID_SELF}>', '?', '&'], intents=INTENTS, case_insensitive=True, help_command=None)

@RauruBot.event
async def on_ready():
    system.load_blacklist()
    await loadextensions()
    await RauruBot.change_presence(activity=discord.Game(name="Use /help to see my commands!"))

    Logger.system(f'{RauruBot.user.name} is online')
    Logger.system(f'Current File Directory: {system.DIR_ROOT}')
    Logger.info(messages.INFO_CREDITS)
    # Online Message
    try:
        await system.send(RauruBot, system.ACTIVEBOTSYSTEMCHANNELID, f'{RauruBot.user.name}' + messages.BOT_ONLINESIMPLE)
    except:
        Logger.error(f'Unable to send Online Message to channel: {system.ACTIVEBOTSYSTEMCHANNELID}')

@RauruBot.event
async def on_guild_join(guild):
    if not guild.id in config.AUTHSERVERS:
        Logger.system(f'Detected unauthorized guild: {guild.name}')
        try:
            await system.send(RauruBot, guild.system_channel.id, f'Unauthorized server detected!\nLeaving unauthorized server: {guild.name}!')
        except:
            Logger.system(f'Unable to send warning message to: {guild.name}')
        await guild.leave()
        Logger.system(f'Unauthorized guild left: {guild.name}')

    return

# Error listeners
@RauruBot.event
async def on_error(event, *args, **kwargs):
    Logger.error(traceback.format_exc())

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
            Logger.config(f'cogs.{cog} loaded')

@RauruBot.command(name='reloadcog', aliases=['rldcog'])
@commands.is_owner()
async def reloadcog(ctx, arg):

    ARG = arg.lower().replace(" ", "")
    ANSWER = ''

    try:
        await RauruBot.reload_extension(f'cogs.{ARG}')
        ANSWER = f'Reloaded Cog: `{arg}`'
        Logger.config(f'cogs.{arg} reloaded by: {ctx.author}')
    except:
        ANSWER = 'Unable to reload Cog!'
        Logger.config(f'cogs.{arg} failed to be reloaded by: {ctx.author}')
    
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
                Logger.config(f'cogs.{cog} reloaded by: {ctx.author}')
            except:
                LOADED = True
                await RauruBot.load_extension(f'cogs.{cog[:-3]}')
                ANSWER2 += cog + '`, `'
                Logger.config(f'cogs.{cog} loaded by: {ctx.author}')
    
    await system.respond(ctx, ANSWER)
    if LOADED:
        await system.respond(ctx, ANSWER2)


system.setactivebot()
RauruBot.run(system.ACTIVEBOTTOKEN)