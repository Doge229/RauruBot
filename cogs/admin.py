# admin.py
from discord.ext import commands
import system
import messages
import config

class Admin(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()

    @commands.command(name='shutdown')
    @commands.guild_only()
    @commands.check(system.check_admin)
    async def shutdown(self, ctx):
    
        try:
            channel = self.bot.get_channel(system.ACTIVEBOTSYSTEMCHANNELID)
            if not ctx.channel.id == system.ACTIVEBOTSYSTEMCHANNELID:
                await channel.send(messages.BOT_OFFLINESIMPLE)
        except:
            print(system.console_base('System') + f'Unable to send Offline Message to channel: {system.ACTIVEBOTSYSTEMCHANNELID}')

        await ctx.send(messages.BOT_OFFLINEPERSON)
        await self.bot.close()
        print(system.console_base('System') + f'{self.bot.user.name} was shutdown by command from: {ctx.author}')

    @commands.command(name='blacklist')
    @commands.guild_only()
    @commands.check(system.check_admin)
    async def blacklist(self, ctx, mode, target=None, *reason):
        ANSWER = ''

        if mode == 'show':
            BLACKLIST = ''
            for key in system.DICT_BLACKLIST:
                BLACKLIST += f'\nUser: `{key}`, Reason: `{system.DICT_BLACKLIST[key]}`'

            ANSWER = 'Here are the currently blacklisted users:' + BLACKLIST
            await ctx.send(ANSWER)
            print(system.console_base('Blacklist') + f'Blacklist shown by Admin: {ctx.author}')
            return

        try:
            target = str(int(target))
        except:
            await ctx.send(messages.ERROR_BLACKLIST)
            return



        if mode == 'add':
            if not target in system.DICT_BLACKLIST:
                system.DICT_BLACKLIST[target] = reason
                ANSWER = f'User: `{target}` added to blacklist. Reason: `{reason}`'
                print(system.console_base('Blacklist') + f'User: {target} added to blacklist by: {ctx.author}. Reason: {reason}')
                system.save_blacklist()
            else:
                ANSWER = f'User: `{target}` already blacklisted. Reason: `{system.DICT_BLACKLIST[target]}`'
                print(system.console_base('Blacklist') + f'Admin: {ctx.author} attempted to re-blacklist user: {target}. Reason: {reason}')

        elif mode == 'remove':
            if target in system.DICT_BLACKLIST:
                del system.DICT_BLACKLIST[target]
                ANSWER = f'User: `{target}` removed from blacklist.'
                print(system.console_base('Blacklist') + f'User: {target} removed from blacklist by: {ctx.author}. Reason: {reason}')
                system.save_blacklist()
            else:
                ANSWER = f'User: `{target}` not in blacklist.'
                print(system.console_base('Blacklist') + f'Admin: {ctx.author} attempted to remove non-blacklisted user: {target}. Reason: {reason}')

        elif mode == 'update':
            if target in system.DICT_BLACKLIST:
                system.DICT_BLACKLIST[target] = reason
                ANSWER = f'User: `{target}` blacklist reason updated. Reason: `{reason}`'
                print(system.console_base('Blacklist') + f'User: {target} blacklist reason updated by: {ctx.author}. Reason: {reason}')
                system.save_blacklist()
            else:
                ANSWER = f'User: `{target}` not in blacklist.'
                print(system.console_base('Blacklist') + f'Admin: {ctx.author} attempted to update non-blacklisted user: {target}. Reason: {reason}')

        else:
            ANSWER = messages.ERROR_BLACKLIST

        await ctx.send(ANSWER)

    @commands.command(name='blacklisthelp')
    @commands.guild_only()
    @commands.check(system.check_admin)
    async def blacklisthelp(self, ctx):
        await ctx.send(messages.HELP_BLACKLIST)

    
async def setup(bot):
    await bot.add_cog(Admin(bot))