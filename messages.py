# messages.py

# region System
BOT_ONLINESIMPLE = '''Bot is now online'''
BOT_ONLINEPERSON = ''''''
BOT_OFFLINESIMPLE = '''Bot is shutting down'''
BOT_OFFLINEPERSON = '''Now it is up to you, Link...........'''

ERROR_UNKNOWNCMD = '''My apologies, I'm afraid I don't recognize that command. Use `/help` to see available commands.'''
ERROR_BLACKLIST = '''My apologies, but I'm afraid I don't understand that blacklist command. Use `@Rauru#6248 blacklisthelp` to see how to use the blacklist command.'''
ERROR_GUILDONLY = '''My apologies, but my commands are only available inside servers.'''
ERROR_BADROLE = '''My apologies, but you lack the appropriate role for this command.'''

ERROR_BADCOORDS = '''My apologies, but I cannot convert those coordinates.'''
ERROR_BADDEVICE = '''My apologies, but I do not recognize that Zonai Device name.'''

INFO_RAURUBOT = '''
Greetings! My name is Rauru. I am here to help guide you on your journey through Hyrule by providing information and links. 
Please feel free to use `/help` and use as many of my commands as you like in a bot channel.
'''
INFO_CREDITS = '''
This bot and its files were developed by Doge229.

Massive thanks to:
-Zanaras, for helping with development and server setup
-Everyone else who helped with development, cause discord.py has really bad documentation
-Echocolat, Phil, dt13269, bjm, and everyone else on the TOTK Data Collection and Research Discord server who provided truly obscene amounts of information about the game
-savage13 and the Object Map team
-Austin John Plays on Youtube
-u/Silver_Foxx on Reddit/@Lexeon on Youtube
-Suishi on Youtube
-riso for their UI icons
-Shozutko for their map images, and work on various resource documents
-Everyone else in the botw and totk communities who have created resources for these games
-The testers on the RauruBot Devlab server:
    -glitchtest
    -phoenixguy123
    -luciebox
    -gudpotato
'''
INFO_REPOSITORY = '''
Here's a link to my repository on Github:
<https://github.com/Doge229/RauruBot>
Please remember to check out the ReadMe and license if you need to use any of my code/info for your own projects!
'''
INFO_DEVDISCLAIMER = '''
I make a lot of different resources for TotK, and I try my best to keep the information I disseminate as accurate and up-to-date as possible. That being said, if you think any information I have is wrong, please feel free to let me know. I want to make sure everyone has the correct information, so I am always open to being proven wrong. However, please keep in mind that anecdotal evidence is extremely hard to accept by itself, and I will need more substantial information before I am able to make changes to my resources.
'''
# endregion

# region Help
HELP_GENERALARCHIVE = '''
Here are some of my commands:

`/help [option]`
    `show`
  -See what commands I have available

`/tag help`
  -See what options I have for `/tag`

`/find [search terms]`
  -You can use this command to create an Object Map link with search terms integrated into it. Just put the exact text (including spaces and punctuation) for your search terms after the command.

`/coordconvert [Object Map coordinates]`
  -You can use this command to convert the coordinate of an object from the Object Map into its shown in-game coordinates.
  -Just copy the coordinates of the object's position directly from the Object Map, then paste it in.
    
    For Example:
    `/coordconvert -579.73, 129.61, -524.79` will give you the in-game coords: `-580, -525, 25`

`/findpristine [weapon name]`
  -You can use this command to create an Object Map link that will show which Depths Ghosts can spawn a weapon.

`/finddispenser [device name]`
  -You can use this command to see which Device Dispensers are most likely to dispense a specific Zonai Device.
'''

HELP_GENERALTITLE = '''Here are some of my commands:'''
HELP_GENERAL1 = ['''/help [option]''', '''
`show`
- See what commands I have available''']
HELP_GENERAL2 = ['''/tag help''', '''
- See what options I have for `/tag`''']
HELP_GENERAL3 = ['''/find [search terms]''', '''
- You can use this command to create an Object Map link with search terms integrated into it. Just put the exact text (including spaces and punctuation) for your search terms after the command.''']
HELP_GENERAL4 = ['''/coordconvert [Object Map coordinates]''', '''
- You can use this command to convert the coordinate of an object from the Object Map into its shown in-game coordinates.
- Just copy the coordinates of the object's position directly from the Object Map, then paste it in.
For Example:
- `/coordconvert -579.73, 129.61, -524.79` will give you the in-game coords: `-580, -525, 25`''']
HELP_GENERAL5 = ['''/findpristine [weapon name]''', '''
- You can use this command to create an Object Map link that will show which Depths Ghosts can spawn a weapon.''']
HELP_GENERAL6 = ['''/finddispenser [device name]''', '''
- You can use this command to see which Device Dispensers are most likely to dispense a specific Zonai Device.''']


HELP_TAGARCHIVE = '''
Here are the options for my `tag` command:

`/tag [option]`
    `botinfo/userauru, credits, repository`

    **Tag Command Help**
    `help [page number], help show [page number]`
  -*Note: Page number defaults to the 1st page if not specified*
    **General Command Help** (For when `/help` isn't available)
    `helpgeneral, helpgeneral show`
    **Server Stuff**
    `spoiler, piracy/tos, selfpromo/selfpromotion, imgperms, rolerewards, arcaneexp/expsystem, totkexpert`
    **Story Stuff**
    `postgame, elitepics, permaquests, trueend, ringruins, josha, robbie, finalelocation/finalbosslocation`
    **Farming Stuff**
    `bloodmoon, constructrespawn, forcebloodmoon, materialrespawn, shoprestock, chargefarm, starfragment, dragon, arrowfarm, freelynelbows, constructfarm, earlyrupees`
    **Equipment Info**
    `octorok, naturalmodifiers, repairlegendary, legendarylist, fusedurability, shieldfuse, fragilematerials/fragilemats, breakitdown/pelison, pristineweapons, mastersword, truedmg, amiiborespawnalt/duskbow/whitesword, botwarmor/missingarmor`
    **Mechanics and Hints**
    `bargainer/bargainerstatues, crystalrefinery/refinery, botwdata, uniquehorses, cherry/cherrytrees, depthsmirror, coordsystem, ritofabric, trilbyvalley, moatchasm, mat253/sunpumpkin, greatfairy, hestu/hestulocation, control5/jumpslash, missablelocations, hornedstatue, dugby, elementdmg, malanya/malanyalocation, midairwing, gleeokstrat, miskobanner, beginnertips/totktips`
    **Effects and Builds**
    `defense, bestarmor, backscratcher, dmgcalc, moisture, weatherattack, gloomattackresist, slipresist, attackupstacking, boneprof`
Page 1 of 2
    **Useful Links and Stuff**
    `wiki, fandom/wikimigration, tracker, armorcalc, mapcompletion, shrinefinder, maps, objectmap, objectterms, datasheet/phildatasheet, echodatasheet, objectsheet, worldexp, templescaling, sagelevel, bloodmoondoc/respawndoc, cooking, cookcalc, bread/howtocookbread, levelcards, directimglink, beedletrades, amiibodrops, glitchsheet, dondon, horsecolors, devicedrain/energycelldrain, hoverbike, hoverbike4.0, goldenwing/infinitywing, railpart/elevatorrail, betterpics, paracopter, bestfuses/fuseideas`
    **Meta Info**
    `dupe1.1.2, dupe1.2.0, dupe1.2.1, downpatch, preventupdates, versioncheck, transferalbum, whereDLC`
    **Reference Images**
    `horseupgrades, ascendmap, cherrymap, cherryareamap, invupgrades, shrinecounts, dmgformula, armortotals, fruitandveggietotals, meattotals, horntotals, gutsandtailtotals, otherparttotals, oretotals, zonaitotals, dragontotals`
Page 2 of 2
'''

HELP_TAGTITLE = '''Here are the options for my `tag` command:'''
HELP_TAG1 = ['''/tag [option]''', '''
`botinfo/userauru, credits, repository, shortcuthelp`''']
HELP_TAG2 = ['''**Tag Command Help**''', '''
`help [page number], help show [page number]`
- *Note: Page number defaults to the 1st page if not specified*''']
HELP_TAG3 = ['''**General Command Help** (For when `/help` isn't available)''', '''
`generalhelp, generalhelp show`''']
HELP_TAG4 = ['''**Story Stuff**''', '''
`postgame, elitepics, permaquests, trueend, ringruins, josha, robbie, finalelocation/finalbosslocation, ritofirst/windfirst/firsttemple`''']
HELP_TAG5 = ['''**Farming Stuff**''', '''
`repsawninfo/bloodmoon/zonairespawn, forcebloodmoon, materialrespawn, shoprestock, chargefarm, starfragment, dragon, arrowfarm, freelynelbows, constructfarm, earlyrupees`''']
HELP_TAG6 = ['''**Equipment Info**''', '''
`octorok, naturalmodifiers, repairlegendary, legendarylist, fusedurability, shieldfuse, fragilematerials/fragilemats, breakitdown/pelison, pristineweapons, mastersword, truedmg, amiiborespawnalt/duskbow/whitesword, botwarmor/missingarmor`''']
HELP_TAG7 = ['''**Mechanics and Hints**''', '''
`bargainer/bargainerstatues, crystalrefinery/refinery, botwdata, uniquehorses, cherry/cherrytrees, depthsmirror, coordsystem, ritofabric, trilbyvalley, moatchasm, mat253/sunpumpkin, greatfairy, hestu/hestulocation, control5/jumpslash, missablelocations, mapcompletiontips, subbosscompletion/monstermedaltips, hornedstatue, dugby, elementdmg, malanya/malanyalocation, midairwing, gleeokstrat, miskobanner, beginnertips/totktips`''']
HELP_TAG8 = ['''**Effects and Builds**''', '''
`defense, bestarmor, bestfuse, gloomdmg, backscratcher, dmgcalc, moisture, weatherattack, gloomattackresist, slipresist, attackupstacking, boneprof`''']
HELP_TAG9 = ['''**Useful Links and Stuff**''', '''
`wiki, fandom/wikimigration, tracker, botwtracker, armorcalc, mapcompletion, shrinefinder, maps, objectmap, objectterms, datasheet/phildatasheet, echodatasheet, objectsheet, worldexp/worldlevel, templescaling, sagelevel, bloodmoondoc/respawndoc, cooking, cookcalc, directimglink, beedletrades, amiibodrops, glitchsheet, dondon, horsecolors, devicedrain/energycelldrain, dispenserprices, combatguide/combattips, missableobjects, gamblinggame/luckytreasureshop, hoverbike, hoverbike4.0, goldenwing/infinitywing, railpart/elevatorrail, betterpics, paracopter, fuseideas, autobuildsharing, voicememories/voicememoryvids`''']
HELP_TAG10 = ['''**Meta Info**''', '''
`dupe1.1.2, dupe1.2.0, dupe1.2.1/dupe1.4.0, 1.2.1FEzuggle/1.2.1FE/1.2.1zuggle, 1.2.1MNF/1.2.0MNF/1.2.1MsgNotFound/1.2.0MsgNotFound, downpatch, preventupdates, versioncheck, transferalbum, whereDLC, timestamp`''']
HELP_TAG11 = ['''**Reference Images**''', '''
`horseupgrades, ascendmap/ascendruinsmap, cherrymap, cherryareamap, koltinstallmap/koltinmap, invupgrades/koroktotals, shrinecounts, dmgformula, armortotals, fruitandveggietotals, meattotals, horntotals, gutsandtailtotals, otherparttotals, oretotals, zonaitotals, dragontotals`''']

