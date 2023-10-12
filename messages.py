# messages.py

# region System
BOT_ONLINESIMPLE = '''RauruBot is now online'''
BOT_ONLINEPERSON = ''''''
BOT_OFFLINESIMPLE = '''RauruBot is shutting down'''
BOT_OFFLINEPERSON = '''Now it is up to you, Link...........'''

ERROR_UNKNOWNCMD = '''My apologies, I'm afraid I don't recognize that command. Use `?tag help` to see available commands.'''
ERROR_BLACKLIST = '''My apologies, but I'm afraid I don't understand that blacklist command. Use `@Rauru#6248 blacklisthelp` to see how to use the blacklist command.'''
ERROR_NODM = '''My apologies, but commands are only available inside servers.'''
ERROR_BADROLE = '''My apologies, but you lack the appropriate role for this command.'''
ERROR_BADCOORDS = '''My apologies, but I cannot convert those coordinates.'''
# endregion

HELP_COMMANDS = '''
Here are some of my commands:

`?tag [argument]`
    **Command Help**
    `help [page number], helphere [page number]`
    -*Note: Page number defaults to the 1st page if not specified*
    
    **Server Stuff**
    `botinfo, userauru, imgperms, spoiler, totkexpert, piracy/tos`
    **Story Stuff**
    `ringruins, postgame, permaquests, trueend, elitepics, josha`
    **Farming Stuff**
    `bloodmoon, forcebloodmoon, materialrespawn, shoprestock, chargefarm, starfragment, dragon, earlyrupees`
    **Durability**
    `octorok, repairlegendary, legendarylist, fusedurability, pristine`
    **Mechanics and Hints**
    `mastersword, cherry/cherrytrees, bargainer/bargainerstatues, amiiborespawnalt/duskbow/whitesword`
    `botwdata, coordsystem, depthsmirror, deviceshop, ritofabric, hornedstatue, mat253/sunpumpkin`
    `elementdmg, missablelocations, midairwing, truedmg, botwarmor/missingarmor, moatchasm`
    `control5/jumpslash, breakitdown/pelison, gleeokstrat, dugby`
    **Effects and Builds**
    `defense, bestarmor, moisture, weatherattack, gloomattackresist, slipresist, attackstacking, boneprof`
    `backscratcher, lynelfragile, dmgcalc`
    **Reference Info**
    `tracker, maps, objectmap, echodatasheet, phildatasheet, worldexp, templescaling, sagelevel, objectterms`
    `beedletrades, cooking, hoverbike, mapcompletion, recipecalc, armorcalc, amiibodrops, glitchsheet`
    `hoverbike4.0, cookcalc, constructfarm, shrinefinder, transferpics, levelcards, objectsheet`
    `dondon, arrowfarm`
    **Meta Info**
    `dupe1.1.2, dupe1.2.0, dupe1.2.1, railpart/elevatorrail, unreleasedamiibo, downpatch, versioncheck, betterpics, whereDLC`
    **Reference Images**
    `horseupgrades, ascendmap, cherrymap, dmgformula, invupgrades, shrinecounts, miskobanner`
    `armortotals, fruitandveggietotals, meattotals, horntotals, gutsandtailtotals, otherparttotals, oretotals`
    `zonaitotals, dragontotals`
    
`Page 1 of 2`
'''
HELP_COMMANDS2 = '''
Here are some of my commands:

`?createobjlink [search terms]`, `?find [search terms]`
    -You can use this command to create an Object Map link with search terms integrated into it. Just put the exact text (including spaces and punctuation) after the command.

`?coordconvert [Object Map coordinates]`
    -You can use this command to convert the coordinate of an object from the Object Map into its shown in-game coordinates.
    -Just copy the coordinates of the object's position directly from the Object Map, then paste it after `?coordconvert `.
    
    For Example:
    `?coordconvert -579.73, 129.61, -524.79` will give you the in-game coords: `-580, -525, 25`

`?findpristine [weapon name]`
    -You can use this command to create an Object Map link that will show which Depths Ghosts can spawn a weapon.

`?finddispenser [device name]`, `?dispenser [device name]`
    -You can use this command to see which Device Dispensers are most likely to dispense a specific Zonai Device.

`Page 2 of 2`
'''
HELP_NOTIFY = '''Sending you a list of my commands'''
HELP_NOTIFYERROR1 = '''My apologies'''
HELP_NOTIFYERROR2 = ''', but I can't send you a list of my commands. Please try using `?tag helphere` in a bot channel.'''

HELP_BLACKLIST = '''
Here's how to use my blacklist command: 
***Please keep in mind that all of my responses to these commands will be sent to the channel in which you use the command!***

`@Rauru#6248 blacklist show`
    -Shows the currently blacklisted users and the reasons they were blacklisted

`@Rauru#6248 blacklist add <userid> <reason(optional)>`
    -Adds a user to the blacklist. Add information after the userid to save the reason they were blacklisted, or other info.

`@Rauru#6248 blacklist remove <userid>`
    -Remove a user from the blacklist

`@Rauru#6248 blacklist update <userid> <reason(optional)>`
    -Update a user's blacklist reason/info
'''

