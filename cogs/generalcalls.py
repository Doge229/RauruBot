# generalcalls.py
import discord
from discord.ext import commands
from discord import app_commands
import system
import tag
import general

class General2(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()
    
    @commands.command(name='tag')
    @commands.guild_only()
    @commands.check(system.check_banned)
    async def tag(self, ctx, *, arg):
        await tag.tag(context=ctx, arg=arg)
    
    @app_commands.command(name='tag', description='This is my main command for information! Try using /tag help!')
    @app_commands.check(system.slashcheck_banned)
    async def tagslash(self, interaction: discord.Interaction, *, option: str):
        await tag.tag(context=interaction, arg=option)

    
    @commands.command(name='createobjlink', aliases=['createobjectlink', 'find'])
    @commands.guild_only()
    @commands.check(system.check_banned)
    async def objmaplinkcreator(self, ctx, *, arg):
        await general.objmaplinkcreator(context=ctx, arg=arg)

    @app_commands.command(name='find', description='Create an Object Map link with your search terms integrated into it')
    @commands.guild_only()
    @app_commands.check(system.slashcheck_banned)
    async def objmaplinkcreatorslash(self, interaction: discord.Interaction, *, searchterms: str):
        await general.objmaplinkcreator(context=interaction, arg=searchterms)

    
    @commands.command(name='coordconvert')
    @commands.guild_only()
    @commands.check(system.check_banned)
    async def coordconverter(self, ctx, *, arg):
        await general.coordconverter(context=ctx, arg=arg)
    
    @app_commands.command(name='coordconvert', description='Copy the coordinates of an object on the Object Map here to convert them to in-game coords.')
    @commands.guild_only()
    @app_commands.check(system.slashcheck_banned)
    async def coordconverterslash(self, interaction: discord.Interaction, *, coordinates: str):
        await general.coordconverter(context=interaction, arg=coordinates)

    
    @commands.command(name='findpristine')
    @commands.guild_only()
    @commands.check(system.check_banned)
    async def findpristine(self, ctx, *, arg):
        await general.findpristine(context=ctx, arg=arg)

    @app_commands.command(name='findpristine', description='Create an Object Map link that shows all the Depths Ghosts that can spawn a specific weapon')
    @commands.guild_only()
    @app_commands.check(system.slashcheck_banned)
    async def findpristineslash(self, interaction: discord.Interaction, *, weaponname: str):
        await general.findpristine(context=interaction, arg=weaponname)

    
    @commands.command(name='finddispenser', aliases=['dispenser'])
    @commands.guild_only()
    @commands.check(system.check_banned)
    async def finddispenser(self, ctx, *, arg):
        await general.finddispenser(context=ctx, arg=arg)
    
    @app_commands.command(name='finddispenser', description='See which Device Dispensers can dispense a specific Zonai Device capsule')
    @commands.guild_only()
    @app_commands.check(system.slashcheck_banned)
    async def finddispenserslash(self, interaction: discord.Interaction, *, device: str):
        await general.finddispenser(context=interaction, arg=device)

async def setup(bot):
    await bot.add_cog(General2(bot))