HELP_TAGGENSERVER = ['''**Server Stuff**''', '''
`spoiler, piracy/tos, selfpromo/selfpromotion, imgperms, rolerewards, arcaneexp/expsystem, sageofhyrule`''']

HELP_COMMANDSHORTCUT = '''
You can trigger some of my commands from within a message using certain markdowns:
- `/find [search terms]` = `f{search terms}`
- `/findpristine [weapon name]` = `p{weapon name}`
- `/finddispenser [device name]` = `d{device name}`

Just put the terms you would normally use with those commands inside the brackets, and I'll respond to your message just how I would if you used the command!
This is limited to 3 uses per command per message (1 use for `/finddispenser` per message), and I will automatically remove duplicate terms.
'''

HELP_NOTIFY = '''Sending you my response to that command'''
HELP_NOTIFYERROR1 = '''My apologies'''
HELP_NOTIFYERROR2 = ''', but I can't send you my response!. Please try using the slash command or visible version of that command.'''

HELP_BLACKLIST = '''
Here's how to use my blacklist command: 
***Please keep in mind that all of my responses to these commands will be sent to the channel in which you use the command!***

`&blacklist show`
  -Shows the currently blacklisted users and the reasons they were blacklisted

`&blacklist add [userid] [reason (optional)]`
  -Adds a user to the blacklist. Add information after the userid to save the reason they were blacklisted, or other info.

`&blacklist remove [userid]`
  -Remove a user from the blacklist

`&blacklist update [userid] [reason (optional)]`
  -Update a user's blacklist reason/info
'''
# endregion

# region TOTKGeneral Server Stuff
INFO_SPOILERTAG = '''
Please be mindful of any newer players present and spoiler tag any information they might not want to have spoiled for them. 
- You can spoiler tag text by putting "||" on both sides of the spoiler, \|\|like this\|\|.
You can spoiler tag images and videos **when attaching** them: 
- If you are on the desktop app, by clicking the small eye icon above the image.
- If you are on mobile, by tapping and holding on the image to view the options for it.
'''
INFO_RULETOS = '''Please refer to rule 9 in <#1022236312209739846>, which states that promotion of methods or services that involve piracy, hacking, modification of consoles, or illegal emulation is not allowed on this server. Discussion of emulation or modding is permitted, as long as the discussion does not involve information about ***how*** to do either.'''
INFO_SELFPROMOTION = '''
Please keep all self promotion to <#753016129043169402>. In order to post in <#753016129043169402> you will need to have at least the **Member** role (lvl 1 or above).
Please remember that you are not allowed to use this server solely for self promotion, and that the posting of server invites, NSFW stuff, or any of the other prohibited acts listed in the channel description will be dealt with accordingly.
'''

INFO_IMGPERM = '''
In order to be able to post images or embed other stuff on this server, you will need to reach **Traveler** rank (Level 3) or above. 
Use `/level` in <#811092574672388106> to view your current level information.
'''
INFO_ROLEREWARDS = '''
At certain level thresholds, Arcane will award you a role. You can use `/level` in <#811092574672388106> to see your current level information. If you are missing a role that you qualify for, feel free to ask for assistance in <#798676709117132810>.
Use `/tag arcaneexp` for more info about Arcane's experience system.
'''
INFO_ARCANEEXP = '''
You can earn Arcane experience once per minute by sending messages.
- Any extra messages sent during the minute will not increase the exp gained, so consistency of activity is more important than rate of messages sent, if you want to maximize experience gain.
- The possible amount of exp gained per minute is controlled by the server admins, and is random within the set range.
For example, if Arcane is set to award you between 40-100 exp per minute that you chat, then it does not matter whether you send 1 message or 20 messages within that minute, you will still earn between 40 and 100 exp, depending on RNG.
'''

INFO_SAGEHYRULEROLE = '''The "Sage of Hyrule" role is the former "TotK Expert" role repurposed into the TotK Server's own MVP Role. It is no longer recognised as a Staff Role, and does not come with any special permissions. Instead, it is awarded to users who have active participation in the server among other criteria. The Sage of Hyrule role is awarded on a rolling basis at the end of each month and is added at the moderators' discretion.'''
# endregion

# region Story Stuff
INFO_POSTGAME = '''
Legend of Zelda games do not generally have a post-game. Instead, TotK reverts you to your last save before the finale and adds a little star to it. This will:
 -Add a counter to your Purah Pad that tracks your *map completion* percentage
 -Add counters to your Purah Pad that tracks your total quests and character profiles
 -Unlock the option to purchase Elite Enemy Compendium pictures from Robbie
 -Carry over any pictures and Compendium entries you obtained during the finale
 -Add ||Zelda's Sage symbol to the loading screen||
'''
INFO_ELITEPIC = '''After beating the game, you unlock the option to purchase Elite Enemy Pictures for your Compendium from Robbie.'''
INFO_PERMQUESTS = '''You cannot permanently complete the quests ||"Destroy Ganondorf"|| or ||"Find Princess Zelda"||, as they are completed during the finale of the game.'''
INFO_TRUEEND = '''If you have collected every memory, then ||a new cutscene featuring all of the Sages will play after the credits.||'''
INFO_RINGRUINQUEST = '''The main quest ||"Secret of the Ring Ruins"|| can be begun by speaking to Tauro and Paya in Kakariko Village after you have completed ||"Crisis at Hyrule Castle"||.'''
INFO_JOSHA = '''Josha is Purah's head of Depths Research and can be found in her workshop in Lookout Landing. She provides a number of quests designed to lead you to important locations within the Depths, so anytime you have a question about the Depths it might be a good idea to see if she has any information for you.'''
INFO_ROBBIE = '''
Robbie is the Head of Purah Pad Development, and offers a few different upgrades to your Purah Pad throughout the game. During "Camera Work in the Depths" he can be found near Iayusus Lightroot, where he will unlock the Camera functionality of your Purah Pad.

In order to get the rest of your Purah Pad upgrades, you will need to complete Josha's quest, "A Mystery in the Depths" (which also requires completion of at least one part of "Regional Phenomena"), at which point Robbie will set off for his lab in Hateno Village.
There, Robbie can provide you with the Sensor, Sensor+, Travel Medallions, and Hero's Path Mode for your Purah Pad, although he will request data in exchange for some of these.
'''
INFO_FINALEAPPROACHING = '''
If you happen to be worried that TotK's final boss is in Hyrule Castle, don't be! The final boss is not located in Hyrule Castle, and you will ***definitely*** know when you're approaching it. Once you do get to the point where you're approaching the final boss, don't be afraid to place down a Travel Medallion so you can go prepare more before taking the finale on.
'''
INFO_RITOFIRST = '''
Purah will tell you to head for the Rito Regional Phenomenon first for a good reason; Along the way to Rito Village, you can encounter a number of tutorials for the game's systems:

- At New Serenne Stable, you can encounter a lot of nearby horses that you can easily tame and register with the stablehand, who explains the stabling system to you. If you've played BotW before, you may find a neat feature. (Use `?tag botwdata`)
- Nearby New Serenne Stable, you can find Impa, who introduces you to the Geoglyphs, which are an important part of this game's storyline, and following her advice will allow you to view it in the proper order.
- Between New Serenne Stable and Lindor's Brow Skyview Tower, you will find Hestu, who you can return Korok Seeds to in exchange for inventory upgrades. (Use `?tag hestu`)
- Closer to Rito Village, you will find the Lucky Clover Gazette, which will allow you to start an important Side Adventure that leads to the ability to upgrade your armour later on, as well as providing some small boosts in cash for the early-mid game. (Use `?tag greatfairy`)
- Rito Village's Main Quest also functions as a steady tutorial for the game's more intense temperature management, as you are expected to have gathered enough Rupees by the time you reached the village to purchase some cold resistance armour. (Use `?tag earlyrupees`)
'''
# endregion

# region Farming Stuff
INFO_RESPAWNINGTITLE = '''
TotK uses a set of timers to determine when to respawn enemies and equipment.
'''
INFO_RESPAWNING = '''
**Blood Moons**
Blood Moons control when equipment and most enemies respawn, but not Construct enemies or materials/animals.
- Starting from when Link receives the Main Quest "The Closed Door", a timer will count until it reaches 6 in-game days (144 minutes) of unpaused gameplay.
- Once the timer goes over 6 in-game days, TotK will attempt to cause a Blood Moon on the next midnight, at which point the Blood Moon timer is reset to 0.
- Blood Moons can only occur if Link is outside of a dungeon/Shrine and on the Surface or in the Sky at 9pm, unless a save made after 9pm is loaded.
- Sleeping through the night at a bed or campfire while the timer is over 6 days will still cause a Blood Moon, if Link is in a valid area.
- Blood Moons cannot occur until Link has touched the Surface and unlocked the map layer for it.

**Zonai Respawn**
Zonai Respawns control when Soldier Constructs, Captain Constructs, and Flux Constructs respawn.
- Just like for Blood Moons, a timer starts when Link begins "The Closed Door", counting up until it reaches 6 in-game days (144 minutes) of unpaused gameplay.
- After the timer reaches 6 in-game days and the in-game clock passes midnight, the game will set all the Constructs as "ready to respawn", however they will not respawn immediately.
- Once Link warps or enters/exits a Shrine, all Construct enemies will respawn. Closing and re-opening the game or loading a save does not cause them to respawn.
- The game will not set the Constructs as "ready to respawn" until the clock passes midnight *after* Link has unlocked the Surface map layer.
This is how Zonai Respawns are currently understood, so it is possible that there are triggers for the Zonai Respawn other than warping and entering/exiting a Shrine.

**More Info**
For info about material/animal respawns, use `/tag materialtimer`.
If you'd like more details on how the respawn mechanics work, please check out bjm's [document on respawn mechanics and "No Blood Moons" playthroughs](<https://docs.google.com/document/d/1w59IZh1z7Empep1kCjqXLHuTPqu5DHnwKdYEzU3TC60/edit?usp=sharing>)
'''
POINT_FORCEMOON = '''
Here's are some links to examples of how to force a Blood Moon to occur in TotK:
- [Rock Wall Opal Method](<https://youtu.be/cBolBE0792k>)
- [Water Shock Method](<https://youtu.be/WU01EY3dGc8>)
'''
INFO_MATERIALTIMER = '''
TotK's map is divided into a 10x8 grid of "cells" that are used to determine when to respawn materials and animals. Every minute, each material/animal has a 1% chance to respawn, as long as Link is at least half a "cell" away from that material/animal's "cell".
'''
INFO_SHOPRESTOCK = '''Shops restock at midnight. You can make them restock by waiting at a campfire or bed, then reloading the shop by fast traveling, or saving and reloading. Menu-based shops only require passing time, as opening the shop causes them to reload.'''

