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
        NICKCHOICE = 'default'
        PICCHOICE = 'default'

        if int == 1:
            PICCHOICE = 'funny'
        elif int == 2:
            NICKCHOICE == 'cursed'
            PICCHOICE == 'cursed'
        elif int > 51:
            PICCHOICE = 'pride'

        await system.setnicknameself(self.bot, NICKCHOICE)
        await system.setprofilepic(self.bot, PICCHOICE)
         

async def setup(bot):
    await bot.add_cog(DailyProfile(bot))