# dev.py

import discord
from discord.ext import commands
from discord.ext.commands import Greedy
from typing import Literal
import importlib
import system
import messages
import config

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
            
            await system.respond(ctx, f"Synced {len(synced)} commands {'globally' if globally else 'to the current guild.'}")
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
            
        await system.respond(ctx, f"Synced the tree to {ret}/{len(guilds)} guilds.")
        print(system.console_base('System') + f"tree synced to {ret}/{len(guilds)} guilds by: {ctx.author}")
        print(guilds)

    #region Test Commands
    @commands.command(name='msgtest', hidden=True)
    @commands.is_owner()
    async def msgtest(self, ctx):
        embed = discord.Embed(title=None, description=messages.INFO_DUPE121)
        await system.respond(ctx, messages.INFO_RAURUBOT, embed=embed)

    @commands.command(name='commandtest', aliases=['cmdtest'])
    @commands.is_owner()
    async def commandtest(self, ctx):
        async for guild in self.bot.guilds:
            GUILD = f'{guild.name}: {guild.id}'
            print(GUILD)
    #endregion

    #region Speak Commands

    @commands.command(name='spk', aliases=['speak'])
    @commands.is_owner()
    async def speak(self, ctx, *, arg):
        await system.send(self.bot, SPEAKCHANNELID, arg)
        if ctx.channel.id == SPEAKCHANNELID:
            await system.respond(ctx, f'Speaking in channel: {self.bot.get_channel(SPEAKCHANNELID).name}', time=1)
        else:
            await system.respond(ctx, f'Speaking in channel: {self.bot.get_channel(SPEAKCHANNELID).name}')

    @commands.command(name='stspk', aliases=['setspeak'])
    @commands.is_owner()
    async def setspeak(self, ctx, channelid):
        global SPEAKCHANNELID
        try:
            channelid = int(channelid.replace(" ", ""))
            IDUSED = True
        except:
            IDUSED = False

        if IDUSED:
            SPEAKCHANNELID = channelid
        else:
            match channelid:
                case 'totkgen':
                    SPEAKCHANNELID = config.GENSERVERCHANNELID_TGEN
                case 'qc':
                    SPEAKCHANNELID = config.GENSERVERCHANNELID_QC
                case 'botfun':
                    SPEAKCHANNELID = config.GENSERVERCHANNELID_BF

                case _:
                    SPEAKCHANNELID = system.ACTIVEBOTSYSTEMCHANNELID
        if ctx.channel.id == SPEAKCHANNELID:
            await system.respond(ctx, f'Speak channel set: {self.bot.get_channel(SPEAKCHANNELID).name}', time=1)
        else:
            await system.respond(ctx, f'Speak channel set: {self.bot.get_channel(SPEAKCHANNELID).name}')
            
    #endregion

    #region Delete Commands
    @commands.command(name='liststoredmsgs')
    @commands.is_owner()
    async def liststoredmessages(self, ctx):
        print(system.MESSAGEHISTORY)

    @commands.command(name='dellast')
    @commands.is_owner()
    async def deletestoredmessage(self, ctx, arg: int = 1):
        if len(system.MESSAGEHISTORY) == 0:
            await system.respond(ctx, 'No stored messages to delete!')
        
        count = arg
        errors = 0

        while (count > 0):
            count -= 1
            try:
                msginfo = system.MESSAGEHISTORY.pop()
                channel = self.bot.get_channel(msginfo[0])
                message = await channel.fetch_message(msginfo[1])

                await message.delete()
                print(system.console_base('System') + f'Message deleted by: {ctx.author.name}\n\tMessage content: {message.content}\n\tChannel: {channel.name} in {channel.guild.name}')
            except:
                print(system.console_base('Error') + f'Failed to delete message!')
                errors += 1

        print(system.console_base('System') + f'{arg} message(s) deleted by {ctx.author.name}')
        await system.respond(ctx, f'Deleted the last {arg} message(s). {errors} deletions failed.', time=3)

    @commands.command(name='delmsg')
    @commands.is_owner()
    async def deletespecificmessage(self, ctx, messageid, channelid = None):
        messageid = int(messageid.replace(" ", ""))
        if not channelid:
            channelid = ctx.channel.id
        else:
            channelid = int(channelid.replace(" ", ""))
        
        try:
            channel = self.bot.get_channel(channelid)
            message = await channel.fetch_message(messageid)

            await message.delete()
            print(system.console_base('System') + f'Message deleted by: {ctx.author.name}\n\tMessage content: {message.content}\n\tChannel: {channel.name} in {channel.guild.name}')
            await system.respond(ctx, f'Deleted message: {messageid}', time=3)

        except:
            await system.respond(ctx, f'Unable to delete message: {messageid}', time=3)
    #endregion

    #region Managment Commands
    @commands.command(name='shutdown')
    @commands.is_owner()
    async def shutdown(self, ctx):
        try:
            if not ctx.channel.id == system.ACTIVEBOTSYSTEMCHANNELID:
                await system.send(self.bot, system.ACTIVEBOTSYSTEMCHANNELID, f'{self.bot.user.name}' + messages.BOT_OFFLINESIMPLE)
        except:
            print(system.console_base('System') + f'Unable to send Offline Message to channel: {system.ACTIVEBOTSYSTEMCHANNELID}')

        await system.respond(ctx, messages.BOT_OFFLINEPERSON)
        await self.bot.close()
        print(system.console_base('System') + f'{self.bot.user.name} was shutdown by command from: {ctx.author}')
    
    @commands.command(name='profpic')
    @commands.is_owner()
    async def profilepic(self, ctx, arg):
        IMAGENAME = await system.setprofilepic(self.bot, arg)
        await system.respond(ctx, f'Profile picture set to: {IMAGENAME}')

    @commands.command(name='nick')
    @commands.is_owner()
    async def nicknameself(self, ctx, arg):
        USERNAME = await system.setnicknameself(self.bot, arg)
        await system.respond(ctx, f'Nickname set to: {USERNAME}')

    @commands.command(name='status')
    @commands.is_owner()
    async def setstatus(self, ctx, *, arg):
        ANSWER = await system.setstatusself(self.bot, arg)
        await system.respond(ctx, ANSWER)

    @commands.command(name='reloadmodule', aliases=['rldmodule'])
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

        system.setactivebot()
        await system.respond(ctx, ANSWER)
    
    @commands.command(name='toglog')
    @commands.is_owner()
    async def togglelogging(self, ctx):
        if system.ERRORLOGGING == False:
            system.ERRORLOGGING = True
        elif system.ERRORLOGGING == True:
            system.ERRORLOGGING = False

        print(system.console_base('System') + f'Error Logging was set to: {system.ERRORLOGGING} by: {ctx.author}')
        await system.respond(ctx, f'Error Logging now set to {system.ERRORLOGGING}')

    @commands.command(name='listservers')
    @commands.is_owner()
    async def listservers(self, ctx):
        async for guild in self.bot.guilds:
            GUILD = f'{guild.name}: {guild.id}'
            print(GUILD)

    @commands.command(name='leaveunauthserver')
    @commands.is_owner()
    async def leaveunauthservers(self, ctx):
        print('Leaving unauthorized servers....')
        async for guild in self.bot.guilds:
            if not guild.id in config.AUTHSERVERS:
                print(f'Unauthorized server:{guild.name} detected!')
                await guild.leave()
                print(f'Unauthorized server:{guild.name} left!')
        print('All unauthorized servers have been left!')
    #endregion

async def setup(bot):
    await bot.add_cog(Dev(bot))