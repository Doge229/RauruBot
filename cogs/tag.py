# tag.py

import os
import discord
from discord.ext import commands
import system
import messages
import config


class Tag(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()

    async def tag(context, arg):
        ANSWER = ''
        IMAGE = None
        EPHEMERAL = False

        arg = system.argcleanup(arg)

        match arg:
            case 'botinfo':
                ANSWER = messages.INFO_RAURUBOT
            case 'userauru':
                ANSWER = messages.INFO_RAURUBOT

            # region General Help Stuff
            case 'helpgeneral':
                EPHEMERAL = True
                ANSWER = messages.HELP_GENERAL
            case 'helpgeneral1':
                EPHEMERAL = True
                ANSWER = messages.HELP_GENERAL
            case 'helpgeneralshow':
                ANSWER = messages.HELP_GENERAL
            case 'helpgeneralshow1':
                ANSWER = messages.HELP_GENERAL
            # endregion

            # region Tag Help Stuff
            case 'help':
                EPHEMERAL = True
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.HELP_TAGBASE + messages.HELP_GENSERVERTAGS + messages.HELP_TAG1
                else:
                    ANSWER = messages.HELP_TAGBASE + messages.HELP_TAG1
            case 'help1':
                EPHEMERAL = True
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.HELP_TAGBASE + messages.HELP_GENSERVERTAGS + messages.HELP_TAG1
                else:
                    ANSWER = messages.HELP_TAGBASE + messages.HELP_TAG1
            case 'helppage1':
                EPHEMERAL = True
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.HELP_TAGBASE + messages.HELP_GENSERVERTAGS + messages.HELP_TAG1
                else:
                    ANSWER = messages.HELP_TAGBASE + messages.HELP_TAG1
            case 'helpshow':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.HELP_TAGBASE + messages.HELP_GENSERVERTAGS + messages.HELP_TAG1
                else:
                    ANSWER = messages.HELP_TAGBASE + messages.HELP_TAG1
            case 'helpshow1':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.HELP_TAGBASE + messages.HELP_GENSERVERTAGS + messages.HELP_TAG1
                else:
                    ANSWER = messages.HELP_TAGBASE + messages.HELP_TAG1
            case 'helpshowpage1':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.HELP_TAGBASE + messages.HELP_GENSERVERTAGS + messages.HELP_TAG1
                else:
                    ANSWER = messages.HELP_TAGBASE + messages.HELP_TAG1
                
            # endregion

            # region General Server Stuff
            case 'imageperm':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.HELP_IMGPERM
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'imgperm':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.HELP_IMGPERM
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'spoiler':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.HELP_SPOILERTAG
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'totkexpert':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.HELP_EXPERTROLE
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'rule913':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.HELP_RULE913
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'piracy':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.HELP_RULE913
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'to':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.HELP_RULE913
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            # endregion

            # region Story Stuff
            case 'postgame':
                ANSWER = messages.INFO_POSTGAME
            case 'permaquest':
                ANSWER = messages.INFO_PERMQUESTS
            case 'permquest':
                ANSWER = messages.INFO_PERMQUESTS
            case 'elitepic':
                ANSWER = messages.INFO_ELITEPIC
            case 'ringruin':
                ANSWER = messages.INFO_RINGRUINQUEST
            case 'josha':
                ANSWER = messages.INFO_JOSHA
            case 'trueend':
                ANSWER = messages.INFO_TRUEEND
            # endregion

            # region Farming Stuff
            case 'bloodmoon':
                ANSWER = messages.INFO_BLOODMOON
            case 'forcebloodmoon':
                ANSWER = messages.POINT_FORCEMOON
            case 'materialrespawn':
                ANSWER = messages.INFO_MATERIALTIMER
            case 'materialtimer':
                ANSWER = messages.INFO_MATERIALTIMER
            case 'shoprestock':
                ANSWER = messages.INFO_SHOPRESTOCK
            case 'chargefarm':
                ANSWER = messages.INFO_CHARGEFARM
            case 'starfragment':
                ANSWER = messages.POINT_STARFARM
            case 'dragon':
                ANSWER = messages.POINT_DRAGON
            case 'earlyrupee':
                ANSWER = messages.POINT_EARLYCASH
            # endregion

            # region Durability
            case 'octorok':
                ANSWER = messages.INFO_OCTOROK
            case 'repairlegendary':
                ANSWER = messages.INFO_REPAIRLEGEND
            case 'repairlegend':
                ANSWER = messages.INFO_REPAIRLEGEND
            case 'legendarylist':
                ANSWER = messages.INFO_LEGENDLIST
            case 'legendlist':
                ANSWER = messages.INFO_LEGENDLIST
            case 'fusedurability':
                ANSWER = messages.INFO_FUSEDURABILITY
            case 'fusedura':
                ANSWER = messages.INFO_FUSEDURABILITY
            case 'pristine':
                ANSWER = messages.POINT_WEAPONSINTACT
            case 'pristineweapon':
                ANSWER = messages.POINT_WEAPONSINTACT
            # endregion

            # region Mechanics and Hints
            case 'mastersword':
                ANSWER = messages.INFO_MASTERSWORD
            case 'cherry':
                ANSWER = messages.INFO_CHERRYTREE
            case 'cherrytree':
                ANSWER = messages.INFO_CHERRYTREE
            case 'bargainer':
                ANSWER = messages.INFO_BARGAINERSTATUE
            case 'bargainerstatue':
                ANSWER = messages.INFO_BARGAINERSTATUE
            case 'amiiborespawnalt':
                ANSWER = messages.INFO_ALTAMIIBOWEAPONSOURCE
            case 'duskbow':
                ANSWER = messages.INFO_ALTAMIIBOWEAPONSOURCE
            case 'whitesword':
                ANSWER = messages.INFO_ALTAMIIBOWEAPONSOURCE
            case 'botwdata':
                ANSWER = messages.INFO_BOTWDATA
            case 'coordsystem':
                ANSWER = messages.INFO_COORDSYSTEM
            case 'depthmirror':
                ANSWER = messages.INFO_DEPTHSMIRROR
            case 'depthsmirror':
                ANSWER = messages.INFO_DEPTHSMIRROR
            case 'deviceshop':
                ANSWER = messages.INFO_DEVICESHOP
            case 'ritofabric':
                ANSWER = messages.INFO_RITOFABRIC
            case 'hornedstatue':
                ANSWER = messages.INFO_HORNEDSTATUE
            case 'hornedone':
                ANSWER = messages.INFO_HORNEDSTATUE
            case 'mat253':
                ANSWER = messages.INFO_SUNPUMPKIN
            case 'sunpumpkin':
                ANSWER = messages.INFO_SUNPUMPKIN
            case 'elementaldamage':
                ANSWER = messages.INFO_BASEELEMENTALDMG
            case 'elementdmg':
                ANSWER = messages.INFO_BASEELEMENTALDMG
            case 'missablelocation':
                ANSWER = messages.INFO_MISSABLELOCATIONS
            case 'midairwing':
                ANSWER = messages.INFO_MIDAIRWING
            case 'truedmg':
                ANSWER = messages.INFO_TRUEDAMAGE
            case 'truedamage':
                ANSWER = messages.INFO_TRUEDAMAGE
            case 'botwarmor':
                ANSWER = messages.INFO_MISSINGARMOR
            case 'missingarmor':
                ANSWER = messages.INFO_MISSINGARMOR
            case 'control5':
                ANSWER = messages.INFO_JSCONTROL
            case 'jumpslash':
                ANSWER = messages.INFO_JSCONTROL
            case 'moatchasm':
                ANSWER = messages.INFO_MOATCHASM
            case 'breakitdown':
                ANSWER = messages.INFO_BREAKITDOWN
            case 'breakapart':
                ANSWER = messages.INFO_BREAKITDOWN
            case 'pelison':
                ANSWER = messages.INFO_BREAKITDOWN
            case 'gleeokstrat':
                ANSWER = messages.INFO_GLEEOKSTRAT
            case 'dugby':
                ANSWER = messages.INFO_DUGBY
            # endregion

            # region Effects and Builds
            case 'defense':
                ANSWER = messages.INFO_DEFENSESTAT
            case 'bestarmor':
                ANSWER = messages.INFO_BESTARMOR
            case 'bestarmour':
                ANSWER = messages.INFO_BESTARMOR
            case 'moisture':
                ANSWER = messages.INFO_MOISTURE
            case 'weatherattack':
                ANSWER = messages.INFO_WEATHERATK
            case 'gloomattackresist':
                ANSWER = messages.INFO_GLOOMATKRES
            case 'slipresist':
                ANSWER = messages.INFO_SLIPRESIST
            case 'attackstack':
                ANSWER = messages.INFO_ATKSTACK
            case 'attackstacking':
                ANSWER = messages.INFO_ATKSTACK
            case 'attackupstacking':
                ANSWER = messages.INFO_ATKSTACK
            case 'boneprof':
                ANSWER = messages.INFO_BONEPROF
            case 'backscratcher':
                ANSWER = messages.INFO_BACKSCRATCH
            case 'lynelbackscratcher':
                ANSWER = messages.INFO_BACKSCRATCH
            case 'lynelfragile':
                ANSWER = messages.INFO_FRAGILEONLYNEL
            case 'dmgcalc':
                ANSWER = messages.POINT_DMGCALC
            # endregion

            # region Reference Info
            case 'tracker':
                ANSWER = messages.POINT_TRACKER
            case 'map':
                ANSWER = messages.POINT_INTERACTMAPS
            case 'interactivemap':
                ANSWER = messages.POINT_INTERACTMAPS
            case 'objmap':
                ANSWER = messages.INFO_OBJECTMAP
            case 'objectmap':
                ANSWER = messages.INFO_OBJECTMAP
            case 'objectterm':
                ANSWER = messages.INFO_USEFULOBJECTTERMS
            case 'echodatasheet':
                ANSWER = messages.POINT_DATAECHO
            case 'phildatasheet':
                ANSWER = messages.POINT_DATAPHIL
            case 'datasheet':
                ANSWER = messages.POINT_DATAPHIL
            case 'worldexp':
                ANSWER = messages.POINT_WORLDEXP
            case 'templescaling':
                ANSWER = messages.POINT_TEMPLESCALING
            case 'sagelevel':
                ANSWER = messages.POINT_SAGELVL
            case 'sagelvl':
                ANSWER = messages.POINT_SAGELVL
            case 'beedletrade':
                ANSWER = messages.POINT_BEEDLETRADES
            case 'cooking':
                ANSWER = messages.POINT_COOKING
            case 'hoverbike':
                ANSWER = messages.POINT_HOVERBIKE
            case 'mapcompletion':
                ANSWER = messages.POINT_MAPCOMPLETION
            case 'recipecalc':
                ANSWER = messages.POINT_RECIPECALC    
            case 'armorcalc':
                ANSWER = messages.POINT_PHILARMORCALC
            case 'armourcalc':
                ANSWER = messages.POINT_PHILARMORCALC
            case 'amiibodrop':
                ANSWER = messages.POINT_AMIIBODROPTABLES
            case 'glitchsheet':
                ANSWER = messages.POINT_GLITCHSHEET
            case 'hoverbike4.0':
                ANSWER = messages.POINT_HOVERBIKEv4
            case 'cookcalc':
                ANSWER = messages.POINT_COOKCALC
            case 'constructhorn':
                ANSWER = messages.POINT_CONSTRUCTHORNFARM
            case 'constructfarm':
                ANSWER = messages.POINT_CONSTRUCTHORNFARM
            case 'shrinefinder':
                ANSWER = messages.POINT_SHRINEFINDER
            case 'sendscreenshot':
                ANSWER = messages.POINT_TRANSFERSCREENSHOTS
            case 'transferscreenshot':
                ANSWER = messages.POINT_TRANSFERSCREENSHOTS
            case 'transferpic':
                ANSWER = messages.POINT_TRANSFERSCREENSHOTS
            case 'levelcard':
                ANSWER = messages.POINT_LEVELCARDS
            case 'lvlcard':
                ANSWER = messages.POINT_LEVELCARDS
            case 'objectsheet':
                ANSWER = messages.POINT_INTEROBJECTSHEET
            case 'dondon':
                ANSWER = messages.POINT_DONDON
            case 'arrowfarm':
                ANSWER = messages.POINT_ARROWFARM
            # endregion

            # region Meta Info
            case 'dupe1.1.2':
                ANSWER = messages.INFO_DUPE112
            case 'dupe1.2.0':
                ANSWER = messages.INFO_DUPE120
            case 'dupe1.2.1':
                ANSWER = messages.INFO_DUPE121
            case 'railingpart':
                ANSWER = messages.INFO_RAILPART
            case 'railpart':
                ANSWER = messages.INFO_RAILPART
            case 'elevatorpart':
                ANSWER = messages.INFO_RAILPART
            case 'unreleasedamiibo':
                ANSWER = messages.POINT_UNRELEASEDAMIIBO
            case 'downpatch':
                ANSWER = messages.INFO_DOWNPATCH
            case 'versioncheck':
                ANSWER = messages.INFO_CHECKGAMEVERSION
            case 'betterphoto':
                ANSWER = messages.POINT_BETTERPHOTOS   
            case 'betterpic':
                ANSWER = messages.POINT_BETTERPHOTOS
            case 'wheredlc':
                ANSWER = messages.POINT_WHEREDLC
            # endregion

            # region Armor Totals
            case 'armortotal':
                ANSWER = messages.IMAGE_ARMORTOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'armortotals.png'))
            case 'armourtotal':
                ANSWER = messages.IMAGE_ARMORTOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'armortotals.png'))
            case 'oretotal':
                ANSWER = messages.IMAGE_ORETOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'oretotals.png'))
            case 'dragontotal':
                ANSWER = messages.IMAGE_DRAGONTOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'dragontotals.png'))
            case 'horntotal':
                ANSWER = messages.IMAGE_HORNTOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'horntotals.png'))
            case 'gutsandtailtotal':
                ANSWER = messages.IMAGE_GUTTAILTOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'guttailtotals.png'))
            case 'gutstotal':
                ANSWER = messages.IMAGE_GUTTAILTOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'guttailtotals.png'))
            case 'tailstotal':
                ANSWER = messages.IMAGE_GUTTAILTOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'guttailtotals.png'))
            case 'meattotal':
                ANSWER = messages.IMAGE_MEATANDADDITIVETOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'meatandadditivetotals.png'))
            case 'fruitandveggietotal':
                ANSWER = messages.IMAGE_FRUITANDVEGGIETOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'fruitandveggietotals.png'))
            case 'fruittotal':
                ANSWER = messages.IMAGE_FRUITANDVEGGIETOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'fruitandveggietotals.png'))
            case 'veggietotal':
                ANSWER = messages.IMAGE_FRUITANDVEGGIETOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'fruitandveggietotals.png'))
            case 'crittertotal':
                ANSWER = messages.IMAGE_CRITTERTOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'crittertotals.png'))
            case 'otherparttotal':
                ANSWER = messages.IMAGE_OTHERPARTTOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'otherparttotals.png'))
            case 'othertotal':
                ANSWER = messages.IMAGE_OTHERPARTTOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'otherparttotals.png'))
            # endregion

            # region Other Images
            case 'horseupgrade':
                ANSWER = messages.IMAGE_HORSEUPGRADE
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'horseupgrades.jpg'))
            case 'horsetotal':
                ANSWER = messages.IMAGE_HORSEUPGRADE
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'horseupgrades.jpg'))
            case 'ascendmap':
                ANSWER = messages.IMAGE_ASCENDMAP
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'ascendmap.jpg'))
            case 'cherrymap':
                ANSWER = messages.IMAGE_CHERRYMAP
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'cherrymap.jpg'))
            case 'dmgformula':
                ANSWER = messages.IMAGE_DMGFORMULA
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'dmgformula.png'))
            case 'invupgrade':
                ANSWER = messages.IMAGE_INVENTORYUPGRADES
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'inventoryupgrades.jpg'))
            case 'shrinecount':
                ANSWER = messages.IMAGE_SHRINECOUNTS
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'shrinecounts.jpg'))
            case 'shrinetotal':
                ANSWER = messages.IMAGE_SHRINECOUNTS
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'shrinecounts.jpg'))
            case 'miskobanner':
                ANSWER = messages.IMAGE_MISKOBANNER
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'miskobanner.jpg'))
            # endregion

            case _:
                ANSWER = messages.ERROR_UNKNOWNCMD

        await system.respond(context, ANSWER, image=IMAGE, hidden=EPHEMERAL)

async def setup(bot):
    await bot.add_cog(Tag(bot))