# region Server Stuff
BOT_INFO = '''Greetings! My name is Rauru. I am here to help guide you on your journey through Hyrule by providing information and links.'''
INFO_USERAURU = '''
I have a lot of useful information and links. Please feel free to use `?tag help` and use as many of my commands as you like in <#811092574672388106> or <#1145875241080475658>.
'''
HELP_IMGPERM = '''
In order to be able to post images or embed other stuff on this server, you'll need to reach **Traveler** rank (Level 3) or above. 
Use `/level` in #bot-fun to view your current level information.
'''
HELP_SPOILERTAG = '''
Please spoiler tag any main story spoilers outside of spoiler-friendly channels. You can spoiler tag text by putting "||" on both sides of the spoiler, \|\|like this\|\|.
You can spoiler tag images **when attaching** them by clicking the small eye icon above them if you're on desktop, or by tapping and holding on the image if you are on mobile.
'''
HELP_EXPERTROLE = '''The TOTK Expert role is considered a staff role. The responsibility of a TOTK Expert is to help assist and guide members with their gameplay. Although it does not come with any moderation tools, TOTK Expert are given Manage Messages permission so they can pin any important information in any channel.'''
HELP_RULE913 = '''Please refer to rules 9 and 13 in <#1022236312209739846>, which state that discussion of hacking, piracy, emulation, or anything else against Nintendo's Terms of Service is not allowed on this server.'''
# endregion

# region Story Stuff
INFO_RINGRUINQUEST = '''The main quest ||"Secret of the Ring Ruins"|| can be begun by speaking to Tauro and Paya in Kakariko Village after you\'ve completed ||"Crisis at Hyrule Castle"||.'''
INFO_POSTGAME = '''
Legend of Zelda games do not generally have a post-game. Instead, TotK reverts you to your last save before the finale and adds a little star to it. This will:
 -Add a percentage counter for your map completion to your Purah Pad
 -Add totals counters for your quests to your Purah Pad
 -Unlock the option to purchase Elite Enemy Compendium pictures from Robbie
 -Carry over any pictures and Compendium entries you got during the finale
 -Add ||Zelda's Sage symbol to the loading screen||
'''
INFO_PERMQUESTS = '''You cannot permanently complete the quests ||"Destroy Ganondorf"|| or ||"Find Princess Zelda"||, as they are completed during the finale of the game.'''
INFO_TRUEEND = '''If you have collected every memory, then ||a new cutscene featuring all the Sages will play after the credits.||'''
INFO_ELITEPIC = '''After beating the game, you get the option to purchase Elite Enemy Pictures for your Compendium from Robbie.'''
INFO_JOSHA = '''Josha is the head of Depths Research and can be found in her workshop in Lookout Landing. She provides a number of quests designed to lead you to important locations in the Depths, so anytime you have a question about the Depths it might be a good idea to see if she has any information for you.'''
# endregion

# region Farming Stuff
INFO_BLOODMOON = '''Every 168 unpaused minutes, the game will attempt to trigger a Blood Moon on the next night. If you are in a shrine or the Depths, the game will postpone the Blood Moon until the next night. Blood Moons will respawn most enemies and weapons. Soldier and Captain Constructs do not respawn on Blood Moons however; Their respawn mechanics are still being investigated.'''
POINT_FORCEMOON = '''
Here's are some links to examples of how to force a Blood Moon to occur in TotK:
Rock Wall Opal Method:
<https://youtu.be/cBolBE0792k>
Water Shock Method:
<https://youtu.be/WU01EY3dGc8>
'''
INFO_MATERIALTIMER = '''TotK's map is divided into a 10x8 grid of "cells". Every minute that you are not in a map cell, there is an additive chance that every material and animal in that cell will respawn.'''
INFO_SHOPRESTOCK = '''Shops restock at midnight. You can make them restock by waiting at a campfire or bed, then reloading the shop by fast traveling, or saving and reloading. Shops that are menus only require passing time, as opening the shop causes them to reload.'''
INFO_CHARGEFARM = '''
You can farm Crystallized Charges by:
-Defeating ||Master Kohga at each Abandoned Mine he appears at|| and ||each Temple Boss Rematch||, all of which each give a chest containing a Huge Crystallized Charge(worth 100 normal Crystallized Charges) the first time you defeat them.
-Visiting Yiga Bases and most Canyon Mines, which each have a chest with a Large Crystallized Charge(worth 20 normal Crystallized Charges)
-Defeating Mini-Bosses in the Depths, which drop a Large Crystallized Charge every Blood Moon.
'''
POINT_STARFARM = '''
Here's a link to an explanation on Star Fragment farming in TotK: 
https://www.reddit.com/r/zelda/comments/14ks4ci/totk_star_fragment_farming_guide_get_one_per/
'''
POINT_DRAGON = '''
Here's a link to a guide on Dragons and Dragon Part Farming in TotK: 
https://youtu.be/Pk27gun8xOw
'''
POINT_EARLYCASH = '''
Here's a link to a guide for getting rupees in early game: 
https://youtu.be/BJ5vAEiMwq8
'''
# endregion