INFO_CHARGEFARMTITLE = '''You can farm Crystallized Charges by:'''
INFO_CHARGEFARM = '''
- Defeating ||Master Kohga at each Abandoned Mine he appears at|| and ||each Temple Boss Rematch||, all of which each give a chest containing a Huge Crystallized Charge (worth 100 normal Crystallized Charges) the first time you defeat them.
- Defeating Sub-Bosses in the Depths, which drop a Large Crystallized Charge (worth 20 normal Crystallized Charges) every Blood Moon.
- Visiting various locations in the Depths, as some of them have treasure chests containing a Large Crystallized Charge.
  Here are the totals for each type of location:
  - 34/34 Yiga Clan Bases
  - 21/29 Canyon Mines
  - 9/10 Abandoned Mine Bonus Chests
  - 11/15 Groves
  - 3/4 Lavafalls
  - 5 Misc. Locations: Blupee Burrow, Gerudo Underground Cemetery, Dracozu Altar, Secret Spring of Revival, and the Ancient Observation Deck
'''
POINT_STARFARM = '''
Here's a link to an explanation on Star Fragment farming in TotK: 
https://www.reddit.com/r/zelda/comments/14ks4ci/totk_star_fragment_farming_guide_get_one_per/
'''
POINT_DRAGON = '''
Here's a link to a guide on Dragons and Dragon Part Farming in TotK: 
https://youtu.be/Pk27gun8xOw
'''
POINT_ARROWFARM = '''
Here's a link to a guide on farming arrows in TotK:
https://youtu.be/wR-6ThhtO5U
'''
POINT_FREELYNELBOWS = '''
Here's a link to a guide on obtaining free Lynel Bows in TotK:
https://youtu.be/EvkR-10p2t4
'''
POINT_CONSTRUCTHORNFARM = '''
Here's a link to a guide on where to farm Construct Horns inside Proving Grounds Shrines:
https://www.reddit.com/r/TOTK/comments/15d3ksj/proving_grounds_shrines_construct_farming/
'''

POINT_EARLYCASH = '''
Here's a link to a guide for getting rupees in early game: 
https://youtu.be/BJ5vAEiMwq8
'''
# endregion

# region Equipment Info
INFO_OCTOROK = '''
You can repair and modify any non-Legendary equipment by dropping it on the ground in front of a Rock Octorok in Eldin Canyon. 
The Octorok will restore the Base and Bonus Durability of the equipment, as well as any equipment (not materials) fused to it. 

In addition, Rock Octoroks will modify the base equipment that they repair, from Tier 0 (no modifier) to Tier 1 (blue/white icon), Tier 1 to Tier 2 (orange icon), or Tier 2 to Tier 2. The modifier applied by the Octorok is random, based on the available modifiers for that equipment and the tier it is upgrading to. 
Please take a look at this spreadsheet to see the available modifiers and values for each modifier: 
<https://docs.google.com/spreadsheets/d/12b8vsytM41T3nZrkXqiTrD3zejF1827-_10Os1yZIoo/edit?usp=sharing> 

You can save next to an Octorok before giving it equipment, and reload that save to reroll the modifier you get. 

Each Octorok can only be used once per Blood Moon, and the area will need to be reloaded for the refresh to take effect.
'''
POINT_NATURALMODIFIERS = '''
Here's a link to the Natural Modifier sheet for TotK:
https://docs.google.com/spreadsheets/d/12b8vsytM41T3nZrkXqiTrD3zejF1827-_10Os1yZIoo/edit?usp=sharing
'''
INFO_REPAIRLEGEND = '''
You can repair any Legendary equipment by fusing it to a non-Legendary weapon or shield, then repairing that with a Rock Octorok. Then take it to the Break-A-Part Shop at Tarrey Town, which is located in the Akkala Highlands. Have Pelison break it down, and your Legendary equipment will be fully repaired.

If you wish to repair a piece of Legendary equipment without losing its modifier, please take a look at this guide: <https://youtu.be/a0slhXe6jzU>
'''
INFO_LEGENDLISTTITLE = '''The following equipment cannot be modified by Rock Octoroks and is usually referred to as Legendary equipment:'''
INFO_LEGENDLIST = '''
- Master Sword 
- Demon King's Bow 

**amiibo Weapons:**
- Sea-Breeze Boomerang 
- Sword of the Hero 
- White Sword of the Sky 
- Biggoron's Sword 
- Dusk Claymore 
- Fierce Deity Sword 
- Dusk Bow 
- Sea-Breeze Shield 

**Champions' Arms:** 
- Scimitar of the Seven 
- Boulder Breaker 
- Lightscale Trident 
- Great Eagle Bow 
- Daybreaker 

**Magic Weapons:**
- Magic Rod 
- Magic Scepter 
- Magic Staff
'''

INFO_FUSEDURABILITY = '''
Each weapon has a Base Durability and a Bonus Durability, which is unlocked while something is fused to the weapon. 
Bonus Durability Values: 
-Stal Enemy Arms = 3 
-Gerudo Weapons, excluding the Scimitar of the Seven = 5 
-Tree Branches, Tools, Rusty Weapons, Royal Guard Weapons, and Gloom Weapons = 10 
-All other weapons = 25 

Bonus Durability is a property of the base weapon, and any Bonus Durability used will not be restored by fusing something else to the base weapon. Aside from materials that break in one hit, such as Gibdo Bones and Ancient Blades, all materials will last until the base weapon breaks. When fusing equipment to a weapon, the base weapon will still unlock its Bonus Durability, but the fused equipment will not. The durability of both equipment will be drained on hit.

When fusing equipment to a weapon or shield, the fused equipment will lose its modifier, but if it is a weapon, its Bonus Durability will be restored to maximum.
'''
INFO_SHIELDFUSE = '''
Shield Fusions are primarily used for utility. 
-When Fused to a shield, objects with the "Shield Bash Attack" Fuse property will make Link's parry deal damage, or add to its existing damage, for Lynel shields.
-The only object that increases a shield's guard stat is the Long Lava Slab, which increases it by 1.
-Shields do not have Bonus Durability, meaning that they do not get any increase in durability when Fused.
'''
INFO_FRAGILEMATERIALS = '''
Certain materials, such as Gibdo Bones or Ancient Blades, are fragile and will break after one hit when Fused to a weapon. This is not connected to durability, as materials **do not** have durability.
When in scenarios where weapon durability is not drained, such as mounted attacks on a Lynel, fragile materials will still break after one hit.
If a fragile material Fused to a full durability weapon breaks from a jump attack, the weapon will not lose durability from the jump attack.
'''
INFO_BREAKITDOWN = '''
You can break down most Fused weapons and shields into their base equipment and Fuse material by paying 20 rupees to Pelison at the Break-a-Part Shop in Tarrey Town. 
'''

POINT_WEAPONSINTACT = '''
Here's a link to an explanation of Pristine weapon mechanics in TotK:
<https://docs.google.com/document/d/1hEXB9TDTKJ-Mdv7PbY_tYe6A9gWIMOXJsASVoFAxl2I/edit?usp=sharing>
'''

INFO_MASTERSWORD = '''The Master Sword has a base damage of 30, which increases to 45 when it is Awakened (nearby Gloom-Wreathed enemies). It has a Base Durability of 40 and a Bonus Durability of 25, but it does not currently recharge its Bonus Durability, meaning that after it runs out of energy for the first time it will only ever have a Total Durability of 40. When facing Phantom Ganon or ||Ganondorf||, its base damage increases to 60, and it does not lose any durability on use.'''
INFO_TRUEDAMAGE = '''
In TotK, the displayed attack numbers for spears and two-handed weapons do not reflect their actual attack power.
- The true attack power of spears is roughly 75% of what is displayed, rounded up
- The true attack power of two-handed weapons is roughly 5% higher than what is displayed, rounded down

These multipliers also affect modifiers to the weapon, such as the Fused item, Attack Up from a modifier, and Zonaite-Powered/Strong Fusion. They do not apply to temporary weapon buffs, such as those from the Attack Up effect or conditional weapon Traits like Water Warrior.
'''
INFO_ALTAMIIBOWEAPONSOURCE = '''
The White Sword of the Sky and the Dusk Bow cannot be purchased from Baragainer Statues. Instead, the Dusk Bow can found at the top of Hyrule Castle every Blood Moon. The White Sword of the Sky can be reobtained from the Mother Goddess Statue by bringing her Dinraal's Claw, Farosh's Claw, and Naydra's Claw.
'''
INFO_MISSINGARMOR = '''
The following armors from BotW are not available in TotK:
-Old Shirt and Well-Worn Trousers
-Warm Doublet
-Nintendo Switch Shirt
-Salvager's Set
-Ancient Set
-Gerudo Vai Set
-Phantom Ganon Set (renamed to Evil Spirit Set)
-Thunder Helm (replaced by Lightning Helm)
-Champion's Tunic (nerfed into Tunic of Memories)
'''
# endregion

# region Mechanics/Hints
INFO_BARGAINERSTATUE = '''
Bargainer Statue merchants offer rare equipment and materials in return for Poes to guide into the afterlife. There are 7 in the game, 1 found at Lookout Landing, and 6 found within the Depths. 
Each Bargainer Statue in the Depths is found ||directly below a Great Goddess Statue on the Surface or in the Sky||. 

All Bargainer Statue merchants will sell you Dark Clumps, Muddle Buds, Puffshrooms, Bomb Flowers, and the armors unlocked by visiting each Bargainer Statue merchant.

Aside from the Dusk Bow and White Sword of the Sky, amiibo weapons/armor and BotW DLC armor can be purchased from Bargainer Statues **in the Depths** after you have obtained the gear piece at least once.
They will also sell you the Magic Rod, Magic Scepter, and Magic Staff.
'''
INFO_CRYSTALREFINERY = '''
Crystal Refineries are "shops" where you can trade 100 Crystallized Charges for an Energy Well, permanently increasing your Energy Cell capacity, up to a max of 48 total Wells (or 16 total Cells/"Batteries"), including the 3 Wells you start with.
There are only 2 Crystal Refineries that can be found within TotK:
 -One found directly in front of Nachoyah Shrine (the Recall tutorial Shrine on the Great Sky Island)
 -One found just north of Lookout Landing

After you have fully upgraded your Energy Cell to 48 total Energy Wells, you can use your Crystallized Charges at Crystal Refineries to purchase any Zonai Device. Each device costs 3 Charges per capsule, except for Big Batteries, which are 30 Charges each.
'''

