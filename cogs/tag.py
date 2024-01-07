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
        ANSWER = None
        IMAGE = None
        EMBED = None
        EPHEMERAL = False

        arg = system.argcleanup(arg)

        match arg:
            case 'botinfo':
                ANSWER = messages.INFO_RAURUBOT
            case 'userauru':
                ANSWER = messages.INFO_RAURUBOT
            case 'credit':
                ANSWER = messages.INFO_CREDITS
            case 'repo':
                ANSWER = messages.INFO_REPOSITORY
            case 'repository':
                ANSWER = messages.INFO_REPOSITORY
            case 'disclaimer':
                try:
                    if context.author.id == config.USERID_DOGE229:
                        ANSWER = messages.INFO_DEVDISCLAIMER
                        EPHEMERAL = True
                    else:
                        ANSWER = messages.ERROR_UNKNOWNCMD
                except:
                    if context.user.id == config.USERID_DOGE229:
                        ANSWER = messages.INFO_DEVDISCLAIMER
                        EPHEMERAL = True
                    else:
                        ANSWER = messages.ERROR_UNKNOWNCMD
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
            case 'test':
                ANSWER = ''
                EMBED = discord.Embed(description=messages.HELP_TAGBASE)
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
            case 'help2':
                EPHEMERAL = True
                ANSWER = messages.HELP_TAGBASE + messages.HELP_TAG2
            case 'helppage2':
                EPHEMERAL = True
                ANSWER = messages.HELP_TAGBASE + messages.HELP_TAG2
            case 'helpshow2':
                ANSWER = messages.HELP_TAGBASE + messages.HELP_TAG2
            case 'helpshowpage2':
                ANSWER = messages.HELP_TAGBASE + messages.HELP_TAG2
                
            # endregion

            # region TOTKGeneral Server Stuff
            case 'spoiler':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_SPOILERTAG
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'rule913':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_RULE913
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'piracy':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_RULE913
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'to':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_RULE913
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'selfpromotion':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_SELFPROMOTION
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'selfpromo':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_SELFPROMOTION
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'imageperm':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_IMGPERM
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'imgperm':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_IMGPERM
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'traveler':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_IMGPERM
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'travelerrole':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_IMGPERM
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'rolereward':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_ROLEREWARDS
                    IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'rolerewards.jpg'))
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'arcaneexp':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_ARCANEEXP
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'arcanexp':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_ARCANEEXP
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'expsystem':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_ARCANEEXP
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'totkexpert':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_EXPERTROLE
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            # endregion

            # region Story Stuff
            case 'postgame':
                ANSWER = messages.INFO_POSTGAME
            case 'elitepic':
                ANSWER = messages.INFO_ELITEPIC
            case 'permaquest':
                ANSWER = messages.INFO_PERMQUESTS
            case 'permquest':
                ANSWER = messages.INFO_PERMQUESTS
            case 'trueend':
                ANSWER = messages.INFO_TRUEEND
            case 'ringruin':
                ANSWER = messages.INFO_RINGRUINQUEST
            case 'josha':
                ANSWER = messages.INFO_JOSHA
            case 'robbie':
                ANSWER = messages.INFO_ROBBIE
            case 'finalelocation':
                ANSWER = messages.INFO_FINALEAPPROACHING
            case 'finalbosslocation':
                ANSWER = messages.INFO_FINALEAPPROACHING
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
                ANSWER = messages.INFO_CHARGEFARMTITLE
                EMBED = discord.Embed(description=messages.INFO_CHARGEFARM)
            case 'starfragment':
                ANSWER = messages.POINT_STARFARM
            case 'dragon':
                ANSWER = messages.POINT_DRAGON
            case 'arrowfarm':
                ANSWER = messages.POINT_ARROWFARM
            case 'freelynelbow':
                ANSWER = messages.POINT_FREELYNELBOWS
            case 'constructhorn':
                ANSWER = messages.POINT_CONSTRUCTHORNFARM
            case 'constructfarm':
                ANSWER = messages.POINT_CONSTRUCTHORNFARM

            case 'earlyrupee':
                ANSWER = messages.POINT_EARLYCASH
            case 'earlycash':
                ANSWER = messages.POINT_EARLYCASH
            # endregion

            # region Equipment Info
            case 'octorok':
                ANSWER = messages.INFO_OCTOROK
            case 'modifier':
                ANSWER = messages.POINT_NATURALMODIFIERS
            case 'naturalmodifier':
                ANSWER = messages.POINT_NATURALMODIFIERS
            case 'repairlegendary':
                ANSWER = messages.INFO_REPAIRLEGEND
            case 'repairlegend':
                ANSWER = messages.INFO_REPAIRLEGEND
            case 'legendarylist':
                ANSWER = messages.INFO_LEGENDLISTTITLE
                EMBED = discord.Embed(description=messages.INFO_LEGENDLIST)
            case 'legendlist':
                ANSWER = messages.INFO_LEGENDLISTTITLE
                EMBED = discord.Embed(description=messages.INFO_LEGENDLIST)
            
            case 'fusedurability':
                ANSWER = messages.INFO_FUSEDURABILITY
            case 'fusedura':
                ANSWER = messages.INFO_FUSEDURABILITY
            case 'shieldfuse':
                ANSWER = messages.INFO_SHIELDFUSE
            case 'lynelfragile':
                ANSWER = messages.INFO_FRAGILEMATERIALS
            case 'fragilematerial':
                ANSWER = messages.INFO_FRAGILEMATERIALS
            case 'fragilemat':
                ANSWER = messages.INFO_FRAGILEMATERIALS
            case 'breakitdown':
                ANSWER = messages.INFO_BREAKITDOWN
            case 'breakapart':
                ANSWER = messages.INFO_BREAKITDOWN
            case 'pelison':
                ANSWER = messages.INFO_BREAKITDOWN
            
            case 'pristine':
                ANSWER = messages.POINT_WEAPONSINTACT
            case 'pristineweapon':
                ANSWER = messages.POINT_WEAPONSINTACT
            
            case 'mastersword':
                ANSWER = messages.INFO_MASTERSWORD
            case 'truedmg':
                ANSWER = messages.INFO_TRUEDAMAGE
            case 'truedamage':
                ANSWER = messages.INFO_TRUEDAMAGE
            case 'amiiborespawnalt':
                ANSWER = messages.INFO_ALTAMIIBOWEAPONSOURCE
            case 'duskbow':
                ANSWER = messages.INFO_ALTAMIIBOWEAPONSOURCE
            case 'whitesword':
                ANSWER = messages.INFO_ALTAMIIBOWEAPONSOURCE
            case 'botwarmor':
                ANSWER = messages.INFO_MISSINGARMOR
            case 'missingarmor':
                ANSWER = messages.INFO_MISSINGARMOR
            # endregion

            # region Mechanics and Hints
            case 'bargainer':
                ANSWER = messages.INFO_BARGAINERSTATUE
            case 'bargainerstatue':
                ANSWER = messages.INFO_BARGAINERSTATUE
            case 'deviceshop':
                ANSWER = messages.INFO_CRYSTALREFINERY
            case 'crystalrefinery':
                ANSWER = messages.INFO_CRYSTALREFINERY
            case 'crystalrefinerie':
                ANSWER = messages.INFO_CRYSTALREFINERY
            case 'refinery':
                ANSWER = messages.INFO_CRYSTALREFINERY
            case 'refinerie':
                ANSWER = messages.INFO_CRYSTALREFINERY
            
            case 'botwdata':
                ANSWER = messages.INFO_BOTWDATA
            case 'uniquehorse':
                ANSWER = messages.INFO_UNIQUEHORSES

            case 'cherry':
                ANSWER = messages.INFO_CHERRYTREE
            case 'cherrytree':
                ANSWER = messages.INFO_CHERRYTREE
            case 'depthmirror':
                ANSWER = messages.INFO_DEPTHSMIRROR
            case 'depthsmirror':
                ANSWER = messages.INFO_DEPTHSMIRROR
            case 'coordsystem':
                ANSWER = messages.INFO_COORDSYSTEM
            
            case 'ritofabric':
                ANSWER = messages.INFO_RITOFABRIC
            case 'trilbyvalley':
                ANSWER = messages.INFO_TRILBYVALLEY
            case 'moatchasm':
                ANSWER = messages.INFO_MOATCHASM
            case 'mat253':
                ANSWER = messages.INFO_SUNPUMPKIN
            case 'sunpumpkin':
                ANSWER = messages.INFO_SUNPUMPKIN
            case 'greatfairy':
                ANSWER = messages.INFO_GREATFAIRYQUEST
            case 'greatfairie':
                ANSWER = messages.INFO_GREATFAIRYQUEST
            case 'hestu':
                ANSWER = messages.INFO_HESTULOCATION
            case 'hestulocation':
                ANSWER = messages.INFO_HESTULOCATION
            case 'control5':
                ANSWER = messages.INFO_JSCONTROL
            case 'jumpslash':
                ANSWER = messages.INFO_JSCONTROL
            case 'missablelocation':
                ANSWER = messages.INFO_MISSABLELOCATIONSTITLE
                EMBED = discord.Embed(description=messages.INFO_MISSABLELOCATIONS)
            case 'hornedstatue':
                ANSWER = messages.INFO_HORNEDSTATUE
            case 'hornedone':
                ANSWER = messages.INFO_HORNEDSTATUE
            case 'dugby':
                ANSWER = messages.INFO_DUGBY
            case 'elementaldamage':
                ANSWER = messages.INFO_BASEELEMENTALDMG
            case 'elementdmg':
                ANSWER = messages.INFO_BASEELEMENTALDMG
            case 'malanya':
                ANSWER = messages.INFO_MALANYALOCATION
            case 'malanyalocation':
                ANSWER = messages.INFO_MALANYALOCATION
            case 'horsegod':
                ANSWER = messages.INFO_MALANYALOCATION
            case 'horsegodlocation':
                ANSWER = messages.INFO_MALANYALOCATION
            
            case 'gleeokstrat':
                ANSWER = messages.INFO_GLEEOKSTRAT
            case 'midairwing':
                ANSWER = messages.INFO_MIDAIRWING
            case 'beginnertip':
                ANSWER = messages.INFO_BEGINNERTIPSTITLE
                EMBED = discord.Embed()
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[0], value=messages.INFO_BEGINNERTIPS[0], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[1], value=messages.INFO_BEGINNERTIPS[1], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[2], value=messages.INFO_BEGINNERTIPS[2], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[3], value=messages.INFO_BEGINNERTIPS[3], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[4], value=messages.INFO_BEGINNERTIPS[4], inline=False)
            case 'startertip':
                ANSWER = messages.INFO_BEGINNERTIPSTITLE
                EMBED = discord.Embed()
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[0], value=messages.INFO_BEGINNERTIPS[0], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[1], value=messages.INFO_BEGINNERTIPS[1], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[2], value=messages.INFO_BEGINNERTIPS[2], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[3], value=messages.INFO_BEGINNERTIPS[3], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[4], value=messages.INFO_BEGINNERTIPS[4], inline=False)
            case 'totktip':
                ANSWER = messages.INFO_BEGINNERTIPSTITLE
                EMBED = discord.Embed()
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[0], value=messages.INFO_BEGINNERTIPS[0], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[1], value=messages.INFO_BEGINNERTIPS[1], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[2], value=messages.INFO_BEGINNERTIPS[2], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[3], value=messages.INFO_BEGINNERTIPS[3], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[4], value=messages.INFO_BEGINNERTIPS[4], inline=False)
            # endregion

            # region Effects and Builds
            case 'defense':
                ANSWER = messages.INFO_DEFENSESTAT
            case 'bestarmor':
                ANSWER = messages.INFO_BESTARMOR
            case 'bestarmour':
                ANSWER = messages.INFO_BESTARMOR
            
            case 'backscratcher':
                ANSWER = messages.INFO_BACKSCRATCH
            case 'lynelbackscratcher':
                ANSWER = messages.INFO_BACKSCRATCH
            case 'dmgcalc':
                ANSWER = messages.POINT_DMGCALC
            
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
            # endregion

            # region Reference Info
            case 'wiki':
                ANSWER = messages.POINT_WIKI
            case 'fandom':
                ANSWER = messages.POINT_FANDOMBAD
            case 'fandombad':
                ANSWER = messages.POINT_FANDOMBAD
            case 'wikimigration':
                ANSWER = messages.POINT_FANDOMBAD

            case 'tracker':
                ANSWER = messages.POINT_TRACKER
            case 'armorcalc':
                ANSWER = messages.POINT_PHILARMORCALC
            case 'armourcalc':
                ANSWER = messages.POINT_PHILARMORCALC
            case 'mapcompletion':
                ANSWER = messages.POINT_MAPCOMPLETION
            case 'shrinefinder':
                ANSWER = messages.POINT_SHRINEFINDER2 if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID else messages.POINT_SHRINEFINDER
            
            case 'map':
                ANSWER = messages.POINT_INTERACTMAPS
            case 'interactivemap':
                ANSWER = messages.POINT_INTERACTMAPS
            case 'objmap':
                ANSWER = messages.INFO_OBJECTMAP
            case 'objectmap':
                ANSWER = messages.INFO_OBJECTMAP
            case 'objectterm':
                ANSWER = messages.INFO_USEFULOBJECTTERMSTITLE
                EMBED = discord.Embed(description=messages.INFO_USEFULOBJECTTERMS)
            case 'objterm':
                ANSWER = messages.INFO_USEFULOBJECTTERMSTITLE
                EMBED = discord.Embed(description=messages.INFO_USEFULOBJECTTERMS)
            case 'objectmapterm':
                ANSWER = messages.INFO_USEFULOBJECTTERMSTITLE
                EMBED = discord.Embed(description=messages.INFO_USEFULOBJECTTERMS)
            case 'objmapterm':
                ANSWER = messages.INFO_USEFULOBJECTTERMSTITLE
                EMBED = discord.Embed(description=messages.INFO_USEFULOBJECTTERMS)
            
            case 'phildatasheet':
                ANSWER = messages.POINT_DATAPHIL
            case 'datasheet':
                ANSWER = messages.POINT_DATAPHIL
            case 'echodatasheet':
                ANSWER = messages.POINT_DATAECHO
            case 'objectsheet':
                ANSWER = messages.POINT_INTEROBJECTSHEET
            
            case 'worldexp':
                ANSWER = messages.POINT_WORLDEXP
            case 'templescaling':
                ANSWER = messages.POINT_TEMPLESCALING
            case 'sagelevel':
                ANSWER = messages.POINT_SAGELVL
            case 'sagelvl':
                ANSWER = messages.POINT_SAGELVL
            
            case 'cooking':
                ANSWER = messages.POINT_COOKING
            case 'cookcalc':
                ANSWER = messages.POINT_COOKCALC
            case 'cookbook':
                ANSWER = messages.POINT_COOKCALC

            case 'levelcard':
                ANSWER = messages.POINT_LEVELCARDS
            case 'lvlcard':
                ANSWER = messages.POINT_LEVELCARDS
            case 'directlink':
                ANSWER = messages.INFO_DIRECTIMGLINK
            case 'directimglink':
                ANSWER = messages.INFO_DIRECTIMGLINK
            case 'beedletrade':
                ANSWER = messages.POINT_BEEDLETRADES
            case 'amiibodrop':
                ANSWER = messages.POINT_AMIIBODROPTABLES
            case 'glitchsheet':
                ANSWER = messages.POINT_GLITCHSHEET
            case 'dondon':
                ANSWER = messages.POINT_DONDON
            case 'horsecolor':
                ANSWER = messages.POINT_HORSECOLORS
            case 'devicedrain':
                ANSWER = messages.POINT_ENERGYCELLSTATS
            case 'energycelldrain':
                ANSWER = messages.POINT_ENERGYCELLSTATS
            
            case 'hoverbike':
                ANSWER = messages.POINT_HOVERBIKE
            case 'hoverbike4.0':
                ANSWER = messages.POINT_HOVERBIKEv4
            case 'railbike':
                ANSWER = messages.POINT_HOVERBIKEv4
            case 'goldenwing':
                ANSWER = messages.POINT_GOLDENWING
            case 'infinitywing':
                ANSWER = messages.POINT_GOLDENWING
            case 'infinitewing':
                ANSWER = messages.POINT_GOLDENWING
            case 'railingpart':
                ANSWER = messages.POINT_RAILPART
            case 'railpart':
                ANSWER = messages.POINT_RAILPARTTITLE
                EMBED = discord.Embed(description=messages.POINT_RAILPART)
            case 'elevatorpart':
                ANSWER = messages.POINT_RAILPART
            case 'elevatorrail':
                ANSWER = messages.POINT_RAILPART
            case 'betterphoto':
                ANSWER = messages.POINT_BETTERPHOTOS
            case 'betterpic':
                ANSWER = messages.POINT_BETTERPHOTOS
            case 'paracopter':
                ANSWER = messages.POINT_PARACOPTER
            case 'bestfuse':
                ANSWER = messages.POINT_BESTFUSES
            case 'fuseidea':
                ANSWER = messages.POINT_BESTFUSES
            # endregion

            # region Meta Info
            case 'dupe1.1.2':
                ANSWER = messages.INFO_DUPE112TITLE
                EMBED = discord.Embed(description=messages.INFO_DUPE112)
            case 'dupe1.2.0':
                ANSWER = messages.INFO_DUPE120TITLE
                EMBED = discord.Embed(description=messages.INFO_DUPE120)
            case 'dupe1.2.1':
                ANSWER = messages.INFO_DUPE121TITLE
                EMBED = discord.Embed(description=messages.INFO_DUPE121)

            case 'downpatch':
                ANSWER = messages.INFO_DOWNPATCH
            case 'preventupdate':
                ANSWER = messages.INFO_PREVENTUPDATES
            case 'versioncheck':
                ANSWER = messages.INFO_CHECKGAMEVERSION
            case 'transferalbum':
                ANSWER = messages.POINT_TRANSFERALBUMTITLE
                EMBED = discord.Embed(description=messages.POINT_TRANSFERALBUM)
            case 'transferpic':
                ANSWER = messages.POINT_TRANSFERALBUMTITLE
                EMBED = discord.Embed(description=messages.POINT_TRANSFERALBUM)
            case 'transferclip':
                ANSWER = messages.POINT_TRANSFERALBUMTITLE
                EMBED = discord.Embed(description=messages.POINT_TRANSFERALBUM)
            case 'transfervid':
                ANSWER = messages.POINT_TRANSFERALBUMTITLE
                EMBED = discord.Embed(description=messages.POINT_TRANSFERALBUM)
            
            case 'wheredlc':
                ANSWER = messages.POINT_WHEREDLC
            case 'gimmedlc':
                ANSWER = messages.POINT_WHEREDLC
            case 'dlc':
                ANSWER = messages.POINT_WHEREDLC
            case 'nfctag':
                ANSWER = messages.POINT_NFCTAGS if not context.guild.id == config.GENSERVERID else messages.ERROR_UNKNOWNCMD
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
            
            case 'dmgformula':
                ANSWER = messages.IMAGE_DMGFORMULA
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'dmgformula.png'))
            # endregion

            case _:
                ANSWER = messages.ERROR_UNKNOWNCMD

        await system.respond(context, ANSWER, image=IMAGE, hidden=EPHEMERAL, embed=EMBED)

async def setup(bot):
    await bot.add_cog(Tag(bot))