# region Durability
INFO_OCTOROK = '''
You can repair and modify any non-Legendary equipment by dropping it on the ground in front of a Rock Octorok in Eldin Canyon. 
The Octorok will restore the Base and Bonus Durability of the equipment, as well as any equipment (not materials) fused to it. 

In addition, Rock Octoroks will modify the base equipment that they repair, from Tier 0 (no modifier) to Tier 1 (blue/white), Tier 1 to Tier 2 (orange), or Tier 2 to Tier 2. The modifier applied by the Octorok is random, based on the available modifiers for that equipment and the tier it is upgrading to. 
Please take a look at this spreadsheet to see the available modifiers and values for each modifier: 
<https://docs.google.com/spreadsheets/d/18pNtDx3z-8CwGJRmlW574xbQ6VphQOkvpZhClpOEVDA/edit#gid=328867100> 

You can save next to an Octorok before giving it equipment, and reload that save to reroll the modifier you get. 

Each Octorok can only be used once per Blood Moon, and will need to be killed after use in order to recharge on the next Blood Moon.
'''
INFO_REPAIRLEGEND = '''
You can repair any Legendary equipment by fusing it to a non-Legendary weapon or shield, then repairing that with a Rock Octorok. Then take it to the Break-A-Part Shop at Tarrey Town, which is located in the Akkala Highlands. Have Pelison break it down, and your Legendary equipment will be fully repaired.
'''
INFO_LEGENDLIST = '''
The following equipment cannot be modified by Rock Octoroks and is usually referred to as Legendary equipment: 

-Master Sword 
-Demon King's Bow 

Amiibo Weapons: 
-Sea-Breeze Boomerang 
-Sword of the Hero 
-White Sword of the Sky 
-Biggoron's Sword 
-Dusk Claymore 
-Fierce Deity Sword 
-Dusk Bow 
-Sea-Breeze Shield 

Champion's Arms: 
-Scimitar of the Seven 
-Boulder Breaker 
-Lightscale Trident 
-Great Eagle Bow 
-Daybreaker 

-Magic Rod 
-Magic Scepter 
-Magic Staff
'''
INFO_FUSEDURABILITY = '''
Each weapon has a Base Durability and a Bonus Durability, which is unlocked while something is fused to the weapon. 
Bonus Durability Values: 
-Stal Enemy Arms = 3 
-Gerudo Weapons excluding the Scimitar of the Seven = 5 
-Tree Branches, Tools, Rusty Weapons, Royal Guard Weapons, and Gloom Weapons = 10 
-All other weapons = 25 

Bonus Durability is inherent to the base weapon, and any Bonus Durability used will not be restored by fusing something else to the base weapon. Aside from materials that break in one hit such as Gibdo Bones and Ancient Blades, all materials will last until the base weapon breaks. When fusing equipment to a weapon, the base weapon will still unlock its Bonus Durability, but the fused equipment will not. The durability of both will be drained on hit.

When fusing equipment to a weapon or shield, the fused equipment will lose its modifier, but its Bonus Durability will be restored to maximum, if it is a weapon.
'''
POINT_WEAPONSINTACT = '''
Here's a link to an explanation on Pristine Weapons in TotK: 
<https://www.reddit.com/r/tearsofthekingdom/comments/13uqo9h/everything_you_need_to_know_about_nondecayed/>
Please note: Throwing a Decayed weapon against terrain to break it will NOT unlock it's Pristine variant in the Depths.
'''
# endregion

