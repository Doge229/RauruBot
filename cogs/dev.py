# dev.py

import discord
from discord.ext import commands
from discord.ext.commands import Greedy
from typing import Literal
import importlib
import system
import messages
import config

LASTMESSAGEID = None
SPEAKCHANNELID = system.ACTIVEBOTSYSTEMCHANNELID


class Dev(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def sync(self, ctx, mode: Literal["*", "*^", ">", "~", "~^"], guilds: Greedy[discord.Object]):
        tree = self.bot.tree
        globally = True

        if not guilds:
            #Sync to global tree
            if mode == "*":
                synced = await tree.sync()
            #Clear commands and sync to global tree
            elif mode == "*^":
                tree.clear_commands(guild=None)
                synced = await tree.sync()
            #Copy global to guild tree and sync to guild tree
            elif mode == ">":
                tree.copy_global_to(guild=ctx.guild)
                synced = await tree.sync(guild=ctx.guild)
                globally = False
            #Sync guild-specific commands and sync to guild tree
            elif mode == "~":
                synced = await tree.sync(guild=ctx.guild)
                globally = False
            #Clear guild-specific commands and sync to guild tree
            elif mode == "~^":
                tree.clear_commands(guild=ctx.guild)
                synced = await tree.sync(guild=ctx.guild)
                globally = False
            
            await ctx.send(f"Synced {len(synced)} commands {'globally' if globally else 'to the current guild.'}")
            print(system.console_base('System') + f"{len(synced)} commands synced {'globally' if globally else f'to {ctx.guild}.'} by: {ctx.author}")
            return


        #Copy global to guild tree and sync to guild tree
        if mode == ">":
            ret = 0
            for guild in guilds:
                try:
                    tree.copy_global_to(guild=guild)
                    await tree.sync(guild=guild)
                except discord.HTTPException:
                    pass
                else:
                    ret += 1
        #Sync guild-specific commands and sync to guild tree
        elif mode == "~":
            ret = 0
            for guild in guilds:
                try:
                    await tree.sync(guild=guild)
                except discord.HTTPException:
                    pass
                else:
                    ret += 1
        #Clear guild-specific commands and sync to guild tree
        elif mode == "~^":
            ret = 0
            for guild in guilds:
                try:
                    tree.clear_commands(guild=guild)
                    await tree.sync(guild=guild)
                except discord.HTTPException:
                    pass
                else:
                    ret += 1
            
        await ctx.send(f"Synced the tree to {ret}/{len(guilds)} guilds.")
        print(system.console_base('System') + f"tree synced to {ret}/{len(guilds)} guilds by: {ctx.author}")
        print(guilds)

    #region Test Commands
    @commands.command(name='msgtest', hidden=True)
    @commands.guild_only()
    @commands.is_owner()
    async def msgtest(self, ctx):
        await ctx.send(messages.BOT_INFO)

    @commands.command(name='commandtest', aliases=['cmdtest'])
    @commands.guild_only()
    @commands.is_owner()
    async def commandtest(self, ctx):
        async for guild in self.bot.fetch_guilds(limit=150):
            GUILD = f'{guild.name}: {guild.id}'
            print(GUILD)
    #endregion

    #region Speak Commands

    @commands.command(name='spk', aliases=['speak'])
    @commands.dm_only()
    @commands.is_owner()
    async def speak(self, ctx, *, arg):
        global LASTMESSAGEID
        channel = self.bot.get_channel(SPEAKCHANNELID)

        await ctx.send(f'Speaking in channel: {SPEAKCHANNELID}')
        msg = await channel.send(arg)
        LASTMESSAGEID = msg.id

    @commands.command(name='stspk', aliases=['setspeak'])
    @commands.dm_only()
    @commands.is_owner()
    async def setspeak(self, ctx, arg):
        global SPEAKCHANNELID
        SPEAKCHANNELID = int(arg.replace(" ", ""))
        await ctx.send(f'Speak Channel Set: {SPEAKCHANNELID}')

    @commands.command(name='stspk2', aliases=['setspeak2'])
    @commands.dm_only()
    @commands.is_owner()
    async def setspeak2(self, ctx, arg):
        global SPEAKCHANNELID

        match arg:
            case 'totkgen':
                SPEAKCHANNELID = config.GENSERVERCHANNELID_TGEN
            case 'qc':
                SPEAKCHANNELID = config.GENSERVERCHANNELID_QC
            case 'botfun':
                SPEAKCHANNELID = config.GENSERVERCHANNELID_BF

            case _:
                SPEAKCHANNELID = system.ACTIVEBOTSYSTEMCHANNELID

        await ctx.send(f'Speak Channel Set: {SPEAKCHANNELID}')
    #endregion

    #region Delete Commands
    @commands.command(name='deletemessage', aliases=['delmsg'])
    @commands.is_owner()
    async def deletemessage(self, ctx, arg, arg2):

        channel = self.bot.get_channel(int(arg.replace(" ", "")))
        
        message = await channel.fetch_message(int(arg2.replace(" ", "")))

        await message.delete()
        print(system.console_base('System') + f'Message was deleted by: {ctx.author}\n\tMessage: {message}')
    
    @commands.command(name='deletemessage2', aliases=['delmsg2'])
    @commands.is_owner()
    async def deletemessage2(self, ctx, arg):
        
        message = await ctx.channel.fetch_message(int(arg.replace(" ", "")))

        await message.delete()
        print(system.console_base('System') + f'Message was deleted by: {ctx.author}\n\tMessage: {message}')

    @commands.command(name='deletelastmessage', aliases=['dellast'])
    @commands.is_owner()
    async def deletelastmessage(self, ctx):
        global LASTMESSAGEID
        if LASTMESSAGEID == None:
            await ctx.send('Last message not found!')
            return

        channel = self.bot.get_channel(SPEAKCHANNELID)
        message = await channel.fetch_message(LASTMESSAGEID)

        await message.delete()
        print(system.console_base('System') + f'Last message was deleted by: {ctx.author}\n\tMessage: {message}')

    #endregion

    #region Managment Commands
    @commands.command(name='reloadmodule', aliases=['rldmodule'])
    @commands.guild_only()
    @commands.is_owner()
    async def reloadmodule(self, ctx, arg):

        ARG = arg.replace(" ", "")
        MODULE = None
        ANSWER = ''

        match ARG:
            case 'system':
                MODULE = system
            case 'messages':
                MODULE = messages
            case 'config':
                MODULE = config
        
        try:
            importlib.reload(MODULE)
            ANSWER = f'Reloaded Module: `{arg}`'
            print(system.console_base('System') + f'Module: {arg} reloaded by: {ctx.author}')
        except:
            ANSWER = 'Unable to reload Module!'
            print(system.console_base('System') + f'Module: {arg} failed to be reloaded by: {ctx.author}')

        await ctx.send(ANSWER)
    
    @commands.command(name='toglog')
    @commands.is_owner()
    async def togglelogging(self, ctx):
        if system.ERRORLOGGING == False:
            system.ERRORLOGGING = True
        elif system.ERRORLOGGING == True:
            system.ERRORLOGGING = False

        print(system.console_base('System') + f'Error Logging was set to: {system.ERRORLOGGING} by: {ctx.author}')
        await ctx.send(f'Error Logging now set to {system.ERRORLOGGING}')

    @commands.command(name='listservers')
    @commands.guild_only()
    @commands.is_owner()
    async def listservers(self, ctx):
        async for guild in self.bot.fetch_guilds(limit=150):
            GUILD = f'{guild.name}: {guild.id}'
            print(GUILD)

    @commands.command(name='leaveunauthserver')
    @commands.guild_only()
    @commands.is_owner()
    async def leaveunauthservers(self, ctx):
        print('Leaving unauthorized servers....')
        async for guild in self.bot.fetch_guilds(limit=150):
            if not guild.id in config.AUTHSERVERS:
                print(f'Unauthorized server:{guild.name} detected!')
                await guild.leave()
                print(f'Unauthorized server:{guild.name} left!')
        print('All unauthorized servers have been left!')
    #endregion

async def setup(bot):
    await bot.add_cog(Dev(bot))