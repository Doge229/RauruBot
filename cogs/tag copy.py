# tag.py
import os
import discord
from discord.ext import commands
import system
import messages
import tagtest

class Tag2(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()
    
    @commands.command(name='msgtest2')
    @commands.guild_only()
    @commands.is_owner()
    async def msgtest(self, ctx, *, arg):
        await tagtest.tag2(ctx=ctx, arg=arg)

async def setup(bot):
    await bot.add_cog(Tag2(bot))