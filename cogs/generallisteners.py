# generalcalls.py

import discord
from discord.ext import commands
from discord import app_commands
import re
import typing
import system
import messages
from .general import General
from .tag import Tag


class GeneralListeners(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()

    
    @app_commands.command(name='help', description='See what commands I have!')
    @app_commands.check(system.check_banned)
    async def generalhelp(self, interaction: discord.Interaction, *, option: str = '1'):
        if interaction.guild:
            await General.generalhelp(context=interaction, arg=option)
        else:
            await system.respond(interaction, message=messages.ERROR_GUILDONLY)

    
    @commands.command(name='tag')
    @commands.guild_only()
    @commands.check(system.check_banned)
    async def tag(self, ctx, *, arg):
        await Tag.tag(context=ctx, arg=arg)
    
    @app_commands.command(name='tag', description='This is my main command for information! Try using /tag help!')
    @app_commands.check(system.check_banned)
    async def tagslash(self, interaction: discord.Interaction, *, option: str):
        if interaction.guild:
            await Tag.tag(context=interaction, arg=option)
        else:
            await system.respond(interaction, message=messages.ERROR_GUILDONLY)

    
    @commands.command(name='createobjlink', aliases=['createobjectlink', 'find'])
    @commands.guild_only()
    @commands.check(system.check_banned)
    async def objmaplinkcreator(self, ctx, *, arg):
        await General.objmaplinkcreator(context=ctx, arg=arg)

    @app_commands.command(name='find', description='Create an Object Map link with your search terms integrated into it')
    @commands.guild_only()
    @app_commands.check(system.check_banned)
    async def objmaplinkcreatorslash(self, interaction: discord.Interaction, *, searchterms: str):
        if interaction.guild:
            await General.objmaplinkcreator(context=interaction, arg=searchterms)
        else:
            await system.respond(interaction, message=messages.ERROR_GUILDONLY)

    @commands.Cog.listener('on_message')
    async def autoobjmaplinkcreator(self, message):
        pattern = re.compile(r'f\{(.*?)\}')

        ctx = await self.bot.get_context(message)
        if pattern.search(message.content):
            if not message.guild or not system.check_banned(ctx) or message.author.bot:
                return
        else:
            return
        
        matches = pattern.finditer(message.content)
        unique_matches = set()
        for match in matches:
            if len(unique_matches) < 3 and not match == '':
                unique_matches.add(match.group(1))
        
        for TERMS in unique_matches:
            await General.objmaplinkcreator(context=ctx, arg=TERMS)

    
    @commands.command(name='coordconvert')
    @commands.guild_only()
    @commands.check(system.check_banned)
    async def coordconverter(self, ctx, *, arg):
        await General.coordconverter(context=ctx, arg=arg)
    
    @app_commands.command(name='coordconvert', description='Copy the coordinates of an object on the Object Map here to convert them to in-game coords.')
    @commands.guild_only()
    @app_commands.check(system.check_banned)
    async def coordconverterslash(self, interaction: discord.Interaction, *, coordinates: str):
        if interaction.guild:
            await General.coordconverter(context=interaction, arg=coordinates)
        else:
            await system.respond(interaction, message=messages.ERROR_GUILDONLY)

    
    @commands.command(name='findpristine')
    @commands.guild_only()
    @commands.check(system.check_banned)
    async def findpristine(self, ctx, *, arg):
        await General.findpristine(context=ctx, arg=arg)

    @app_commands.command(name='findpristine', description='Create an Object Map link that shows all the Depths Ghosts that can spawn a specific weapon')
    @app_commands.check(system.check_banned)
    async def findpristineslash(self, interaction: discord.Interaction, *, weaponname: str):
        if interaction.guild:
            await General.findpristine(context=interaction, arg=weaponname)
        else:
            await system.respond(interaction, message=messages.ERROR_GUILDONLY)

    @commands.Cog.listener('on_message')
    async def autofindpristine(self, message):
        pattern = re.compile(r'p\{(.*?)\}')

        ctx = await self.bot.get_context(message)
        if pattern.search(message.content):
            if not message.guild or not system.check_banned(ctx) or message.author.bot:
                return
        else:
            return
        
        matches = pattern.finditer(message.content)
        unique_matches = set()
        for match in matches:
            if len(unique_matches) < 3 and not match == '':
                unique_matches.add(match.group(1))
        
        for TERMS in unique_matches:
            await General.findpristine(context=ctx, arg=TERMS)

    
    @commands.command(name='finddispenser', aliases=['dispenser'])
    @commands.guild_only()
    @commands.check(system.check_banned)
    async def finddispenser(self, ctx, *, arg):
        await General.finddispenser(context=ctx, arg=arg)
    
    @app_commands.command(name='finddispenser', description='See which Device Dispensers can dispense a specific Zonai Device capsule')
    @app_commands.check(system.check_banned)
    async def finddispenserslash(self, interaction: discord.Interaction, *, device: str):
        if interaction.guild:
            await General.finddispenser(context=interaction, arg=device)
        else:
            await system.respond(interaction, message=messages.ERROR_GUILDONLY)

    @finddispenserslash.autocomplete('device')
    async def device_autocomplete(self, interaction: discord.Interaction, current: str)-> typing.List[app_commands.Choice[str]]:
        devices = ['Fan', 'Wing', 'Cart', 'Balloon', 'Rocket', 'Time Bomb', 'Portable Pot', 'Flame Emitter', 'Frost Emitter', 'Shock Emitter', 'Beam Emitter', 'Hydrant', 'Steering Stick', 'Big Wheel', 'Small Wheel', 'Sled', 'Battery', 'Big Battery', 'Spring', 'Cannon', 'Stabilizer', 'Hover Stone', 'Light', 'Stake', 'Mirror', 'Homing Cart', 'Construct Head']
        data = []
        if not current == "":
            for choice in devices:
                    if current.lower().replace(" ", "") in choice.lower().replace(" ", ""):
                        data.append(app_commands.Choice(name=choice, value=choice))
        return data

    @commands.Cog.listener('on_message')
    async def autofinddispenser(self, message):
        pattern = re.compile(r'd\{(.*?)\}')

        ctx = await self.bot.get_context(message)
        MATCH = pattern.search(message.content)
        if MATCH and not MATCH == '':
            if not message.guild or not system.check_banned(ctx) or message.author.bot:
                return
            else:
                await General.finddispenser(context=ctx, arg=MATCH.group(1))


    @commands.command(name='hi', aliases=['hello', 'howdy', 'hola', 'aloha', 'bonjour', 'ciao', 'greetings', 'g\'day', 'yo', 'konichiwa', 'hallo', 'salutations'])
    @commands.guild_only()
    @commands.check(system.check_banned)
    async def hello(self, ctx):
        await General.hello(ctx)

    @app_commands.command(name='hi')
    @app_commands.check(system.check_banned)
    async def helloslash(self, interaction: discord.Interaction):
        if interaction.guild:
            await General.hello(interaction)
        else:
            await system.respond(interaction, message=messages.ERROR_GUILDONLY)
    
    @commands.command(name='thanks', aliases=['thankyou', 'gracias', 'merci', 'tysm', 'mahalo', 'ty', 'danke', 'grazie', 'arigato', 'thx'])
    @commands.guild_only()
    @commands.check(system.check_banned)
    async def thanks(self, ctx):
        await General.thanks(ctx)
    
    @app_commands.command(name='thanks')
    @app_commands.check(system.check_banned)
    async def thanksslash(self, interaction: discord.Interaction):
        if interaction.guild:
            await General.thanks(interaction)
        else:
            await system.respond(interaction, message=messages.ERROR_GUILDONLY)

async def setup(bot):
    await bot.add_cog(GeneralListeners(bot))