# dailyprofile.py

import os
import datetime
import pytz
import inspect
import discord
from discord.ext import commands, tasks
from discord import app_commands
import messages
import system
import config
import json
import random
import asyncio

timezone = datetime.timezone(datetime.timedelta(hours=-6))
times = [
    datetime.time(hour=8, minute=00, tzinfo=timezone),
    datetime.time(hour=16, minute=00, tzinfo=timezone),
    datetime.time(hour=00, minute=00, tzinfo=timezone)
]

class DailyProfile(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()
        self.testtimer.start()

    def cog_unload(self):
        self.testtimer.cancel()
    
    @tasks.loop(time=times)
    async def testtimer(self):
        int = random.randint(1, 100)
        CHOICE = 'default'

        if int == 1:
            CHOICE = 'funny'
        elif int > 51:
            CHOICE = 'pride'

        await system.setprofilepic(self.bot, CHOICE)
         

async def setup(bot):
    await bot.add_cog(DailyProfile(bot))