# infoslash.py

import os
import discord
from discord.ext import commands
from discord import app_commands
import system
import messages
import config

class infoslash(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()
    
    @app_commands.command(name='info', description='This is my command for server-specific information. Use /info help')
    @app_commands.guilds(discord.Object(config.DEVSERVERID), discord.Object(config.GENSERVERID))
    @app_commands.check(system.slashcheck_banned)
    async def infoslash1(self, interaction: discord.Interaction, *, option: str):
        ANSWER = ''
        IMAGEPATH = ''

        EPHEMERAL = False

        arg = option.lower().replace("s ", "")
        arg = arg.replace(" ", "")
        if arg[-1] == 's':
            arg = arg[:-1]

        match arg:
            case 'help':
                EPHEMERAL = True
                ANSWER = messages.HELP_INFO_GENERALSERVER
            case 'help1':
                EPHEMERAL = True
                ANSWER = messages.HELP_INFO_GENERALSERVER
            case 'helppage1':
                EPHEMERAL = True
                ANSWER = messages.HELP_INFO_GENERALSERVER
            case 'showhelp':
                ANSWER = messages.HELP_INFO_GENERALSERVER
            case 'showhelp1':
                ANSWER = messages.HELP_INFO_GENERALSERVER
            case 'showhelppage1':
                ANSWER = messages.HELP_INFO_GENERALSERVER


            case 'userauru':
                ANSWER = messages.INFO_USERAURU
            case 'imageperm':
                ANSWER = messages.HELP_IMGPERM
            case 'imgperm':
                ANSWER = messages.HELP_IMGPERM
            case 'spoiler':
                ANSWER = messages.HELP_SPOILERTAG
            case 'totkexpert':
                ANSWER = messages.HELP_EXPERTROLE
            case 'rule913':
                ANSWER = messages.HELP_RULE913
            case 'piracy':
                ANSWER = messages.HELP_RULE913
            case 'to':
                ANSWER = messages.HELP_RULE913

            case _:
                ANSWER = messages.ERROR_UNKNOWNCMD
            
        if not IMAGEPATH == '':
            IMAGE = discord.File(IMAGEPATH)
            await interaction.response.send_message(ANSWER, file=IMAGE)
        else:
            await interaction.response.send_message(ANSWER, ephemeral=EPHEMERAL)


async def setup(bot):
    await bot.add_cog(infoslash(bot))