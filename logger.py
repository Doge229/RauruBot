# logger.py

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

class Logger():
    def __init__(self) -> None:
        pass

    def getlogdate():
        return f'{datetime.date.today()}'

    def getlogdatetime():
        dt = datetime.datetime.today()

        return f'{dt:%m-%d %I:%M:%S}'
    
    @classmethod
    def log(self, type, msg):

        if not os.path.exists(system.DIR_LOGS):
            os.mkdir(system.DIR_LOGS)

        PADDING = 9
        LINE = f'|{type:<{PADDING}}|{self.getlogdatetime()}| {msg}'
        DIR_CURRENTLOG = os.path.join(system.DIR_LOGS, f'{self.getlogdate()}.txt')
        log = open(DIR_CURRENTLOG, "a")

        log.write(LINE + '\n')
        print(LINE)

        log.close()
    

    @classmethod
    def error(self, msg):
        self.log("Error", msg)

    @classmethod
    def system(self, msg):
        self.log("System", msg)

    @classmethod
    def config(self, msg):
        self.log("Config", msg)

    @classmethod
    def admin(self, msg):
        self.log("Admin", msg)

    @classmethod
    def info(self, msg):
        self.log("Info", msg)