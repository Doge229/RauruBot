# generalslash.py

import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Greedy
import system
import messages
import random


class generalslash(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()

    @app_commands.command(name='help', description='See what commands I have!')
    @commands.guild_only()
    @app_commands.check(system.slashcheck_banned)
    async def helpgeneral(self, interaction: discord.Interaction, option: str = '1'):
        ANSWER = ''
        EPHEMERAL = False

        arg = option.lower().replace("s ", "")
        arg = arg.replace(" ", "")
        if arg[-1] == 's':
            arg = arg[:-1]
        
        match arg:
            case '':
                EPHEMERAL = True
                ANSWER = messages.HELP_GENERAL
            case '1':
                EPHEMERAL = True
                ANSWER = messages.HELP_GENERAL
            case 'show':
                ANSWER = messages.HELP_GENERAL
            case 'show1':
                ANSWER = messages.HELP_GENERAL
            case 'showpage1':
                ANSWER = messages.HELP_GENERAL
            
            case _:
                ANSWER = messages.ERROR_UNKNOWNCMD
        
        await interaction.response.send_message(ANSWER, ephemeral=EPHEMERAL)

async def setup(bot):
    await bot.add_cog(generalslash(bot))