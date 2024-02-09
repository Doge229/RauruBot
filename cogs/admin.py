# admin.py

from discord.ext import commands
import system
import messages
from logger import Logger


class Admin(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()


    @commands.command(name='blacklist')
    @commands.guild_only()
    @commands.check(system.check_admin)
    async def blacklist(self, ctx, mode, target = None, *reason: str):
        ANSWER = ''
        mode = mode.lower().replace(" ", "")
        BLACKLISTENTRY = {}
        # clean up the reason and account for no given reason
        reason = str(reason).replace("(", "").replace(")", "")
        if reason == "":
            reason = "N/A"


        if mode == 'show':
            if len(system.DICT_BLACKLIST) == 0:
                ANSWER = 'There are no currently blacklisted users.'
                await system.respond(ctx, ANSWER)
                Logger.admin(f'Blacklist shown by Admin: {ctx.author.name}')
                return

            BLACKLIST = ''
            for key in system.DICT_BLACKLIST:
                BLACKLIST += f'\nUser: `{system.DICT_BLACKLIST[key]["name"]}`, Server: `{system.DICT_BLACKLIST[key]["guild"]}`, Reason: `{system.DICT_BLACKLIST[key]["reason"]}`'

            ANSWER = 'Here are the currently blacklisted users:' + BLACKLIST
            await system.respond(ctx, ANSWER)
            Logger.admin(f'Blacklist shown by Admin: {ctx.author.name}')
            return
        
        # Setup entry
        try:
            TARGET = await self.bot.fetch_user(target)
            BLACKLISTENTRY = {
                "name": str(TARGET.name),
                "id": str(TARGET.id),
                "guild": ctx.guild.name,
                "guildid": str(ctx.guild.id),
                "reason": reason,
                "admin": ctx.author.name
            }
        except:
            await system.respond(ctx, messages.ERROR_BLACKLIST)
            return
        
        ENTRYNAME = BLACKLISTENTRY["id"]+BLACKLISTENTRY["guildid"]
        TARGETNAME = BLACKLISTENTRY["name"]
        GUILDNAME = BLACKLISTENTRY["guild"]
        REASON = BLACKLISTENTRY["reason"]
        ADMIN = BLACKLISTENTRY["admin"]
        
        

        if mode == 'add':
            if not ENTRYNAME in system.DICT_BLACKLIST:
                system.DICT_BLACKLIST[ENTRYNAME] = BLACKLISTENTRY
                ANSWER = f'User: `{TARGETNAME}` added to blacklist for server: `{GUILDNAME}`. Reason: `{REASON}`'
                Logger.admin(f'User: {TARGETNAME} added to blacklist for guild: {GUILDNAME} by Admin: {ADMIN}. Reason: {REASON}')
                system.save_blacklist()
            else:
                ANSWER = f'User: `{TARGETNAME}` already blacklisted for this server. Reason: `{system.DICT_BLACKLIST[ENTRYNAME]["reason"]}`'
                Logger.admin(f'Admin: {ADMIN} attempted to re-blacklist user: {TARGETNAME} for guild: {GUILDNAME}. Reason: {REASON}')

        elif mode == 'remove':
            if ENTRYNAME in system.DICT_BLACKLIST:
                del system.DICT_BLACKLIST[ENTRYNAME]
                ANSWER = f'User: `{TARGETNAME}` removed from blacklist for server: `{GUILDNAME}`.'
                Logger.admin(f'User: {TARGETNAME} removed from blacklist by: {ADMIN}.')
                system.save_blacklist()
            else:
                ANSWER = f'User: `{TARGETNAME}` not in blacklist for this server.'
                Logger.admin(f'Admin: {ADMIN} attempted to remove non-blacklisted user: {TARGETNAME}.')

        elif mode == 'update':
            if ENTRYNAME in system.DICT_BLACKLIST:
                system.DICT_BLACKLIST[ENTRYNAME] = BLACKLISTENTRY
                ANSWER = f'User: `{TARGETNAME}` blacklist reason for server: {GUILDNAME} updated. Reason: `{REASON}`'
                Logger.admin(f'User: {TARGETNAME} blacklist reason for guild: {GUILDNAME} updated by: {ADMIN}. Reason: {REASON}')
                system.save_blacklist()
            else:
                ANSWER = f'User: `{TARGETNAME}` not in blacklist for server: {GUILDNAME}.'
                Logger.admin(f'Admin: {ADMIN} attempted to update non-blacklisted user: {TARGETNAME}. Reason: {REASON}')

        else:
            ANSWER = messages.ERROR_BLACKLIST

        await system.respond(ctx, ANSWER)

    @commands.command(name='blacklisthelp')
    @commands.guild_only()
    @commands.check(system.check_admin)
    async def blacklisthelp(self, ctx):
        await system.respond(ctx, messages.HELP_BLACKLIST)

    
async def setup(bot):
    await bot.add_cog(Admin(bot))