INFO_BOTWDATA = '''
TotK automatically imports some of your BotW *Normal Mode* data into TotK:
-When you talk to a stablehand for the first time, any registered horses you had in BotW will be in your stables, including any unique horses, which will not spawn in TotK's world if you import them.
-If you hang your Champion's Ballad photo from Kass on the wall in Link's House in BotW, then the photo will be in Zelda's House in TotK. This can be done at any point in your TotK playthrough.
'''
INFO_UNIQUEHORSES = '''
There are 6 unique horses available to register in TotK:
Note: If you imported a unique horse from botw, then it will not spawn in the wild in TotK.

-Giant White Stallion - Found ||east of the Horse God Bridge in Faron Highlands.||
-Giant Horse ("Gerudo") - Found ||at eastern Hateno Beach.||
-Zelda's Golden Horse - Found ||in northern North Tabantha Snowfield|| after starting the side adventure "Potential Princess Sightings!" and will be available for registering after completing the quest, "Zelda's Golden Horse."
-Spot - Found ||southwest of Lookout Landing|| after starting the quest "Spotting Spot," the completion of which will unlock him for registering.
-Royal White Stallion - Found ||north of Skull Lake in Deep Akkala.||
-Epona - Spawns from scanning the Super Smash Bros. Link and Twilight Princess Link amiibo.
'''

INFO_CHERRYTREE = '''If you are having trouble finding caves, try offering some fruit to a cherry blossom tree. Doing so will reveal ALL Surface cave entrances (aside from Ancient Zora Waterworks) in the surrounding area of the map for 24 minutes of unpaused gameplay, although towards the end of this time period the markers will become very faint. These markers will not disappear early if you save and reload, but will disappear if you close the game and re-open it, or activate a different tree.'''
INFO_DEPTHSMIRROR = '''
Hyrule's Depths mirror its Surface; Terrain elevation is usually inverted, and bodies of water on the Surface are almost always impassable walls in the Depths. 
If you are in an area of the Depths and you do not have the map for it yet, try opening your Surface map and then closing it. This will display the Surface on your minimap, aiding in navigation.
'''
INFO_COORDSYSTEM = '''
You can think of the coordinates shown in-game as being X, Z, Y, where positive X is East on the map, positive Z is North on the map, and Y is your height.
The coordinate system internally used by the game can be visualized as X, Y + 105, -Z.
The Object Map coordinate system is based on the internal coordinate system, but it flips the Z axis to better line up with the in-game shown coordinates: X, Y + 105, Z.

For example, there is an Apple found at `0402, -1344, 1541` in-game, but the game internally spawns it at `402.47, 1646.41, 1343.78`, and the Object Map displays its location as `402.47, 1646.41, -1343.78`.

If you need to see what the shown in-game coordinates are for an object on the Object Map, you can go to the Settings menu and select "Use In-Game Coordinates", or use my `/coordconvert` command.
'''

INFO_RITOFABRIC = '''The Ordinary and Nostalgic Fabrics are the stand-ins for the Rito Fabric, as the Paraglider was made by the Rito for Hylians.'''
INFO_TRILBYVALLEY = '''The Trilby Valley Flame Gleeok can be found in the Skies high above Eldin Canyon, at `2238, 694, 795`.'''
INFO_MOATCHASM = '''In order to reach the Depths underneath Hyrule Forest Park (to the east of Hyrule Castle), try flying over the moat while searching the water level of the west side of the island for a small opening with a Chasm inside.'''
INFO_SUNPUMPKIN = '''Compendium Entry #253 is the ||Sun Pumpkin||, a material that is not found within Hyrule until the completion of the quest "Homegrown in Hateno," which you can begin by speaking to Reede in the fields near the entrance to Hateno Village, after completing "The Mayoral Election."'''
INFO_GREATFAIRYQUEST = '''
After speaking to Traysi at the Lucky Clover Gazette and beginning the Side Adventure, "Potential Princess Sightings!" you can speak to Penn and the Stable Trotters at Woodland Stable to begin the Side Adventure, "Serenade to a Great Fairy."
'''
INFO_HESTULOCATION = '''
The Korok known as Hestu can use the Korok Seeds that you've collected to upgrade your weapon, bow, and shield inventories.
- Hestu can initially be found in between the road northeast of New Serenne Stable and Lindor's Brow Skyview Tower at `-1718, 1093, 209`. After completing his quest, "Hestu's Concerns" at this location or completing one part of the quest "Regional Phenomena," he will move to Lookout Landing. 
- If you have defeated ||the Phantom Ganon within the Deku Tree Chasm and restored Korok Forest||, then he will move to Korok Forest permanently, regardless of his quest progress or whether you've spoken to him before in Lindor's Brow or Lookout Landing. 
- You will be able to start/complete his quest in both Lookout Landing and Korok Forest if you missed doing either previously. 
- There is also no limit to the amount of inventory expansions you can receive at Lookout Landing.
'''
INFO_JSCONTROL = '''The 5th Special Control is Jump Slash, and is obtained by reading the journal at the Monster Control Crew camp for Hoz's Squad. The camp can be found along the road west of Hyrule Field Chasm, or north of Dueling Peaks Stable, depending on your Side Adventure progress. If the camp is not at either location, wait until after a Blood Moon, and try those locations again.'''
INFO_MISSABLELOCATIONSTITLE = '''Here are some of the most commonly missed locations for TotK:'''
INFO_MISSABLELOCATIONSHEADERS = [
    '''Surface Locations:''',
    '''Depths Locations:''',
    '''Hidden Locations:'''
]
INFO_MISSABLELOCATIONS = [
    '''
- East and West Passages at Hyrule Castle
- Sherfin's Secret Hot Spring
- Dragon Bone Mire
- Kolomo Garrison Ruins
- Gatepost Town Ruins
- Water Reservoir
- Castle Town Watchtower
- Faron Woods
- Sarjon Bridge
- Ash Swamp
- Oren Bridge
- Luto's Crossing
- All 3 Sokkala Bridges
- Gero Pond
- Royal Ancient Lab Ruins
- Lanayru Road - West Gate''',
    '''
Make sure to visit every Canyon Mine and Lavafalls you can see on the map
- Papetto Grove
- Dracozu Altar
- Hickaly Grove
- Midla Grove
- Ginner Grove
- Retsam Grove
- Blupee Burrow 
- Applean Grove''',
    '''
These still count for 100%, despite not appearing on the map. To confirm that you have them, visit them in-person and make sure you see their name appear in the bottom left.
- All Dungeon Rooms/Floors
- Statue of the Eighth Heroine Room
- The locations on the path to the finale of the game.
'''
]
INFO_MISSABLELOCATIONSFOOTNOTE = '''Original Surface and Depths lists by Dixon#8583'''
INFO_MAPCOMPLETIONTIPS = '''
If you are attempting to earn 100% map completion in TotK, here are some tips to make it easier:
- Watch this [video](<https://youtu.be/wvL0YnIjyCU>) to get an idea of what exactly counts towards map completion.
- Use my `/tag missablelocations` command to see some of the more commonly missed locations.
- Use my `/tag tracker` command to get a link to the 100% Tracker for TotK, which has every location and icon needed for map completion, so feel free to use it to check off each icon and location as you go.
- Double check that you have all icons first, such as Dispensers, Chasms, Forge Constructs, etc., as they do count towards map completion. Don't forget the Smithing Construct either!
- Make sure you have all the hidden locations, as detailed in `/tag missablelocations`.
- Once you have verified that you have all the icons and commonly missed locations, start checking off the named locations on the 100% Tracker, one-by-one.
'''
INFO_SUBBOSSCOMPLETIONTITLE = '''
Here is a recommended strategy for checking all the Sub-Boss locations for a Monster Medal:
'''
INFO_SUBBOSSCOMPLETIONHEADERS = [
    '''1. Use an interactive map''',
    '''2. Stamp all the locations''',
    '''3. Check every location''',
    '''4. Save your checked locations''',
    '''5. Double Check'''
]
INFO_SUBBOSSCOMPLETION= [
    '''- Look up an interactive map to find all the locations of the Sub-Boss you're after. [Zelda Dungeon](<https://www.zeldadungeon.net/tears-of-the-kingdom-interactive-map/>) or [Zelda Universe](<https://zeldamaps.com/?game=TotK>) work well for this. Make sure that you do not have any of the Sub-Boss's locations checked off on the map already.''',
    '''- Using **one type of stamp**, mark all the locations on your in-game map.''',
    '''- Head to each location in-game, and once you've verified that you've defeated the Sub-Boss (either by killing it or checking that it has a "Defeated" star next to its healthbar), ***change the stamp for that location to a different stamp.*** This way you will have stamps for unchecked locations, and stamps for checked locations.''',
    '''- Once you've changed every stamp that you placed, start checking off each location on the interactive map, removing the "checked" stamp on your in-game map for each location as you record it on the interactive map.''',
    '''- Verify on the interactive map that you didn't miss any locations when you originally placed your stamps on your in-game map. If you did, then just go check them in-game and mark them as completed on the interactive map.'''
]
INFO_HORNEDSTATUE = '''After completing one part of "Regional Phenomena," a new opening can be found in the Emergency Shelter in Lookout Landing, through which you will find a statue with an ominous aura. This Horned Statue will allow you to trade Heart Containers for Stamina Vessels, and vice versa, for the cost of 20 rupees each.'''
INFO_DUGBY = '''
Dugby's first quest is "The Ancient City Gorondia!" and has no pre-requisites in order to unlock. Dugby can be found at `1744, 2585, 427` for this quest.

Dugby's second quest is "The Ancient City Gorondia?" and requires the completion of "Yunobo of Goron City" and at least 30 minutes of unpaused gameplay to have passed since the completion of his first quest. Dugby can be found at `1614, 2399, 397` for this quest.
'''
INFO_BASEELEMENTALDMG = '''
Every enemy takes a specific amount of base damage from each element, although some element sources can have a bonus damage that is added to the base damage.
Here's a video going over the specifics for elemental damage in TotK:
https://youtu.be/3vJc-ko00Gk
'''
INFO_MALANYALOCATION = '''
The Horse God Malanya can revive and upgrade your registered horses in TotK. You can find his spring at Bloodleaf Lake in Deep Akkala, north of East Akkala Stable.
You can bring him out of his bud by giving him an Endura Carrot, and he will ask for a Roasted Endura Carrot in order to revive any of your deceased horses.

In order to improve a horse's stats, Malanya will ask for certain meals to give him the energy he needs for the upgrade. To upgrade any stat to 2 stars, you will need to bring him a single Fried Wild Greens meal.
Use `/tag horseupgrades` to see the meals needed for the rest of the upgrades.

Malanya cannot upgrade the stats for Epona, the Giant White Stallion, and the Giant Horse ("Gerudo"), as they like themselves the way they are.
'''

