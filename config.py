# config.py

import tokens

TESTMODE = True

# Servers
DEVSERVERID = 1124106113852379156

GENSERVERID = 753016125566091396
DATASERVERID = 1111764095826415678
WIKISERVERID = 471372235957993474

AUTHSERVERS = [DEVSERVERID, GENSERVERID, DATASERVERID, WIKISERVERID]

# Channels
DEVSERVERCHANNELID_TSTRAURUSYS = 1150154393933594644
DEVSERVERCHANNELID_RAURUSYS = 1150154644920738013

GENSERVERCHANNELID_QC = 753016129328250964
GENSERVERCHANNELID_BF = 811092574672388106
GENSERVERCHANNELID_TGEN = 753016129328250963

# Roles
GENSERVERROLEID_ADMIN = 753016125838721113
GENSERVERROLEID_SENIORMOD = 1081923721465446410
GENSERVERROLEID_MOD = 753016125838721112
GENSERVERROLEID_TRIALMOD = 1104905294498242690

DATASERVERROLEID_MOD = 1111799962976665661

WIKISERVERROLEID_COMMUNITYSTAFF = 612461654990651432

ADMINROLES = [GENSERVERROLEID_ADMIN, GENSERVERROLEID_SENIORMOD, GENSERVERROLEID_MOD, GENSERVERROLEID_TRIALMOD, DATASERVERROLEID_MOD, WIKISERVERROLEID_COMMUNITYSTAFF]

# Users
USERNAME_RAURUBOT = 'Rauru'
USERNAME_TESTRAURUBOT = 'TestRauru'
USERNAME_CURSEDRAURU = 'R̶̽̚a̸̐͛u̶͔͝r̶͋̇u̷͠͝'
USERID_RAURUBOT = 1123940271483265114
USERID_TESTRAURUBOT = 1134667595019206818

USERID_DOGE229 = 294110601339469825

BOT_AUTHADMINS = [USERID_DOGE229]


RAURUBOT_TOKEN = tokens.TOKEN1
TESTRAURUBOT_TOKEN = tokens.TOKEN2