# region Mechanics and Hints
INFO_MASTERSWORD = '''The Master Sword has a base damage of 30, which increases to 45 when it is Awakened (nearby Gloom enemies). It has a Base Durability of 40 and a Bonus Durability of 25, but it does not currently recharge its Bonus Durability, meaning that after it runs out of energy for the first time it will only ever have a Total Durability of 40. When facing Phantom Ganon or ||Ganondorf||, it's base damage increases to 60, and it does not lose any durability on use.'''
INFO_CHERRY = '''If you are having trouble finding caves, try offering some fruit to a cherry tree. Doing so will reveal ALL cave entrances nearby for a decent amount of time.'''
INFO_BARGAINERSTATUES = '''Bargainer Statues are merchants that offer rare equipment and materials in return for Poes to guide into the afterlife. There are 7 in the game, 1 in Lookout Landing, and 6 found within the Depths. Each Bargainer Statue in the Depths is found ||directly below a Large Goddess Statue on the Surface or in the Sky||. The Bargainer Statues in the Depths will also sell most Amiibo weapons and armor to you after you have obtained them once.'''
INFO_ALTAMIIBOWEAPONSOURCE = '''
The White Sword of the Sky and the Dusk Bow cannot be repurchased from Baragainer Statues. Instead, the Dusk Bow can found at the top of Hyrule Castle every Blood Moon. The White Sword of the Sky can be reobtained from the Mother Goddess Statue by bringing her Dinraal's Claw, Farosh's Claw, and Naydra's Claw.
'''
INFO_BOTWDATA = '''
TotK automatically imports your BotW normal mode data upon creating a new game for TotK. The imported data includes: 
-Any registered horses you had, including unique horses, which will not spawn in TotK if you import them. 
-Your Champion's Ballad Photo, if you hung it on the wall in Link's House in BotW.
'''
INFO_COORDSYSTEM = '''TotK uses two different coordinate systems, one that is shown to the player, and one that is used internally. You can think of the shown coordinates as being X, Z, Y, where positive X is East on the map, positive Z is North on the map, and Y is your height. The internal coordinate system can be visualized as X, Y + 105, -Z.'''
INFO_DEPTHSMIRROR = '''
Hyrule's Depths mirror its Surface; Terrain is usually inverted, and bodies of water on the Surface are usually impassable walls in the Depths. 
If you don't yet have the map for the area of the Depths you are in, you can leave your map on the Surface to display the Surface on your Minimap, aiding in navigation.
'''
INFO_DEVICESHOP = '''After you have fully upgraded your Energy Cell to 48 total Energy Wells, you can use your Crystallized Charges at Crystal Refineries to purchase any Zonai Device. Each device costs 3 Charges per capsule, except for Big Batteries, which are 30 Charges each.'''
INFO_RITOFABRIC = '''The Original and Nostalgic Fabrics are the stand-ins for the Rito Fabric, as the Paraglider was made by the Rito for Hylians.'''
INFO_HORNEDSTATUE = '''After completing one part of "Regional Phenomena", a new opening can be found in the Emergency Shelter in Lookout Landing, through which you will find a statue with an ominous aura. This Horned Statue will allow you to trade Heart Containers for Stamina Vessels, and vice versa, at the cost of 20 rupees each.'''
INFO_SUNPUMPKIN = '''Compendium Entry #253 is the ||Sun Pumpkin||, a material that is not found within Hyrule until the completion of the quest "Homegrown in Hateno", which you can begin by speaking to Reede in the fields near the entrance to Hateno Village, after completing "The Mayoral Election".'''
INFO_BASEELEMENTALDMG = '''
Each enemy takes a specific amount of damage from each element. You can find the exact numbers for each enemy on the Monsters tab of Phil's Data Sheet: 
<https://docs.google.com/spreadsheets/d/1fBvQ17WHP3ASgtO8ode_rf1g4DfEHErMrHwwLppNTJM/edit#gid=143376740&range=A1>
'''
INFO_MISSABLELOCATIONS = '''
Here are some of the most commonly missed locations for TotK:
Surface:||
East and West Passages at Hyrule Castle
Sherfin's Secret Hot Spring
Dragonbone Mire
Kolomo Garrison Ruins
Gatepost Town Ruins
Water Reservoir
Castle Town Watchtower
Faron Woods
Sarjon Bridge
Ash Swamp
Oren Bridge
Luto's Crossing
All 3 Sokkala Bridges
Gero Pond
Royal Ancient Lab Ruins
Lanayru Road - West Gate
||
Depths:||
Visit every Canyon Mine and Lavafalls you can see on the map
Papetto Grove
Dracozu Altar
Hickaly Grove
Midla Grove
Ginner Grove
Retsam Grove
Blupee Burrow 
Applean Grove
||
Original message by 𝓣𝓻𝓲⃤
'''
INFO_MIDAIRWING = '''
Here are the steps to deploy a Wing midair in TotK: 
1. Let the Left Stick go neutral while paragliding, so that Link is falling straight down.
2. Open the Quick Menu or Pause Menu and drop a Wing.
3. Close the menu, then immediately tilt the Left Stick up to move forward.
4. Close the paraglider to land on the Wing.
'''
INFO_TRUEDAMAGE = '''
In TotK, the shown damage numbers for spears and two-handed weapons do not reflect their actual damage dealt. 
-The shown damage for spears is divided by 1.3268, which means that spears deal roughly 25 percent less damage per hit than shown. 
-The shown damage for two-handed weapons is divided by 0.95, which means that two-handed weapons deal roughly 5 percent more damage than shown.

These multipliers also affect modifiers to the weapon, such as the Fused item, Attack Up from a modifier, and Zonaite-Powered/Strong Fusion. They do not apply to temporary weapon buffs, such as those from the Attack Up effect, or conditional weapon abilities like Water Warrior.
'''
INFO_MISSINGARMOR = '''
The following armors from BotW are not available in TotK:
-Old Shirt and Well-Worn Trousers
-Warm Doublet
-Nintendo Switch Shirt
-Salvager's Set
-Ancient Set
-Gerudo Vai Set
-Thunder Helm (replaced by Lightning Helm)
-Champion's Tunic (nerfed into Tunic of Memories)
'''
INFO_JSCONTROL = '''The 5th Special Control is Jump Slash, and is obtained by reading the journal at the Monster Control Crew camp for Hoz's Squad. The camp can be found along the road west of Hyrule Field Chasm, or north of Dueling Peaks Stable, depending on your Side Adventure progress. If the camp is not at either location, wait until after a Blood Moon, and try them again.'''
INFO_MOATCHASM = '''In order to reach the Depths underneath Hyrule Forest Park(to the east of Hyrule Castle), try flying over the moat while searching the west side of the island for a small opening with a Chasm inside.'''
INFO_BREAKITDOWN = '''
You can break down most Fused weapons and shields into their base equipment and Fuse material by paying 20 rupees to Pelison at the Break-a-Part Shop in Tarrey Town. 
'''
INFO_GLEEOKSTRAT = '''
The trick to taking down Gleeoks is to use Eyeball arrows while avoiding its attacks or staying behind cover. Multi-shot bows are strongly recommended for this.
Flame Gleeoks take 2x damage from ice attacks and 1.5x damage from water attacks.
Frost Gleeoks take 2x damage from fire attacks.
'''
INFO_DUGBY = '''
Dugby's first quest is "The Ancient City Gorondia!", and has no pre-requisites in order to unlock. Dugby can be found at `1744, 2585, 427` for this quest.

Dugby's second quest is "The Ancient City Gorondia?", and requires the completion of "Yunobo of Goron City" and at least 30 minutes of unpaused gameplay to have passed since the completion of his first quest. Dugby can be found at `1614, 2399, 397` for this quest.
'''
# endregion