INFO_GLEEOKSTRAT = '''
The trick to taking down a Gleeok is to use Eyeball arrow fusions while avoiding its attacks or staying behind cover. It is also a good idea to use updrafts or shield fusions to gain height and shoot arrows while in midair. Multi-shot bows are strongly recommended for this.
- Flame Gleeok heads take 2x damage from ice attacks and 1.5x damage from water attacks.
- Frost Gleeok heads take 2x damage from fire attacks.
'''
INFO_MIDAIRWING = '''
Here are the steps to deploy a Wing midair in TotK:
1. Let the Left Stick go neutral while paragliding, so that Link is falling straight down.
2. Open the Quick Menu or Pause Menu and drop a Wing.
3. Close the menu, then immediately tilt the Left Stick up to move forward.
4. Close the paraglider to land on the Wing.
'''
INFO_BEGINNERTIPSTITLE = '''
Here are some beginner tips for players new to TotK:
'''
INFO_BEGINNERTIPSHEADERS = [
    '''1. Don't be told where to go''',
    '''2. Pay close attention to what you have to work with, both in your inventory and the environment around you''',
    '''3. Never skip dialogue''',
    '''4. Remember your powers''',
    '''5. Early-game strength'''
]
INFO_BEGINNERTIPS = [
    '''- TotK is built around player freedom, meaning that there is no "right" or "wrong" order to do anything, for the most part. Just do whatever you want to do, when you want to do it.''',
    '''- This is a game filled with small tutorials that are designed to teach players about its mechanics. Make sure to consider everything that the game provides you, and to what you've collected so far, as it may just give you one or more solutions to a problem.''',
    '''- Make sure to read all dialogue, **ESPECIALLY** from key characters, as it is very often that they will provide hints and other important information. It is also a good idea to ***check your Adventure Log*** anytime you are stuck on a quest, as important clues are usually recorded there.''',
    '''- Keep all of your powers in mind, you never know when one of them will be the solution to a problem you're facing.''',
    '''- When it comes to early-game, the best weapons you can make are whatever-you-have Fused to whatever-you-have. As you continue playing you will find better weapons and better materials to Fuse to them, so don't worry too much about finding the best stuff immediately.'''
]
# endregion

# region Effects/Builds
INFO_DEFENSESTAT = '''
Every enemy attack has two components: the enemy's base damage for that specific attack, plus the damage of the weapon they are holding (if applicable to that attack). The damage you take from the attack is then calculated by subtracting your total defense from the enemy attack.
'''
INFO_BESTARMOR = '''
There isn't really a "best" armor in TotK, but some sets are useful for specific things. 

For maximum defense, you might want: 
-Diamond Circlet, Amber Earrings, Cap of the Wild, Soldier's Helm, or Zonaite Helm 
-Champion's Leathers 
-Trousers of the Wild, Soldier's Greaves, or Zonaite Shin Guards 

 For Attack Up: 
 -The Barbarian Set and the Fierce Deity Set are identical stat-wise. The only differences between the two are visual design and upgrade materials. 

 For Maximum Damage: 
 -Both the Radiant Set and the Evil Spirit Set grant Bone Proficiency, which when paired with a Molduga Jaw weapon and lvl 3 Attack Up from a meal grants the highest damage increase.
 '''
INFO_BESTFUSE = '''
When it comes to the highest damage Fuse materials, these are usually considered the best:
- Silver Lynel Saber Horn - For consistent high damage
- Molduga Jaw - Highest possible damage, when combined with Bone Prof. and Attack Up
- Gleeok Horns - Best damage for elemental materials, and have unlimited elemental energy
'''
INFO_GLOOMDAMAGEFORMULATITLE = '''
The Gloom damage you take from enemy attacks is based on the physical damage you take after your current defense is subtracted from the attack's damage.
`ROUNDUP(0.075 * Damage Taken) + 1 if Damage Taken is a multiple of 40`

Here is a list of the damage ranges that correlate to each heart of Gloom damage taken.
'''
INFO_GLOOMDAMAGEFORMULA = ['''
```  1 -  13: 1
 14 -  26: 2
 27 -  39: 3
 40 -  53: 4
 54 -  66: 5
 67 -  79: 6
 80 -  93: 7
 94 - 106: 8
107 - 119: 9
120 - 133: 10
134 - 146: 11
147 - 159: 12
160 - 173: 13
174 - 186: 14
187 - 199: 15
200 - 213: 16
214 - 226: 17
227 - 239: 18
240 - 253: 19
254 - 266: 20```
''', '''
```267 - 279: 21
280 - 293: 22
294 - 306: 23
307 - 319: 24
320 - 333: 25
334 - 346: 26
347 - 359: 27
360 - 373: 28
374 - 386: 29
387 - 399: 30
400 - 413: 31
414 - 426: 32
427 - 439: 33
440 - 453: 34
454 - 466: 35
467 - 479: 36
480 - 493: 37
494 - 506: 38
507 - 519: 39
520+     : 40```
''']

INFO_BACKSCRATCH = '''
The current maximum damage that you can consistently output can be referred to as a Lynel Backscratcher build. Take a Pristine Royal Guard's Claymore with a +10 Attack Up modifier, fuse a Molduga Jaw to it, then wear it down until it has 1 durability left. 
Then wear a Bone Proficiency armor set and eat a level 3 Attack Up meal, and take the weapon and only use it for mounted attacks on a Lynel. The mounted attacks take no durability, so you can continually deal last hit critical damage with the almost broken claymore. 

Here is the full math behind this:
rounddown(42 Base Weapon Damage + rounddown((10 Modifier Buff + 32 Molduga Jaw Fuse Damage) * 1.052632 Two-Handed Weapon Multiplier) * 1.5 Attack Up Meal * 1.8 Bone Proficiency * 2 Breaking Point * 2 Last Hit Critical) = 928 total damage per hit.
'''
POINT_DMGCALC = '''
Here's a link to Phil's Damage Calculator for TotK:
<https://philidea.com/totk-calculator>
Please feel free to [submit feedback](<https://docs.google.com/forms/d/e/1FAIpQLSdWgQW8VGALbCsqE25iIV-nFlz37l-pYmLtYqz4dm_N9TTzAQ/viewform>) if you find any potential errors or bugs!
'''

POINT_ADDEDEFFECTWIKI = '''
Here is a link to the Zelda Wiki page for Added Effects:
<https://zeldawiki.wiki/wiki/Added_Effect>
'''
POINT_SETBONUSWIKI = '''
Here is a link to the Zelda Wiki page for Set Bonuses:
<https://zeldawiki.wiki/wiki/Set_Bonus>
'''
INFO_MOISTURE = '''The Froggy armor set pieces each have a hidden effect called Moisturizing, which increases the length of time that Link will be wet for, up to a max of 4 minutes, depending on the water source used.'''
INFO_WEATHERATK = '''The Weather Attack effects do not increase physical weapon damage. They add an elemental AoE to combo finishers and charge attacks, which increases in size with higher effect levels and has a bonus elemental damage of 5, regardless of level. The Weather Charge set bonus just gives you Quick Charge when active.'''
INFO_GLOOMATKRES = '''The Gloom Attack Resist set bonus does not have any impact on gloom attacks. It only adds a fourth gloom resistance heart.'''
INFO_SLIPRESIST = '''Slip Resistance increases the amount of time that Link can climb on slippery surfaces before slipping. With levels 1/2/3 of Slip Resistance, Link will be able to climb on slippery surfaces for 6/8/10 seconds before slipping. Slip Proof is the Froggy Armor set bonus, and makes Link immune to slipping.'''
INFO_ATKSTACK = '''The Attack Up effect can only stack up to a total of level 3 (for 1.5x damage), combining both armor and meal effects.'''
INFO_BONEPROF = '''
"[Stal] Disguise; Bone Weap. Prof." is the set bonus for the Evil Spirit set and Radiant set.
The Bone Proficiency effect multiplies bone weapon damage by 1.8x, and stacks with lvl 3 Attack Up from a meal.

The Evil Spirit set pieces each have Stealth Up, and cannot be upgraded, but they grant the set bonus at base level. The Evil Spirit set can be acquired by ||completing the quests that begin at each of the three labyrinths.||

The Radiant set has no innate effects, but can be upgraded and grants the set bonus at 2 stars. It can be purchased from the Armor Shop in Kakariko Village.
'''
# endregion

# region Reference Info
POINT_WIKI = '''
Here's a link to the wiki for The Legend of Zelda:
<https://zeldawiki.wiki/wiki/Main_Page>
'''
POINT_FANDOMBAD = '''
Here's a link to a video explaining the situation surrounding Fandom and wiki migration:
https://youtu.be/qcfuA_UAz3I
'''

POINT_TRACKER = '''
Here's a link to the 100% Tracker Spreadsheet for TotK: 
https://docs.google.com/spreadsheets/d/1mRHxETl2bYvpRBGV7VzeW0bCdpmEbJJdt7aWAw9T0rY/edit?usp=sharing
Please feel free to make a copy for yourself so you can check off your progress by selecting `File -> Make a Copy`.
'''
POINT_BOTWTRACKER = '''
Here's a link to the 100% Tracker Spreadsheet for BotW: 
https://docs.google.com/spreadsheets/d/14cZbMhJsQ5iSINOVSfYmnloZT6rzmxpMd3-DT4lyRUc/edit?usp=sharing
Please feel free to make a copy for yourself so you can check off your progress by selecting `File -> Make a Copy`.
'''
POINT_PHILARMORCALC = '''
Here's a link to make a copy of Phil's Armor Material Calculator:
<https://docs.google.com/spreadsheets/d/1gzS-kViCZ6c4GCDdUFiwfx_Fih2sbcwJm5czzKLJvGo/copy>
'''
POINT_MAPCOMPLETION = '''
Here's a link to an explanation of what counts towards Map Completion in TotK:
https://youtu.be/wvL0YnIjyCU
'''
POINT_SHRINEFINDER = '''
Here's a link to a website that can help you find what Shrines and Lightroots you are missing:
<https://www.haokepeng.com/zelda>
'''
POINT_SHRINEFINDER2 = '''
Here's a link to a website that can help you find what Shrines and Lightroots you are missing:
<https://www.haokepeng.com/zelda>
If you are having trouble using this site, please feel free to head to <#753016129328250964> and post screenshots of your maps so someone can help you find what you're missing.
'''

