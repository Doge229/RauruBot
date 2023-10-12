# errorhandler.py

import discord
from discord.ext import commands
from discord import app_commands
import system
import messages
import config

class ErrorHandler(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send(messages.ERROR_NODM)

        elif isinstance(error, commands.errors.CheckFailure):
            await ctx.send(messages.ERROR_BADROLE)

        elif isinstance(error, commands.MissingRequiredArgument):
            if str(ctx.command) == 'blacklist':
                await ctx.send(messages.ERROR_BLACKLIST)
            else:
                await ctx.send(messages.ERROR_UNKNOWNCMD)
            
        elif system.ERRORLOGGING == True:
            print(error)
    
    @commands.Cog.listener()
    async def on_app_command_error(self, interaction, error):
        print('test')
        if isinstance(error, app_commands.NoPrivateMessage):
            await interaction.reponse.send_message(messages.ERROR_NODM)

        elif isinstance(error, app_commands.CheckFailure):
            await interaction.reponse.send_message(messages.ERROR_BADROLE)
            
        elif system.ERRORLOGGING == True:
            print(error)

async def setup(bot):
    await bot.add_cog(ErrorHandler(bot))