# region Effects and Builds
INFO_DEFENSESTAT = '''
Every enemy attack has two components: the enemy's base damage, and the damage of the weapon they are holding. The damage you take from the attack is then calculated by subtracting your total defense from the enemy attack.
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
 -Both the Radiant Set and the Evil Spirit Set grant Bone Proficiency, which when paired with a Molduga Jaw weapon and lvl 3 Attack Up from a meal grants the best damage increase.
 '''
INFO_MOISTURE = '''The Froggy armor set pieces each have a hidden effect called Moisturizing, which increases the length of time that Link will be wet for, up to a max of 4 minutes.'''
INFO_WEATHERATK = '''The Weather Attack effects do not increase physical weapon damage. They add an elemental AoE to combo finishers and charge attacks, which increases in size with higher effect levels and has a bonus elemental damage of 5, regardless of level. The Weather Charge set bonus just gives you Quick Charge when active.'''
INFO_GLOOMATKRES = '''The Gloom Attack Resist set bonus does not have any impact on gloom attacks. It only adds a fourth gloom resistance heart.'''
INFO_SLIPRESIST = '''Slip Resistance increases the amount of time that Link can climb on slippery surfaces before slipping. With levels 1/2/3 of Slip Resistance, Link will be able to climb on slippery surfaces for 6/8/10 seconds before slipping. Slip Proof is the Froggy Armor set bonus, and makes Link immune to slipping.'''
INFO_ATKSTACK = '''The Attack Up effect can only stack up to a total of level 3 (for 1.5x damage), combining both armor and meal effects.'''
INFO_BONEPROF = '''
"(Stal) Disguise; Bone Weap. Prof." is the set bonus for the Evil Spirit set and Radiant set.
The Bone Proficiency effect multiplies bone weapon damage by 1.8x, and stacks with lvl 3 Attack Up from a meal.

The Evil Spirit set pieces each have Stealth Up cannot be upgraded, and together grant the set bonus at base level. The Evil Spirit set can be acquired by ||completing the quests that begin at each of the three labyrinths.||

The Radiant set has no innate effects, but can be upgraded and grants the set bonus at 2 stars. It can be purchased from the Armor Shop in Kakariko Village.
'''
INFO_BACKSCRATCH = '''
The current maximum damage that you can consistently output can be referred to as a Lynel Backscratcher build. Take a Pristine Royal Guard's Claymore with a +10 Attack Up modifier, fuse a Molduga Jaw to it, then wear it down until it has 1 durability left. 
Then wear a Bone Proficiency armor set and eat a level 3 Attack Up meal, and take the weapon and only use it for mounted attacks on a Lynel. The mounted attacks take no durability, so you can continually deal critical hit damage. 

Here is the full math behind this:
rounddown(42 Base Weapon Damage + rounddown((10 Modifier Buff + 32 Molduga Jaw Fuse Damage)/0.95 Two-Handed Weapon Multiplier) * 1.5 Attack Up Meal * 1.8 Bone Proficiency * 2 Breaking Point * 2 Last Hit Critical) = 928 total damage per hit.
'''
INFO_FRAGILEONLYNEL = '''Materials that break after one hit, such as Gibdo Bones or Ancient Blades, will still break after one hit during mounted attacks on a Lynel, as the mounted attacks only prevent *durability* loss, and materials do not have durability.'''
POINT_DMGCALC = '''
Here's a link to KreaTV1's Damage Calculator for TotK:
https://tinyurl.com/TotK-Damage-Calc
'''
# endregion