POINT_INTERACTMAPS = '''
Here are some links to interactive maps: 
Zelda Universe: <https://zeldamaps.com/?game=TotK> 
Zelda Dungeon: <https://www.zeldadungeon.net/tears-of-the-kingdom-interactive-map/> 
AeonSake: <https://totk.aeonsake.com/> 

The Object Map doesn't have the same features as other interactive maps, but it is still very useful. Use `/tag objectmap` for more info.
Object Map: <https://objmap-totk.zeldamods.org/#/map/z2,0,0>
'''
INFO_OBJECTMAPTITLE = '''
The Object Map is a very powerful tool for locating things within TotK: 
https://objmap-totk.zeldamods.org/#/map/z2,0,0 
'''
INFO_OBJECTMAP = '''
- Click on the **"Help" button below the search bar** to see some information on what terms to use.
- **If you're on mobile**, use the magnifying glass button to close the Search menu and view the map.
- You can **change what layer of the Object Map is shown** with the Layer button in the top right corner.
- The Filters menu, found below the Search menu, will allow you to **reveal different icons and sections** on the map.
- You can use these terms to filter search results by map level:
  - `surface` (Includes `cave`)
  - `cave`
  - `depths`
  - `sky`
- Use `OR` and `NOT` in your search to show more results or **filter out results you don't want to see**.
- You can filter your search by **scaling or non-scaling objects** using `scale:1` or `scale:0`, respectively.
- Use `/tag objectterms` to see some useful terms and actor names.
- Sometimes, you will need to put your search term in quotes to **prevent other objects from being included**: `"Captain Construct II" Sky`
- If you need to see the **shown in-game coordinates for an object on the Object Map**, go to the Settings menu and select "Use In-Game Coordinates".
'''
INFO_USEFULOBJECTTERMSTITLE = '''Here are some terms/actor names that might be useful when using the Object Map:'''
INFO_USEFULOBJECTTERMS = '''
- `WallCrack`, `RockBroken` - Light Gray Cracked Rocks/Cracked Walls
- `AutoGenerateDestructibleActorHardnessLv1` - Red Hard Sediment
- `AutoGenerateDestructibleActorHardnessLv2` - Blue Hard Sediment
- `AutoGenerateDestructibleActorHardnessLv3` - Dark Gray Hard Sediment
- `AutoGenerateDestructibleActorLuminous` - Luminous Ore Walls
- `AutoGenerateDestructibleActorZonanium` - Zonaite Ore Walls
- `TreeSkyLiana` - Liana/Vine Walls
- `EquipmentUser_Attachment_Arrow` - Actors that use equipment with attached items, such as elemental arrows. You can filter this by specific items as well.
- `BokoblinBasket` - Bokoblins with baskets on their backs.
- `MinusFieldGhost` - Spectral Figures
- `TreeStumpHolySpot_B` - Groups of three Spectral Figures, also doubles as the locations of the Calamity Monuments on the Surface
- `SkyObj_ZonauRobot_Background_A_03` - Decayed Construct (Sky)
- `MinusObj_ZonauRobot_Background_B_03` - Decayed Construct (Depths)
- ||`DungeonBoss Underground`|| - ||Temple Boss Rematches||
- `0xa28db083b72c4f7f OR 0xf29e2d98917a4072 OR 0x01462a767956fbee OR 0xcf49878e3a8c301f` - The areas where a Blood Moon is forced if you haven't seen one before and attempt to visit a Regional Phenomena town.
- `DgnObj_Zonau_SliderBox_A_02` - Elevator Rail
- `BarrelBomb NOT BarrelBomb2 NOT BarrelBomb3`, `BarrelBomb2`, and `BarrelBomb3` - Levels 1, 2, and 3 Bomb Barrels
- `TimerBarrelBomb` - Cube-shaped Time Bombs found in enemy camps
- `Merchants` - Traveling NPC merchants
- `MiasmaSwarm`, `Phantom Ganon` - Gloom Spawn/Phantom Ganon
  Some Gloom Spawn are controlled by certain flags:
  - `MiasmaSwarm_RandomSet`, `MiasmaSwarm_RandomSet3` - Randomized on load; these can be save-scummed to get them to spawn
  You can also search for Phantom Ganons with specific Gloom Weapons
  - `NOT EquipWeaponType` - Gloom Sword
  - `EquipWeaponType 2` - Gloom Club
  - `EquipWeaponType 3` - Gloom Spear
'''

POINT_DATAPHIL = '''
Here's a link to Phil's Data Sheet for TotK: 
https://docs.google.com/spreadsheets/d/1fBvQ17WHP3ASgtO8ode_rf1g4DfEHErMrHwwLppNTJM/edit?usp=sharing
'''
POINT_DATAECHO = '''
Here's a link to Echocolat's Data Sheet for TotK: 
https://docs.google.com/spreadsheets/d/18pNtDx3z-8CwGJRmlW574xbQ6VphQOkvpZhClpOEVDA/edit?usp=sharing
'''
POINT_INTEROBJECTSHEET = '''
Here's a link to Phil's Interactable Objects Sheet for TotK:
https://docs.google.com/spreadsheets/d/1eHHFwGDsI3sHTOLaawlxKgxbiLG8ceHUHpbpC2Bj57k/edit?usp=sharing
'''

POINT_WORLDEXP = '''
Here's a link to an explanantion on World Level in TotK: 
https://www.reddit.com/r/tearsofthekingdom/comments/1dcxgcv/explaining_level_scaling_once_and_for_all_totk/
'''
POINT_TEMPLESCALING = '''
Here's a link to an explanation on Temple Boss Scaling in TotK: 
https://www.reddit.com/r/tearsofthekingdom/comments/14rr5sd/how_temple_bosses_scale_a_full_breakdown/
'''
POINT_SAGELVL = '''
Here's a link to an explanation on Sage Attack Power: 
https://www.reddit.com/r/tearsofthekingdom/comments/14ct8kt/sage_attack_power_a_full_breakdown/
'''
POINT_BLOODMOONDOC = '''
Here's a link to bjm's document on Blood Moons and other respawn mechanics:
https://docs.google.com/document/d/1w59IZh1z7Empep1kCjqXLHuTPqu5DHnwKdYEzU3TC60/edit?usp=sharing
'''

POINT_COOKING = '''
Here's a link to a guide about cooking: 
https://zeldawiki.wiki/wiki/Cooking
'''
POINT_COOKCALC = '''
Here's a link to Ghastly64's cooking calculator for TotK:
https://www.totkcookbook.com/
'''
POINT_BREADRECIPE = '''
Here's a link to a guide on making Bread in TotK:
https://youtu.be/XYUhLxlqOH0
'''

POINT_LEVELCARDS = '''
Here are some links to galleries of level cards for you to use with Arcane's `/card image set` command:
NOTE: It is recommended to use 70 percent opacity `/card opacity <number>`.
TotK Level Cards:
<https://imgur.com/gallery/totk-level-cards-T5bxKuT>
HW:AoC Level Cards:
<https://imgur.com/gallery/hwaoc-level-cards-TulXkr5>
Lucie's HW:AoC Level Cards:
<https://imgur.com/a/lucies-age-of-calamity-cards-wTUmiAp>
Dash's Classic Zelda Level Cards:
<https://imgur.com/a/classic-zelda-level-cards-ss-oot-tp-gLiEcRY>
'''
INFO_DIRECTIMGLINK = '''
In order to use Arcane's `/card image set` command, you will need to provide a direct link to the image you want to use. You can use Imgur to host your own images, but keep in mind that Arcane will stretch the image to fit 800x200 pixels.

Direct links for images will usually end in `.jpg` or `.png`. Ex: <https://i.imgur.com/jM8Qume.jpg>

In order to get the direct link for an image on pc, right click on the specific image you want to use and select, "Copy image address."
If you're on mobile, try viewing the image in fullscreen, look for a "Share" option, and then a "Copy link" option.
'''
POINT_BEEDLETRADES = '''
Here's a link to a list of all Beedle Trades: 
https://docs.google.com/spreadsheets/d/1QMCSV19HFazu-dQuz0vN5lBDlMwXDYciUEYgG3h57ZQ/edit?usp=sharing
'''
POINT_AMIIBODROPTABLES = '''
Here's a link to the Amiibo Drop Tables Spreadsheet for TotK:
https://docs.google.com/spreadsheets/d/1BF5WDN09z0evruAQH-3qIMjnPe6dfKyomfLT_0aIZrg/edit?usp=sharing
'''
POINT_GLITCHSHEET = '''
Here's a link to the Glitch Spreadsheet:
https://docs.google.com/spreadsheets/d/1xNB1gOLZRSF9yp1mHUsS9ymogRJa1Wz8rTliTXezeRM/edit?usp=sharing
'''
POINT_DONDON = '''
Here are some links to information on what gems Dondons can give:
Video Guide: <https://youtu.be/BGxltmsZaAI>
Drop Table Sheet: <https://docs.google.com/spreadsheets/d/1bj_1KHBFgr-1tyc1HJIHTXmLgws3mWnTTgVyg8LSZVY/edit?usp=sharing>
'''
POINT_HORSECOLORS = '''
Here's a link to a document on Wild Horse Coloration in TotK by Artoirel:
https://docs.google.com/document/d/1c2ZyGfECQw3OLTt2qHuzM6mrWfSNkbhk6xJK1fSP4aU/edit?usp=sharing
'''
POINT_ENERGYCELLSTATS = '''
Here are some link's to Paradox Gaming's videos on Zonai Device power usage in TotK:
Energy Cell usage:
<https://youtu.be/TpFoMHQ1nyw>
Battery usage:
<https://youtu.be/ZVk7u7L2dEA>
'''
POINT_DISPENSERPRICES = '''
Here is a link to a sheet with the Device Dispenser prices:
https://docs.google.com/spreadsheets/d/1mYfBsunmPgVa3ANXgeAhCtk1csOKlKFoTipVypf_nYE/edit?usp=sharing
'''
POINT_COMBATGUIDE = '''
Here is a link to RinHara5aki's Advanced Combat Glossary for TotK:
https://docs.google.com/document/d/1z0qViEN9cl7dTpTb2LP2vlUVp9qiFMu2QJS8KDFx-cM/edit?usp=sharing
'''
POINT_MISSABLEOBJECTS = '''
Here is a link to the Missable Objects List for TotK:
https://docs.google.com/document/d/1Sfeh1OmGCQ200bGbWtuL7yhtj6Hqe_83JC87-ntQ4qU/edit?usp=sharing
'''
POINT_GAMBLINGGAME = '''
Here is a link to a spreadsheet with the odds for the different rewards from the Lucky Treasure Shop in Lurelin Village:
https://docs.google.com/spreadsheets/d/1OvdU1fdPh3gVOX4uVtT4WNNDob3HgdsX5uOtzQ5v8RY/edit?usp=sharing
'''

POINT_HOVERBIKE = '''
Here's a link to a guide on building a Hoverbike: 
https://youtu.be/oq4LmYEFlHM
'''
POINT_HOVERBIKEv4 = '''
Here's a link to a guide on building the Hoverbike 4.0:
https://youtu.be/AXWAEBlvIXs
'''
POINT_GOLDENWING = '''
Here's are some links guides on obtaining the Golden Wing/Infinity Wing in TotK:
Versions 1.0.0 - 1.1.2: <https://youtu.be/KTxbMQeIhno>
Versions 1.2.0 - 1.2.1: <https://youtu.be/k7R94dGai0E>
'''
POINT_RAILPARTTITLE = '''Here are some links to videos showing how to detach an Elevator Rail:'''
POINT_RAILPART = '''
- [Stabilizer Method](<https://www.reddit.com/r/HyruleEngineering/comments/14qj7qw/simple_and_low_part_cost_way_to_detach_the/>)
  - Used in the Construct Factory's Right Leg Depot, on the elevators that move straight up and down.
- [Rocket Method](<https://youtu.be/d5LeqKkJdYQ>)
  - Used on the elevators found at the bottom of Great Plateau West Chasm and Ancient Underground Fortress

'''
POINT_BETTERPHOTOS = '''
Here's are some links to guides on taking higher quality photos in TotK:
- [Horse Method](<https://youtu.be/Bi7BC4wSjI8>) - Longer setup, early-mid game
- [Mineru Method](<https://youtu.be/mHC8BJpDxGE?t=277>) - Uses part of the setup for Vendor Scamming (__**watch until 6:50**__). Quick to set up, but requires the ||Vow of Mineru||.
'''
POINT_PARACOPTER = '''
Here's a link to a guide on building and using a Paracopter:
https://youtu.be/HjS60KRpiq4
'''
POINT_FUSEIDEAS = '''
Here's a link to video demonstrating some of the useful Fuse options in TotK:
https://youtu.be/3f7PiBOgAuk
'''

