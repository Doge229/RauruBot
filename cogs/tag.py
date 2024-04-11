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

    #region Embed Setup
    
    #General Help
    EMBED_HELPGENERAL = discord.Embed()
    EMBED_HELPGENERAL.add_field(name=messages.HELP_GENERAL1[0], value=messages.HELP_GENERAL1[1], inline=False)
    EMBED_HELPGENERAL.add_field(name=messages.HELP_GENERAL2[0], value=messages.HELP_GENERAL2[1], inline=False)
    EMBED_HELPGENERAL.add_field(name=messages.HELP_GENERAL3[0], value=messages.HELP_GENERAL3[1], inline=False)
    EMBED_HELPGENERAL.add_field(name=messages.HELP_GENERAL4[0], value=messages.HELP_GENERAL4[1], inline=False)
    EMBED_HELPGENERAL.add_field(name=messages.HELP_GENERAL5[0], value=messages.HELP_GENERAL5[1], inline=False)
    EMBED_HELPGENERAL.add_field(name=messages.HELP_GENERAL6[0], value=messages.HELP_GENERAL6[1], inline=False)

    #Tag Help pg 1
    EMBED_HELPTAGPAGE1 = discord.Embed()
    EMBED_HELPTAGPAGE1.add_field(name=messages.HELP_TAG1[0], value=messages.HELP_TAG1[1], inline=False)
    EMBED_HELPTAGPAGE1.add_field(name=messages.HELP_TAG2[0], value=messages.HELP_TAG2[1], inline=False)
    EMBED_HELPTAGPAGE1.add_field(name=messages.HELP_TAG3[0], value=messages.HELP_TAG3[1], inline=False)
    EMBED_HELPTAGPAGE1.add_field(name=messages.HELP_TAG4[0], value=messages.HELP_TAG4[1], inline=False)
    EMBED_HELPTAGPAGE1.add_field(name=messages.HELP_TAG5[0], value=messages.HELP_TAG5[1], inline=False)
    EMBED_HELPTAGPAGE1.add_field(name=messages.HELP_TAG6[0], value=messages.HELP_TAG6[1], inline=False)
    EMBED_HELPTAGPAGE1.add_field(name=messages.HELP_TAG7[0], value=messages.HELP_TAG7[1], inline=False)
    EMBED_HELPTAGPAGE1.add_field(name=messages.HELP_TAG8[0], value=messages.HELP_TAG8[1], inline=False)

    EMBED_HELPTAGPAGE1.set_footer(text="Page 1 of 2")

    #Tag Help pg 1 (Gen Server)
    EMBED_HELPTAGPAGE1GEN = discord.Embed()
    EMBED_HELPTAGPAGE1GEN.add_field(name=messages.HELP_TAG1[0], value=messages.HELP_TAG1[1], inline=False)
    EMBED_HELPTAGPAGE1GEN.add_field(name=messages.HELP_TAG2[0], value=messages.HELP_TAG2[1], inline=False)
    EMBED_HELPTAGPAGE1GEN.add_field(name=messages.HELP_TAG3[0], value=messages.HELP_TAG3[1], inline=False)
    EMBED_HELPTAGPAGE1GEN.add_field(name=messages.HELP_TAGGENSERVER[0], value=messages.HELP_TAGGENSERVER[1], inline=False)
    EMBED_HELPTAGPAGE1GEN.add_field(name=messages.HELP_TAG4[0], value=messages.HELP_TAG4[1], inline=False)
    EMBED_HELPTAGPAGE1GEN.add_field(name=messages.HELP_TAG5[0], value=messages.HELP_TAG5[1], inline=False)
    EMBED_HELPTAGPAGE1GEN.add_field(name=messages.HELP_TAG6[0], value=messages.HELP_TAG6[1], inline=False)
    EMBED_HELPTAGPAGE1GEN.add_field(name=messages.HELP_TAG7[0], value=messages.HELP_TAG7[1], inline=False)
    EMBED_HELPTAGPAGE1GEN.add_field(name=messages.HELP_TAG8[0], value=messages.HELP_TAG8[1], inline=False)

    EMBED_HELPTAGPAGE1GEN.set_footer(text="Page 1 of 2")

    #Tag Help pg 2
    EMBED_HELPTAGPAGE2 = discord.Embed()
    EMBED_HELPTAGPAGE2.add_field(name=messages.HELP_TAG9[0], value=messages.HELP_TAG9[1], inline=False)
    EMBED_HELPTAGPAGE2.add_field(name=messages.HELP_TAG10[0], value=messages.HELP_TAG10[1], inline=False)
    EMBED_HELPTAGPAGE2.add_field(name=messages.HELP_TAG11[0], value=messages.HELP_TAG11[1], inline=False)

    EMBED_HELPTAGPAGE2.set_footer(text="Page 2 of 2")

    #endregion


    async def tag(context, arg):
        ANSWER = None
        IMAGE = None
        EMBED = None
        EPHEMERAL = False

        arg = system.argcleanup(arg)

        match arg:
            case 'botinfo' | 'userauru':
                ANSWER = messages.INFO_RAURUBOT
            case 'credit':
                ANSWER = messages.INFO_CREDITS
            case 'repo' | 'repository':
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
            case 'helpgeneral' | 'helpgeneral1':
                EPHEMERAL = True
                ANSWER = messages.HELP_GENERALTITLE
                EMBED = Tag.EMBED_HELPGENERAL
            case 'helpgeneralshow' | 'helpgeneralshow1':
                ANSWER = messages.HELP_GENERALTITLE
                EMBED = Tag.EMBED_HELPGENERAL
            case 'generalhelp' | 'generalhelp1':
                EPHEMERAL = True
                ANSWER = messages.HELP_GENERALTITLE
                EMBED = Tag.EMBED_HELPGENERAL
            case 'generalhelpshow' | 'generalhelpshow1':
                ANSWER = messages.HELP_GENERALTITLE
                EMBED = Tag.EMBED_HELPGENERAL
            
            case 'helpshortcut' | 'shortcuthelp':
                ANSWER = messages.HELP_COMMANDSHORTCUT
            # endregion

            # region Tag Help Stuff
            case 'help' | 'help1' | 'helppage1':
                EPHEMERAL = True
                ANSWER = messages.HELP_TAGTITLE
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    EMBED = Tag.EMBED_HELPTAGPAGE1GEN
                else:
                    EMBED = Tag.EMBED_HELPTAGPAGE1
            case 'helpshow' | 'helpshow1' | 'helpshowpage1':
                ANSWER = messages.HELP_TAGTITLE
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    EMBED = Tag.EMBED_HELPTAGPAGE1GEN
                else:
                    EMBED = Tag.EMBED_HELPTAGPAGE1
            case 'help2' | 'helppage2':
                EPHEMERAL = True
                ANSWER = messages.HELP_TAGTITLE
                EMBED = Tag.EMBED_HELPTAGPAGE2
            case 'helpshow2' | 'helpshowpage2':
                ANSWER = messages.HELP_TAGTITLE
                EMBED = Tag.EMBED_HELPTAGPAGE2
            # endregion

            # region TOTKGeneral Server Stuff
            case 'spoiler':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_SPOILERTAG
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'rule913' | 'piracy' | 'to':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_RULE913
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'selfpromotion' | 'selfpromo':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_SELFPROMOTION
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'imageperm' | 'imgperm':
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
            case 'arcaneexp' | 'arcanexp' | 'expsystem':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_ARCANEEXP
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            case 'sageofhyrule' | 'sagerole':
                if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID:
                    ANSWER = messages.INFO_SAGEHYRULEROLE
                else:
                    ANSWER = messages.ERROR_UNKNOWNCMD
            # endregion

            # region Story Stuff
            case 'postgame':
                ANSWER = messages.INFO_POSTGAME
            case 'elitepic':
                ANSWER = messages.INFO_ELITEPIC
            case 'permaquest' | 'permquest':
                ANSWER = messages.INFO_PERMQUESTS
            case 'trueend':
                ANSWER = messages.INFO_TRUEEND
            case 'ringruin':
                ANSWER = messages.INFO_RINGRUINQUEST
            case 'josha':
                ANSWER = messages.INFO_JOSHA
            case 'robbie':
                ANSWER = messages.INFO_ROBBIE
            case 'finalelocation' | 'finalbosslocation':
                ANSWER = messages.INFO_FINALEAPPROACHING
            # endregion

            # region Farming Stuff
            case 'bloodmoon':
                ANSWER = messages.INFO_BLOODMOON
            case 'constructrespawn' | 'constructtimer':
                ANSWER = messages.INFO_CONSTRUCTRESPAWN
            case 'forcebloodmoon':
                ANSWER = messages.POINT_FORCEMOON
            case 'materialrespawn' | 'materialtimer':
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
            case 'constructhorn' | 'constructfarm':
                ANSWER = messages.POINT_CONSTRUCTHORNFARM

            case 'earlyrupee' | 'earlycash':
                ANSWER = messages.POINT_EARLYCASH
            # endregion

            # region Equipment Info
            case 'octorok':
                ANSWER = messages.INFO_OCTOROK
            case 'modifier' | 'naturalmodifier':
                ANSWER = messages.POINT_NATURALMODIFIERS
            case 'repairlegendary' | 'repairlegend':
                ANSWER = messages.INFO_REPAIRLEGEND
            case 'legendarylist' | 'legendlist':
                ANSWER = messages.INFO_LEGENDLISTTITLE
                EMBED = discord.Embed(description=messages.INFO_LEGENDLIST)
            
            case 'fusedurability' | 'fusedura':
                ANSWER = messages.INFO_FUSEDURABILITY
            case 'shieldfuse':
                ANSWER = messages.INFO_SHIELDFUSE
            case 'lynelfragile' | 'fragilematerial' | 'fragilemat':
                ANSWER = messages.INFO_FRAGILEMATERIALS
            case 'breakitdown' | 'breakapart' | 'pelison':
                ANSWER = messages.INFO_BREAKITDOWN
            
            case 'pristine' | 'pristineweapon':
                ANSWER = messages.POINT_WEAPONSINTACT
            
            case 'mastersword':
                ANSWER = messages.INFO_MASTERSWORD
            case 'truedmg' | 'truedamage':
                ANSWER = messages.INFO_TRUEDAMAGE
            case 'amiiborespawnalt' | 'duskbow' | 'whitesword':
                ANSWER = messages.INFO_ALTAMIIBOWEAPONSOURCE
            case 'botwarmor' | 'botwarmour' | 'missingarmor' | 'missingarmour':
                ANSWER = messages.INFO_MISSINGARMOR
            # endregion

            # region Mechanics and Hints
            case 'bargainer' | 'bargainerstatue':
                ANSWER = messages.INFO_BARGAINERSTATUE
            case 'deviceshop' | 'crystalrefinery' | 'crystalrefinerie' | 'refinery' | 'refinerie':
                ANSWER = messages.INFO_CRYSTALREFINERY
            
            case 'botwdata':
                ANSWER = messages.INFO_BOTWDATA
            case 'uniquehorse':
                ANSWER = messages.INFO_UNIQUEHORSES

            case 'cherry' | 'cherrytree':
                ANSWER = messages.INFO_CHERRYTREE
            case 'depthmirror' | 'depthsmirror':
                ANSWER = messages.INFO_DEPTHSMIRROR
            case 'coordsystem':
                ANSWER = messages.INFO_COORDSYSTEM
            
            case 'ritofabric':
                ANSWER = messages.INFO_RITOFABRIC
            case 'trilbyvalley':
                ANSWER = messages.INFO_TRILBYVALLEY
            case 'moatchasm':
                ANSWER = messages.INFO_MOATCHASM
            case 'mat253' | 'sunpumpkin':
                ANSWER = messages.INFO_SUNPUMPKIN
            case 'greatfairy' | 'greatfairie':
                ANSWER = messages.INFO_GREATFAIRYQUEST
            case 'hestu' | 'hestulocation':
                ANSWER = messages.INFO_HESTULOCATION
            case 'control5' | 'jumpslash':
                ANSWER = messages.INFO_JSCONTROL
            case 'missablelocation':
                ANSWER = messages.INFO_MISSABLELOCATIONSTITLE
                EMBED = discord.Embed()
                EMBED.add_field(name=messages.INFO_MISSABLELOCATIONSHEADERS[0], value=messages.INFO_MISSABLELOCATIONS[0], inline=True)
                EMBED.add_field(name=messages.INFO_MISSABLELOCATIONSHEADERS[1], value=messages.INFO_MISSABLELOCATIONS[1], inline=True)
                EMBED.add_field(name=messages.INFO_MISSABLELOCATIONSHEADERS[2], value=messages.INFO_MISSABLELOCATIONS[2], inline=False)
                EMBED.set_footer(text=messages.INFO_MISSABLELOCATIONSFOOTNOTE)
            case 'mapcompletiontip':
                ANSWER = messages.INFO_MAPCOMPLETIONTIPS
            case 'subbosscompletion' | 'minibosscompletion' | 'monstermedal' | 'monstermedaltip':
                ANSWER = messages.INFO_SUBBOSSCOMPLETIONTITLE
                EMBED = discord.Embed()
                EMBED.add_field(name=messages.INFO_SUBBOSSCOMPLETIONHEADERS[0], value=messages.INFO_SUBBOSSCOMPLETION[0], inline=False)
                EMBED.add_field(name=messages.INFO_SUBBOSSCOMPLETIONHEADERS[1], value=messages.INFO_SUBBOSSCOMPLETION[1], inline=False)
                EMBED.add_field(name=messages.INFO_SUBBOSSCOMPLETIONHEADERS[2], value=messages.INFO_SUBBOSSCOMPLETION[2], inline=False)
                EMBED.add_field(name=messages.INFO_SUBBOSSCOMPLETIONHEADERS[3], value=messages.INFO_SUBBOSSCOMPLETION[3], inline=False)
                EMBED.add_field(name=messages.INFO_SUBBOSSCOMPLETIONHEADERS[4], value=messages.INFO_SUBBOSSCOMPLETION[4], inline=False)
            case 'hornedstatue' | 'hornedone':
                ANSWER = messages.INFO_HORNEDSTATUE
            case 'dugby':
                ANSWER = messages.INFO_DUGBY
            case 'elementaldamage' | 'elementdmg':
                ANSWER = messages.INFO_BASEELEMENTALDMG
            case 'malanya' | 'malanyalocation' | 'horsegod' | 'horsegodlocation':
                ANSWER = messages.INFO_MALANYALOCATION
            
            case 'gleeokstrat':
                ANSWER = messages.INFO_GLEEOKSTRAT
            case 'midairwing':
                ANSWER = messages.INFO_MIDAIRWING
            case 'beginnertip' | 'startertip' | 'totktip':
                ANSWER = messages.INFO_BEGINNERTIPSTITLE
                EMBED = discord.Embed()
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[0], value=messages.INFO_BEGINNERTIPS[0], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[1], value=messages.INFO_BEGINNERTIPS[1], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[2], value=messages.INFO_BEGINNERTIPS[2], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[3], value=messages.INFO_BEGINNERTIPS[3], inline=False)
                EMBED.add_field(name=messages.INFO_BEGINNERTIPSHEADERS[4], value=messages.INFO_BEGINNERTIPS[4], inline=False)
            # endregion

            # region Effects and Builds
            case 'defense' | 'defence':
                ANSWER = messages.INFO_DEFENSESTAT
            case 'bestarmor' | 'bestarmour':
                ANSWER = messages.INFO_BESTARMOR
            case 'bestfuse':
                ANSWER = messages.INFO_BESTFUSE
            case 'gloomdmg' | 'gloomdamage':
                ANSWER = messages.INFO_GLOOMDAMAGEFORMULATITLE
                EMBED = discord.Embed()
                EMBED.add_field(name='', value=messages.INFO_GLOOMDAMAGEFORMULA[0])
                EMBED.add_field(name='', value=messages.INFO_GLOOMDAMAGEFORMULA[1])
            
            case 'backscratcher' | 'lynelbackscratcher':
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
            case 'attackstack' | 'attackstacking' | 'attackupstacking':
                ANSWER = messages.INFO_ATKSTACK
            case 'boneprof':
                ANSWER = messages.INFO_BONEPROF
            # endregion

            # region Reference Info
            case 'wiki':
                ANSWER = messages.POINT_WIKI
            case 'fandom' | 'fandombad' | 'wikimigration':
                ANSWER = messages.POINT_FANDOMBAD

            case 'tracker':
                ANSWER = messages.POINT_TRACKER
            case 'botwtracker' | 'trackerbotw':
                ANSWER = messages.POINT_BOTWTRACKER
            case 'armorcalc' | 'armourcalc':
                ANSWER = messages.POINT_PHILARMORCALC
            case 'mapcompletion':
                ANSWER = messages.POINT_MAPCOMPLETION
            case 'shrinefinder':
                ANSWER = messages.POINT_SHRINEFINDER2 if context.guild.id == config.GENSERVERID or context.guild.id == config.DEVSERVERID else messages.POINT_SHRINEFINDER
            
            case 'map' | 'interactivemap':
                ANSWER = messages.POINT_INTERACTMAPS
            case 'objmap' | 'objectmap':
                ANSWER = messages.INFO_OBJECTMAP
            case 'objectterm' | 'objterm' | 'objectmapterm' | 'objmapterm':
                ANSWER = messages.INFO_USEFULOBJECTTERMSTITLE
                EMBED = discord.Embed(description=messages.INFO_USEFULOBJECTTERMS)
            
            case 'phildatasheet' | 'datasheet':
                ANSWER = messages.POINT_DATAPHIL
            case 'echodatasheet':
                ANSWER = messages.POINT_DATAECHO
            case 'objectsheet':
                ANSWER = messages.POINT_INTEROBJECTSHEET
            
            case 'worldexp' | 'worldxp':
                ANSWER = messages.POINT_WORLDEXP
            case 'templescaling' | 'bossscaling' | 'dungeonscaling':
                ANSWER = messages.POINT_TEMPLESCALING
            case 'sagelevel' | 'sagelvl':
                ANSWER = messages.POINT_SAGELVL
            case 'bloodmoondoc' | 'respawndoc':
                ANSWER = messages.POINT_BLOODMOONDOC

            case 'cooking':
                ANSWER = messages.POINT_COOKING
            case 'cookcalc' | 'cookbook':
                ANSWER = messages.POINT_COOKCALC

            case 'levelcard' | 'lvlcard':
                ANSWER = messages.POINT_LEVELCARDS
            case 'directlink' | 'directimglink':
                ANSWER = messages.INFO_DIRECTIMGLINK
            case 'beedletrade':
                ANSWER = messages.POINT_BEEDLETRADES
            case 'amiibodrop':
                ANSWER = messages.POINT_AMIIBODROPTABLES
            case 'glitchsheet':
                ANSWER = messages.POINT_GLITCHSHEET
            case 'dondon':
                ANSWER = messages.POINT_DONDON
            case 'horsecolor' | 'horsecolour':
                ANSWER = messages.POINT_HORSECOLORS
            case 'devicedrain' | 'energycelldrain':
                ANSWER = messages.POINT_ENERGYCELLSTATS
            case 'dispenserprice' | 'dispenserdrop' | 'dispenserrate':
                ANSWER = messages.POINT_DISPENSERPRICES
            case 'combatguide' | 'combattip':
                ANSWER = messages.POINT_COMBATGUIDE
            case 'missableobject' | 'missableitem':
                ANSWER = messages.POINT_MISSABLEOBJECTS

            case 'hoverbike':
                ANSWER = messages.POINT_HOVERBIKE
            case 'hoverbike4.0' | 'railbike':
                ANSWER = messages.POINT_HOVERBIKEv4
            case 'goldenwing' | 'infinitywing' | 'infinitewing':
                ANSWER = messages.POINT_GOLDENWING
            case 'railingpart' | 'railpart' | 'elevatorpart' | 'elevatorrail':
                ANSWER = messages.POINT_RAILPARTTITLE
                EMBED = discord.Embed(description=messages.POINT_RAILPART)
            case 'betterphoto' | 'betterpic':
                ANSWER = messages.POINT_BETTERPHOTOS
            case 'paracopter':
                ANSWER = messages.POINT_PARACOPTER
            case 'fuseidea':
                ANSWER = messages.POINT_FUSEIDEAS
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
            case 'transferalbum' | 'transferpic' | 'transferclip' | 'transfervid':
                ANSWER = messages.POINT_TRANSFERALBUMTITLE
                EMBED = discord.Embed(description=messages.POINT_TRANSFERALBUM)
            
            case 'wheredlc' | 'gimmedlc' | 'dlc':
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
            case 'gutsandtailtotal' | 'gutstotal' | 'tailstotal':
                ANSWER = messages.IMAGE_GUTTAILTOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'guttailtotals.png'))
            case 'meattotal':
                ANSWER = messages.IMAGE_MEATANDADDITIVETOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'meatandadditivetotals.png'))
            case 'fruitandveggietotal' | 'fruittotal' | 'veggietotal':
                ANSWER = messages.IMAGE_FRUITANDVEGGIETOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'fruitandveggietotals.png'))
            case 'crittertotal':
                ANSWER = messages.IMAGE_CRITTERTOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'crittertotals.png'))
            case 'otherparttotal' | 'othertotal':
                ANSWER = messages.IMAGE_OTHERPARTTOTAL
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'otherparttotals.png'))
            # endregion

            # region Other Images
            case 'horseupgrade' | 'horsetotal':
                ANSWER = messages.IMAGE_HORSEUPGRADE
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'horseupgrades.jpg'))
            case 'ascendmap' | 'ascendpointmap' | 'ascendpointsmap' | 'ascendruinmap' | 'ascendruinsmap':
                ANSWER = messages.IMAGE_ASCENDMAP
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'ascendmap.jpg'))
            case 'cherrymap':
                ANSWER = messages.IMAGE_CHERRYMAP
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'cherrymap.jpg'))
            case 'cherryareamap':
                ANSWER = messages.IMAGE_CHERRYAREAMAP
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'SPOILER_cherryareamap.jpg'))
            case 'koltinstallmap' | 'koltinmap':
                ANSWER = messages.IMAGE_KOLTINSTALLMAP
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'koltinstallmap.jpg'))
            case 'invupgrade':
                ANSWER = messages.IMAGE_INVENTORYUPGRADES
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'inventoryupgrades.jpg'))
            case 'shrinecount' | 'shrinetotal' | 'shrinetype':
                ANSWER = messages.IMAGE_SHRINECOUNTS
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'shrinecounts.jpg'))
            
            case 'miskobanner':
                ANSWER = messages.IMAGE_MISKOBANNER
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'miskobanner.jpg'))
            
            case 'dmgformula':
                ANSWER = messages.IMAGE_DMGFORMULA
                IMAGE = discord.File(os.path.join(system.DIR_RESOURCE, 'dmgformula.jpg'))
            # endregion

            case _:
                ANSWER = messages.ERROR_UNKNOWNCMD

        await system.respond(context, ANSWER, image=IMAGE, hidden=EPHEMERAL, embed=EMBED)

async def setup(bot):
    await bot.add_cog(Tag(bot))