# region Reference Info
POINT_TRACKER = '''
Here's a link to the 100% Tracker Spreadsheet for TotK: 
https://docs.google.com/spreadsheets/d/1mRHxETl2bYvpRBGV7VzeW0bCdpmEbJJdt7aWAw9T0rY/edit?usp=sharing
Please feel free to make a copy for yourself so you can check off your progress by selecting `File -> Make a Copy`.
'''
POINT_INTERACTMAPS = '''
Here are some links to interactive maps: 
Zelda Universe: <https://zeldamaps.com/?game=TotK> 
Zelda Dungeon: <https://www.zeldadungeon.net/tears-of-the-kingdom-interactive-map/> 
AeonSake: <https://totk.aeonsake.com/> 

Object Map: <https://objmap-totk.zeldamods.org/#/map/z2,0,0>
'''
INFO_OBJECTMAP = '''
The Object Map is a very powerful tool for locating things within TotK: 
https://objmap-totk.zeldamods.org/#/map/z2,0,0 

-Click on the "Help" button below the search bar to see some information on what terms to use. 
-The Filters menu below the Search menu will allow you to reveal different icons and sections on the map. 
-You can use these terms to filter search results by map level: 
`surface` 
`depths` 
`cave` 
`sky`
-You can filter your search by scaling or non-scaling objects using `scale:1` or `scale:0`, respectively.
'''
INFO_USEFULOBJECTTERMS = '''
Here are some terms/actor names that might be useful when using the Object Map:

-`WallCrack`, `RockBroken` - Light Gray Cracked Rocks/Rock Walls
-`AutoGenerateDestructibleActorHardnessLv1` - Red Cracked Rock
-`AutoGenerateDestructibleActorHardnessLv2` - Blue Cracked Rock
-`AutoGenerateDestructibleActorHardnessLv3` - Dark Gray Cracked Rock
-`AutoGenerateDestructibleActorLuminous` - Luminous Ore Walls
-`AutoGenerateDestructibleActorZonanium` - Zonaite Ore Walls
-`BokoblinBasket` - Bokoblins with baskets on their backs.
-`MinusFieldGhost` - Depths Ghosts
-`TreeStumpHolySpot_B` - Triple Depths Ghosts, also doubles as the locations of the Calamity Monuments
-||`dungeonboss underground`|| - ||Temple Boss Rematches||
-`DgnObj_Zonau_SliderBox_A_02` - Elevator Rail
-`MiasmaSwarm`, `Phantom Ganon` - Gloom Spawn/Phantom Ganon
  Some Gloom Spawn are controlled by certain flags:
  -`MiasmaSwarm_RandomSet`, `MiasmaSwarm_RandomSet3` - Randomized on load; these can be save-scummed to get them to spawn
  You can search for Phantom Ganons with specific Gloom Weapons
  -`NOT EquipWeaponType 2 NOT EquipWeaponType 3` - Gloom Sword
  -`EquipWeaponType 2` - Gloom Club
  -`EquipWeaponType 3` - Gloom Spear
'''
POINT_DATAECHO = '''
Here's a link to Echocolat's Data Sheet for TotK: 
https://docs.google.com/spreadsheets/d/18pNtDx3z-8CwGJRmlW574xbQ6VphQOkvpZhClpOEVDA/edit#gid=114269320
'''
POINT_DATAPHIL = '''
Here's a link to Phil's Data Sheet for TotK: 
https://docs.google.com/spreadsheets/d/1fBvQ17WHP3ASgtO8ode_rf1g4DfEHErMrHwwLppNTJM/edit#gid=1307828066
'''
POINT_WORLDEXP = '''
Here's a link to an explanantion on Level Scaling in TotK: 
https://www.reddit.com/r/tearsofthekingdom/comments/1496az3/explaining_level_scaling_in_totk/
'''
POINT_TEMPLESCALING = '''
Here's a link to an explanation on Temple Boss Scaling in TotK: 
https://www.reddit.com/r/tearsofthekingdom/comments/14rr5sd/how_temple_bosses_scale_a_full_breakdown/
'''
POINT_SAGELVL = '''
Here's a link to an explanation on Sage Attack Power: 
https://www.reddit.com/r/tearsofthekingdom/comments/14ct8kt/sage_attack_power_a_full_breakdown/
'''
POINT_BEEDLETRADES = '''
Here's a link to a list of all Beedle Trades: 
https://docs.google.com/spreadsheets/d/1QMCSV19HFazu-dQuz0vN5lBDlMwXDYciUEYgG3h57ZQ/edit#gid=0
'''
POINT_COOKING = '''
Here's a link to a guide about cooking: 
https://youtu.be/ho3fZyokkg8
'''
POINT_HOVERBIKE = '''
Here's a link to a guide on building a Hoverbike: 
https://youtu.be/oq4LmYEFlHM
'''
POINT_MAPCOMPLETION = '''
Here's a link to an explanation of what counts towards Map Completion in TotK:
https://youtu.be/wvL0YnIjyCU
'''
POINT_RECIPECALC = '''
Here are some links to Recipe Calculators for TotK:
https://www.zelda.recipes/
https://zeldacookbook.vercel.app/
'''
POINT_PHILARMORCALC = '''
Here's a link to make a copy of Phil's Armor Material Calculator:
<https://docs.google.com/spreadsheets/d/1gzS-kViCZ6c4GCDdUFiwfx_Fih2sbcwJm5czzKLJvGo/copy>
'''
POINT_AMIIBODROPTABLES = '''
Here's a link to the Amiibo Drop Tables Spreadsheet:
https://docs.google.com/spreadsheets/d/1dcw7GRsrwMHO8-iZsjuUsZ0WanA6Krb4WyxG124Kt7I/edit?usp=sharing
'''
POINT_GLITCHSHEET = '''
Here's a link to the Glitch Spreadsheet:
https://docs.google.com/spreadsheets/d/1xNB1gOLZRSF9yp1mHUsS9ymogRJa1Wz8rTliTXezeRM/edit?usp=sharing
'''
POINT_HOVERBIKEv4 = '''
Here's a link to a guide on building the Hoverbike 4.0:
https://youtu.be/AXWAEBlvIXs
'''
POINT_COOKCALC = '''
Here's a link to a cooking calculator for TotK:
https://www.totkcookbook.com/
'''
POINT_CONSTRUCTHORNFARM = '''
Here's a link to a guide on where to farm Construct Horns inside Proving Grounds Shrines:
https://www.reddit.com/r/TOTK/comments/15d3ksj/proving_grounds_shrines_construct_farming/
'''
POINT_SHRINEFINDER = '''
Here's a link to a website that can help you find what Shrines and Lightroots you are missing:
<https://www.haokepeng.com/zelda>
If you are having trouble using this site, please feel free to head to <#753016129328250964> and post screenshots of your maps so the experts can help you find what you're missing.
'''
POINT_TRANSFERSCREENSHOTS = '''
Here's a link to an article explaining how to transfer screenshots from your switch to your smartphone:
<https://en-americas-support.nintendo.com/app/answers/detail/a_id/53138/kw/how%20to%20transfer%20Screenshots%20and%20Video%20Captures%20to%20a%20Smart%20Device%20Wirelessly>
'''
POINT_LEVELCARDS = '''
Here's a link to a gallery of level cards for you to use with Arcane's `/card image set` command:
NOTE: It is recommended to use 70 percent opacity `/card opacity <number>`.
<https://imgur.com/gallery/jP6Adci>
'''
POINT_INTEROBJECTSHEET = '''
Here's a link to Phil's Interactable Objects Sheet for TotK:
https://docs.google.com/spreadsheets/d/1eHHFwGDsI3sHTOLaawlxKgxbiLG8ceHUHpbpC2Bj57k/edit?usp=sharing
'''
POINT_DONDON = '''
Here are some links to information on what gems Dondons can give:
Video Guide: <https://youtu.be/BGxltmsZaAI>
Drop Table Sheet: <https://docs.google.com/spreadsheets/d/1bj_1KHBFgr-1tyc1HJIHTXmLgws3mWnTTgVyg8LSZVY/edit#gid=0>
'''
POINT_ARROWFARM = '''
Here's a link to a guide on farming arrows in TotK:
https://youtu.be/wR-6ThhtO5U
'''
# endregion