POINT_AUTOBUILDSHARING = '''
Here is a link to the community Zelda Wiki page for sharing Autobuild designs:
<https://zeldawiki.wiki/wiki/Community:Autobuild_Sharing>
'''
POINT_VOICEMEMORYTITLE = '''Here are some links to recordings and transcriptions of the Voice Memories available in Zelda Notes:'''
POINT_VOICEMEMORY = '''
**Zelda Universe's Videos**
BotW:
- [Zelda](<https://youtube.com/watch?v=uydyVY2aMXo>)
TotK:
- [Zelda](<https://youtube.com/watch?v=j5LSmGLq6fE>)
- [Rauru](<https://youtube.com/watch?v=VMz_v0M2ufQ>)
- [Master Kohga](<https://youtube.com/watch?v=AGjUdviyJpw>)

**Zelda Wiki Pages**
- [Breath of the Wild](<https://zeldawiki.wiki/wiki/Voice_Memories_in_Breath_of_the_Wild>)
- [Tears of the Kingdom](<https://zeldawiki.wiki/wiki/Voice_Memories_in_Tears_of_the_Kingdom>)
'''
# endregion

# region Meta Info
INFO_DUPE112TITLE = '''Here are some duplication glitches for 1.1.2:'''
INFO_DUPE112 = '''
**Equipment Dupes**
- [Shock Duping](<https://youtu.be/TbzG9aXo8JA>)
- [Save Load Dupe](<https://youtu.be/lGgVL4QdRFA>) (For throwable equipment)
- [Rock Octorok Recall](<https://youtu.be/0cR_fbx-P_Y>) (For non-Legendary equipment)
- [Weapon Stat Transfer](<https://youtu.be/9jJbAJdP3d8>)
**Rupee Farming**
- [Autobuild Duplication](<https://youtu.be/YLxu53iXB_w>)
- Vendor Scamming
  - [Horse Method](<https://youtu.be/mHC8BJpDxGE?t=76>) - Longer setup, early-mid game
  - [Mineru Method](<https://youtu.be/mHC8BJpDxGE?t=277>) - Quick to set up, but requires the ||Vow of Mineru||.
**Materials and Other Dupes**
- [Tobio's Hollow Chasm Duplication](<https://youtu.be/E8nab6JNBts>) (For fusable materials)
- [Midair Inventory Shift Dupe (MISD)](https://youtu.be/th585pt33sA)
- [MISD w/ Dispenser Storage](https://youtu.be/2YJkvpmeNzo)
- [Midair Throw Duplication (MTD)](<https://youtu.be/BZID7B_99QY?t=827>) (For throwable materials)
- [MTD w/ Dispenser Storage](<https://youtu.be/BZID7B_99QY?t=977>)
- [Bundle Item Duplication (BID)](<https://youtu.be/LAmtplodqWQ>) (For critters or mass duping)
  - Read the description if your on version 1.1.2 or under.
- [Zonai Inventory Shift Duplication (ZISD)](<https://youtu.be/BZID7B_99QY?t=685>) (For Zonai Devices)
- [Bomb/Elemental Fruit "Dupe"](<https://youtu.be/BZID7B_99QY?t=21>)
'''
INFO_DUPE120TITLE = '''Here are some duplication glitches for 1.2.0:'''
INFO_DUPE120 = '''
**Equipment Dupes**
- [Cull Transmutation and Overload Duping](<https://youtu.be/gAwqDumlH4g>)
- [Like-Like Fuse Entanglement](<https://youtu.be/BZID7B_99QY?t=1207>)
  - [Slugging](<https://youtu.be/BZID7B_99QY?t=1553>)
  - [Weapon Stat Transfer (WST) w/ Like-Like Fuse Entanglement](<https://youtu.be/Jw2HWQTKS8w>)
- [Stal-Arm Smuggling](<https://youtu.be/OL64sy4Uucc>)
  - Dupes weapons, including their Fused item. Note that when any equipment is fused to other equipment it will lose its modifier, if applicable.
- Like-Like Stick Culling:
  - Allows for all equipment duplication, Fuse Entanglement/FE WST, and more.
  - [BlizeYT's guide](<https://youtu.be/iRkNT3NEVuQ>)
  - [Suishi's guide](<https://youtu.be/5SJvlf0iTcE>)
**Rupee Farming**
- Vendor Scamming
  - [Horse Method](<https://youtu.be/mHC8BJpDxGE?t=76>) - Longer setup, early-mid game
  - [Mineru Method](<https://youtu.be/mHC8BJpDxGE?t=277>) - Quick to set up, but requires the ||Vow of Mineru||.
**Materials and Other Dupes**
- [Minus Duping w/ Dispenser Storage](<https://youtu.be/StAzqZ_YAEI>) (For throwable materials)
- [Midair Throw Duplication (MTD)](<https://youtu.be/BZID7B_99QY?t=827>) (For throwable materials)
  - [MTD w/ Dispenser Storage](<https://youtu.be/BZID7B_99QY?t=977>)
- [Bundle Item Duplication (BID)](<https://youtu.be/LAmtplodqWQ>) (For critters or mass duping)
- [Zonai Inventory Shift Duplication (ZISD)](<https://youtu.be/BZID7B_99QY?t=685>) (For Zonai Devices)
- [Bomb/Elemental Fruit "Dupe"](<https://youtu.be/BZID7B_99QY?t=21>)
'''
INFO_DUPE121TITLE = '''Here are some duplication glitches for 1.2.1-1.4.0:'''
INFO_DUPE121 = '''
**Equipment Dupes**
- [Cull Transmutation and Overload Duping](<https://youtu.be/gAwqDumlH4g>)
- [Pelison Duping and Easy WST](<https://youtu.be/SfWqYmKAT5o>)
  - Dupes any equipment, as long as it can be Fused to something else. Note that when any equipment is fused to other equipment it will lose its modifier, if applicable.
  - Allows for quick Weapon Stat Transfer (WST) while duping.
- [Stal-Arm Smuggling](<https://youtu.be/OL64sy4Uucc>)
  - Dupes weapons, including their Fused item. Note that when any equipment is fused to other equipment it will lose its modifier, if applicable.
- Like-Like Stick Culling:
  - Allows for all equipment duplication, Fuse Entanglement/FE WST, and more.
  - [BlizeYT's guide](<https://youtu.be/iRkNT3NEVuQ>)
  - [Suishi's guide](<https://youtu.be/5SJvlf0iTcE>)
**Rupee Farming**
- [Vendor Scamming](<https://youtu.be/mHC8BJpDxGE?t=410>)
  - NOTE: This glitch is limited, so the Hold Storage will need to be re-performed every 5 items on 1.2.1.
**Materials and Other Dupes**
- [Minus Duping w/ Dispenser Storage](<https://youtu.be/StAzqZ_YAEI>) (For throwable materials)
- [Midair Throw Duplication (MTD)](<https://youtu.be/bV1KxESU9v8?t=283>)
  - [MTD w/ Dispenser Storage](<https://youtu.be/BZID7B_99QY?t=977>) - Guide from 1.2.0, but can still be used with the 1.2.1 MTD method
- [Bundle Item Duplication (BID)](<https://youtu.be/LAmtplodqWQ>) (For critters or mass duping)
- [Zonai Inventory Shift Duplication (ZISD)](<https://youtu.be/LCc1525GlHo?t=561>)
- [Bomb/Elemental Fruit "Dupe"](<https://youtu.be/BZID7B_99QY?t=21>)

**Changes on 1.4.1 and Switch 2**
- [Changes on 1.4.1 and Switch 2](<https://youtu.be/HoGgmzej2-o>)
'''
POINT_121FEZUGGLE = '''
Here's are some links to SuishiYT's guides on Fuse Entanglement and Zuggling in 1.2.0-1.4.1:
- Intro to Entanglement & Zuggling - <https://youtu.be/kJGVuI0fizk>
- Intermediate Entanglement & Zuggling - <https://youtu.be/on9x_uisocw>
'''
POINT_121MNF = '''
Here are some guides on obtaining and upgrading an unbreakable Master Sword in versions 1.2.0-1.2.1 of TotK:
- [Suishi's guide](<https://youtu.be/bueZYVnq-QQ>)
- [El Duende's guide](<https://youtu.be/GlVJarlWaTo>)
'''
INFO_DOWNPATCH = '''
You cannot downpatch your game without losing your save data. You can only downpatch to 1.0, unless you have access to another Switch with a version in between 1.0 and current patch. 

To downpatch to 1.0, you will need to have a physical copy of the game, and to factory reset your Switch. After doing so, make sure you keep your Switch from updating the software, either by disconnecting it from the internet or by turning off auto-updates and rejecting the prompts to update. 

If you have access to a Switch with a version between 1.0 and current patch, you can match your update with it after factory resetting your Switch.
'''
INFO_PREVENTUPDATES = '''
**When your Auto-Update Software setting is set to "On" and your Switch is connected to the internet,** it will attempt to automatically download any available update data for any installed software. When your Switch has downloaded update data for a software, it will install that update data when that software is not running.

**In order to prevent your Switch from downloading update data for a software,** you can either disconnect your Switch from the internet, or you can go your Settings -> System -> Auto-Update Software and set it to "Off." Keep in mind that if there is update data available for a software and your Switch is connected to the internet, then you will be prompted with a pop-up every time you start that software. In order to prevent the software from being updated, make sure to select "Start Software" and not "Download" or your Switch will *download the update data and install it.*

**If you attempt to resume a suspended software from the home screen and receive a pop-up telling you that you need to close the software to *install* an update,** then that means your Switch has downloaded the update data for the software, and it will install it once the software is closed. You can safely resume the software without it updating, but once you fully close it, or restart your Switch, the software will be updated.

**If you launch a software and you get a pop-up saying that you need to restart your Switch to install a *system* update,** then you can do so without fear of your software being updated, if the update data is not downloaded and waiting to be installed.
'''
INFO_CHECKGAMEVERSION = '''You can check your game version by pressing `+` on your controller from the Switch Home Screen.'''
POINT_TRANSFERALBUMTITLE = '''Here are some guides on how to transfer screenshots and clips from your Switch:'''
POINT_TRANSFERALBUM = '''
- [Transfer to your smartphone via QR code](<https://en-americas-support.nintendo.com/app/answers/detail/a_id/53138/kw/how-to-transfer-Screenshots-and-Video-Captures-to-a-Smart-Device-Wirelessly>)
- [Transfer to your computer via USB](<https://en-americas-support.nintendo.com/app/answers/detail/a_id/53664/~/how-to-transfer-screenshots-and-video-captures-to-a-computer-via-a-usb-cable>)
'''