# region Meta Info
INFO_DUPE112 = '''
Here are some links for duplication glitches for 1.1.2:
Tobio's Hollow Chasm Duplication:
<https://youtu.be/E8nab6JNBts>
Shock Duping (For equipment):
<https://youtu.be/dFsNK8bf1io>
Autobuild Duplication (For rupee farming):
<https://youtu.be/RKsvliFBCV4>
Rock Octorok Recall (For most equipment):
<https://youtu.be/0cR_fbx-P_Y>
Midair Inventory Shift Dupe w/ Dispenser Storage:
<https://youtu.be/OVWuFLYSGiE>
Midair Inventory Shift Dupe (For creatures):
<https://youtu.be/33pm1D6ugh0>
Save Load Dupe (For throwable equipment):
<https://youtube.com/shorts/N26xvLp2F1I>
Weapon Stat Transfer:
<https://youtu.be/9jJbAJdP3d8>
'''
INFO_DUPE120 = '''
Here are some links for duplication glitches on 1.2.0:
Bomb/Elemental Fruit Dupe:
<https://youtu.be/BZID7B_99QY?t=21>
Minus Duping:
<https://youtu.be/BZID7B_99QY?t=223>
Vendor Scamming:
<https://youtu.be/BZID7B_99QY?t=456>
Zonai Inventory Shift Duplication(ZISD):
<https://youtu.be/BZID7B_99QY?t=685>
Midair Throw Duplication(MTD):
<https://youtu.be/BZID7B_99QY?t=827>
MTD w/ Dispenser Storage:
<https://youtu.be/BZID7B_99QY?t=977>
Like-Like Fuse Entanglement:
<https://youtu.be/BZID7B_99QY?t=1207>
Weapon Stat Transfer(WST) w/ Like-Like Fuse Entanglement:
<https://youtu.be/Jw2HWQTKS8w>
Sluggling:
<https://youtu.be/BZID7B_99QY?t=1553>
'''
INFO_DUPE121 = '''
Here are some links for duplication glitches on 1.2.1:
Vendor Scamming:
NOTE: This glitch is limited, and will need to be re-performed every 5 items.
<https://youtu.be/LCc1525GlHo?t=138>
Minus Duping:
<https://youtu.be/bV1KxESU9v8?t=17>
Dispenser Storage (Used with Minus Duping):
<https://youtu.be/LCc1525GlHo?t=434>
Zonai Inventory Shift Duplication (ZISD):
<https://youtu.be/LCc1525GlHo?t=561>
Midair Throw Duplication (MTD):
NOTE: This is for Zonai Devices ONLY.
<https://youtu.be/LCc1525GlHo?t=693>
MTD for other materials:
<https://youtu.be/bV1KxESU9v8?t=283>
'''
INFO_RAILPART = '''
Here are some links to videos showing how to detach an Elevator Rail:
Stabilizer Method (Construct Factory, Right Leg Depot)
<https://www.reddit.com/r/HyruleEngineering/comments/14qj7qw/simple_and_low_part_cost_way_to_detach_the/>
Rocket Method (Bottom of Great Plateau West Chasm/Ancient Underground Fortress)
<https://youtu.be/d5LeqKkJdYQ>
'''
POINT_UNRELEASEDAMIIBO = '''
Here's a link to a guide on obtaining the Unreleased TotK Zelda and Ganondorf Amiibo Paraglider Fabrics:
https://youtu.be/ZuohEzyhKxM
'''
INFO_DOWNPATCH = '''
You cannot downpatch your game without losing your save data. You can only downpatch to 1.0, unless you have access to another Switch with a version in between 1.0 and current patch. 

To downpatch to 1.0, you will need to have a physical copy of the game, and to factory reset your Switch. After doing so, make sure you keep your Switch from updating the software, either by disconnecting it from the internet or by turning off auto-updates and rejecting the prompts to update. 

If you have access to a Switch with a version between 1.0 and current patch, you can match your update with it after factory resetting your Switch.
'''
INFO_CHECKGAMEVERSION = '''You can check your game version by pressing `+` on your controller from the Home Screen.'''
POINT_BETTERPHOTOS = '''
Here's a link to a guide on taking higher quality photos in TotK:
https://youtu.be/Bi7BC4wSjI8
'''
POINT_WHEREDLC = '''
Here's a link to a video explaining the situation regarding DLC for TotK:
https://youtu.be/DY-qfykgeuQ
'''
# endregion

# region Image Messages
IMAGE_ARMORTOTAL = '''Here are all of the totals for materials required to fully upgrade every armor in TotK:'''
IMAGE_HORSEUPGRADE = '''Here are the meals needed to upgrade a horse to maximum in TotK:'''
IMAGE_ORETOTAL = '''Here are the totals for Ores/Misc materials required to upgrade every armor in TotK:'''
IMAGE_DRAGONTOTAL = '''Here are the totals for Dragon Parts required to upgrade every armor in TotK:'''
IMAGE_HORNTOTAL = '''Here are the totals for Monster Horns required to upgrade every armor in TotK:'''
IMAGE_GUTTAILTOTAL = '''Here are the totals for Monster Guts/Tails required to upgrade every armor in TotK:'''
IMAGE_MEATANDADDITIVETOTAL = '''Here are the totals for Meats and Additives required to upgrade every armor in TotK:'''
IMAGE_FRUITANDVEGGIETOTAL = '''Here are the totals for Fruits and Veggies required to upgrade every armor in TotK:'''
IMAGE_OTHERPARTTOTAL = '''Here are the totals for Other Monster Parts required to upgrade every armor in TotK:'''
IMAGE_CRITTERTOTAL = '''Here are the totals for Critters required to upgrade every armor in TotK:'''

IMAGE_ASCENDMAP = '''Here is a map of all the Ascend Points within the Depths:'''
IMAGE_CHERRYMAP = '''Here is a map of all the Cherry Trees:'''
IMAGE_MISKOBANNER = '''The Great Bandit Misko left distinct banners along the path to their treasure. The banners don't point directly to the treasure, but you can follow from one banner to the next to find the hidden spoils.'''
IMAGE_DMGFORMULA = '''
Here is the damage formula for Link's attacks in TotK; for more information, please check out the Damage Calculations Doc:
<https://docs.google.com/document/d/1K5hLcxfnvSnY-nsIP-n8Ew7rm9EkqHtnn6iJqOnxlng/edit?usp=sharing>
'''
IMAGE_INVENTORYUPGRADES = '''Here are all of the Inventory upgrade costs:'''
IMAGE_SHRINECOUNTS = '''Here are the totals of each type of Shrine of Light in TotK:'''
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
Lanayry Sky Archipelago - 20%
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
There are no Device Dispensers that provide Big Batteries. They can only be obtained from chests and Crystal Refineries(after you have fully upgraded your Energy Cell).
'''
DISP_SPRING = '''
North Necluda Sky Archipelago - 40%
Valor Island - 30%
Gerudo Canyon Pass - 15%
Lightcast Island - 15%
'''
DISP_CANNON = '''
North Necluda Sky Archipelago - 20%
Sotuh Necluda Sky Archipelago - 20%
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
COMMAND_OBJMAPNOTE = '''Note: You can change what layer of the Object Map is shown with the Layer button in the top right corner.'''
COMMAND_OBJMAPBASELINK = '''https://objmap-totk.zeldamods.org/#/map/z2,0,0,'''
CONVERT_COORD1 = '''The Object Map coordinates: '''
CONVERT_COORD2 = ''' are equivalent to the shown in-game coordinates: '''
COMMAND_FINDPRISTINE1 = '''Here are the Ghosts in the Depths that can spawn a Pristine '''
COMMAND_HELLO1 = '''Hi!'''
COMMAND_HELLO2 = '''Hello!'''
COMMAND_HELLO3 = '''Greetings!'''
# endregion

# Unimplemented Messages --- UPDATE HELP ---