POINT_WHEREDLC = '''
Here's a link to a video explaining the situation regarding DLC for TotK:
https://youtu.be/DY-qfykgeuQ
'''
POINT_NFCTAGS = '''
Here's a link to a guide on making NFC tags to use as amiibo:
https://youtu.be/tBFSa4Tuzug
'''
POINT_TIMESTAMP = '''
Here's a link to a website where you can create timestamps that automatically convert to other people's timezone:
<https://sesh.fyi/timestamp/>
'''
# endregion

# region Image Messages
IMAGE_ARMORTOTAL = '''Here are all of the totals for materials required to fully upgrade every armor in TotK:'''
IMAGE_ORETOTAL = '''Here are the totals for Ores/Misc materials required to upgrade every armor in TotK:'''
IMAGE_DRAGONTOTAL = '''Here are the totals for Dragon Parts required to upgrade every armor in TotK:'''
IMAGE_HORNTOTAL = '''Here are the totals for Monster Horns required to upgrade every armor in TotK:'''
IMAGE_GUTTAILTOTAL = '''Here are the totals for Monster Guts/Tails required to upgrade every armor in TotK:'''
IMAGE_MEATANDADDITIVETOTAL = '''Here are the totals for Meats and Additives required to upgrade every armor in TotK:'''
IMAGE_FRUITANDVEGGIETOTAL = '''Here are the totals for Fruits and Veggies required to upgrade every armor in TotK:'''
IMAGE_OTHERPARTTOTAL = '''Here are the totals for Other Monster Parts required to upgrade every armor in TotK:'''
IMAGE_CRITTERTOTAL = '''Here are the totals for Critters required to upgrade every armor in TotK:'''
IMAGE_ZONAITOTAL = '''Here are the totals for Zonai materials required to upgrade every armor in TotK:'''

IMAGE_ASCENDMAP = '''Here is a map of all the Ascend Ruins within the Depths:'''
IMAGE_CHERRYMAP = '''Here is a map of all the Cherry Blossom Trees in TotK:'''
IMAGE_CHERRYAREAMAP = '''Here is a map of all the Cherry Blossom Tree Areas in TotK:'''
IMAGE_KOLTINSTALLMAP = '''Here's a map of the locations where you can find Koltin's Stall in TotK:'''
IMAGE_INVENTORYUPGRADES = '''Here are all of the Inventory upgrade costs for TotK:'''
IMAGE_SHRINECOUNTS = '''Here are the totals of each type of Shrine of Light in TotK:'''
IMAGE_HORSEUPGRADE = '''Here are the meals needed to upgrade a horse to maximum in TotK:'''

IMAGE_MISKOBANNER = '''The Great Bandit Misko left distinct banners along the path to their treasure. The banners don't point directly to the treasure, but you can follow from one banner to the next to find the hidden spoils.'''

IMAGE_DMGFORMULA = '''
Here is the damage formula for Link's attacks in TotK; for more information, please check out the Damage Calculations Doc:
<https://docs.google.com/document/d/1K5hLcxfnvSnY-nsIP-n8Ew7rm9EkqHtnn6iJqOnxlng/edit?usp=sharing>
'''
# endregion

# region Dispenser Messages
DISP_BASE = '''Here are all of the Device Dispensers that can dispense '''
DISP_BASE2 = ''' capsules:'''

DISP_FAN = '''
Great Sky Island (South) - 40%
Thunderhead Isles - 35%
Great Sky Island (East) - 30%
Dragonhead Island - 25%
Courage Island - 20%
Kakariko Village - 20%
Lanayru Sky Archipelago - 20%
South Eldin Sky Archipelago - 20%
East Hebra Sky Archipelago - 15%
Hudson Construction Site - 15%
Wellspring Island - 15%
'''
DISP_WING = '''
Great Sky Island (East) - 35%
Lanayru Sky Archipelago - 30%
Tabantha Sky Archipelago - 30%
Dragonhead Island - 25%
East Hebra Sky Archipelago - 25%
Lightcast Island - 20%
North Necluda Sky Archipelago - 20%
South Lanayru Sky Archipelago - 20%
Left-Leg Depot - 15%
Wellspring Island - 15%
'''
DISP_CART = '''
Lanayru Sky Archipelago - 30%
Dragonhead Island - 25%
West Necluda Sky Archipelago - 20%
East Hebra Sky Archipelago - 15%
Sokkala Sky Archipelago - 15%
'''
DISP_BALLOON = '''
Courage Island - 30%
West Necluda Sky Archipelago - 20%
Hudson Construction Site - 15%
Kakariko Village - 25%
Lightcast Island - 15%
'''
DISP_ROCKET = '''
West Hebra Sky Archipelago - 30%
South Hyrule Sky Archipelago - 25%
Hudson Construction Site - 15%
Left-Leg Depot - 15%
'''
DISP_TIMEBOMB = '''
Courage Island - 25%
Sky Mine - 25%
West Hebra Sky Archipelago - 25%
North Necluda Sky Archipelago - 20%
South Hyrule Sky Archipelago - 20%
Zonaite Forge Island - 20%
'''
DISP_PORTABLEPOT = '''
Great Sky Island (South) - 40%
Courage Island - 25%
Great Sky Island (East) - 20%
Death Mountain Depths - 15%
Gerudo Canyon Pass - 15%
Thunderhead Isles - 15%
West Hebra Sky Archipelago - 15%
'''
DISP_FLAMEEMITTER = '''
West Hebra Sky Archipelago - 30%
Bravery Island - 20%
Great Sky Island (South) - 20%
Zonaite Forge Island - 20%
Great Sky Island (East) - 15%
'''
DISP_FROSTEMITTER = '''
South Lanayru Sky Archipelago - 30%
Starview Island - 20%
Tabantha Sky Archipelago - 20%
Zonaite Forge Island - 20%
'''
DISP_SHOCKEMITTER = '''
Thunderhead Isles - 35%
North Hyrule Sky Archipelago - 20%
Starview Island - 20%
'''
DISP_BEAMEMITTER = '''
Lanayru Sky Archipelago - 20%
Valor Island - 20%
Zonaite Forge Island - 20%
East Gerudo Sky Archipelago - 15%
'''
DISP_HYDRANT = '''
South Eldin Sky Archipelago - 40%
Valor Island - 25%
West Necluda Sky Archipelago - 20%
Sky Mine - 15%
'''
DISP_STEERINGSTICK = '''
Death Mountain Depths - 40%
East Gerudo Sky Archipelago - 30%
North Hyrule Sky Archipelago - 30%
South Necluda Sky Archipelago - 30%
Dragonhead Island - 25%
Valor Island - 25%
Hudson Construction Site - 20%
Left-Leg Depot - 20%
'''
DISP_BIGWHEEL = '''
Death Mountain Depths - 30%
Gerudo Canyon Pass - 30%
Kakariko Village - 20%
Left-Leg Depot - 20%
South Eldin Sky Archipelago - 20%
Hudson Construction Site - 15%
'''
DISP_SMALLWHEEL = '''
South Hyrule Sky Archipelago - 30%
South Necluda Sky Archipelago - 30%
Tabantha Sky Archipelago - 25%
Hudson Construction Site - 20%
Left-Leg Depot - 15%
'''
DISP_SLED = '''
East Hebra Sky Archipelago - 30%
Starview Island - 25%
East Gerudo Sky Archipelago - 20%
'''
DISP_BATTERY = '''
Bravery Island - 30%
South Lanayru Sky Archpelago - 30%
South Eldin Sky Archipelago - 20%
Death Mountain Depths - 15%
Gerudo Canyon Pass - 15%
Thunderhead Isles - 15%
Wellspring Island - 15%
'''
DISP_BIGBATTERY = '''
There are no Device Dispensers that provide Big Batteries. They can only be obtained from chests and Crystal Refineries (after you have fully upgraded your Energy Cell).
'''
DISP_SPRING = '''
North Necluda Sky Archipelago - 40%
Valor Island - 30%
Gerudo Canyon Pass - 15%
Lightcast Island - 15%
'''
DISP_CANNON = '''
North Necluda Sky Archipelago - 20%
South Necluda Sky Archipelago - 20%
Sokkala Sky Archipelago - 15%
'''
DISP_STABILIZER = '''
Kakariko Village - 35%
Wellspring Island - 20%
West Necluda Sky Archipelago - 20%
Starview Island - 15%
'''
DISP_HOVERSTONE = '''
Sky Mine - 35%
Wellspring Island - 35%
Lightcast Island - 15%
'''
DISP_LIGHT = '''
North Hyrule Sky Arhipelago - 30%
Bravery Island - 25%
South Hyrule Sky Archipelago - 25%
South Necluda Sky Archipelago - 20%
East Hebra Sky Archipelago - 15%
'''
DISP_STAKE = '''
Gerudo Canyon Pass - 25%
Sokkala Sky Archipelago - 20%
Starview Island - 20%
East Gerudo Sky Archipelago - 15%
'''
DISP_MIRROR = '''
Lightcast Island - 35%
Tabantha Sky Archipelago - 25%
East Gerudo Sky Archipelago - 20%
South Lanayru Sky Archipelago - 20%
'''
DISP_HOMINGCART = '''
Sokkala Sky Archipelago - 30%
Sky Mine - 25%
North Hyrule Sky Archipelago - 20%
Zonaite Forge Island - 20%
'''
DISP_CONSTRUCTHEAD = '''
Bravery Island - 25%
Sokkala Sky Archipelago - 20%
West Necluda Sky Archipelago - 20%
Left-Leg Depot - 15%
'''
# endregion

# region Command Messages
COMMAND_OBJMAPTERMS = '''Here is your Object Map link for the search term, '''
COMMAND_OBJMAPBASELINK = '''https://objmap-totk.zeldamods.org/#/map/z2,0,0,'''

CONVERT_COORD1 = '''The Object Map coordinates: '''
CONVERT_COORD2 = ''' are equivalent to the shown in-game coordinates: '''

COMMAND_FINDPRISTINE1 = '''Here are the Spectral Figures in the Depths that can spawn Pristine '''
COMMAND_FINDPRISTINE2 = ''' weapons:'''

COMMAND_HELLO1 = '''Hi!'''
COMMAND_HELLO2 = '''Hello!'''
COMMAND_HELLO3 = '''Greetings!'''

COMMAND_THANKS1 = '''You're welcome!'''
COMMAND_THANKS2 = '''You are quite welcome!'''
COMMAND_THANKS3 = '''Happy to help!'''
# endregion

# Unimplemented Messages --- UPDATE HELP ---