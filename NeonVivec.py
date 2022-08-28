import tkinter as tk  # import tk for mainframe
from tkinter.simpledialog import askstring  # import simpledialog with askstring
from tkinter import filedialog  # import filedialog
from PyQt6 import QtWidgets, uic # import PyQT6 widgets
from PyQt6.QtCore import Qt # import PyQT6 for external GUI
import tkinter # import tkinter
import sys # import sys for QT widget UI
import os  # import os for path related code
import shutil  # import shutil for copying files
import subprocess  # import subprocess for executing terminal commands

root = tk.Tk() # create a mainframe for application
root.withdraw() # hide the mainframe from view
currentdirectory = os.getcwd()  # acquire current directory
temporarydirectory = filedialog.askdirectory(
    parent=root, initialdir=currentdirectory, title='Please select tes3mp folder directory') # set temp dir through file dialog

def copy():  # copy .bat files to the morrowind directory
    dir = os.path.join(currentdirectory, './' + 'scripts')  # set a path to script files
    files = os.listdir(dir)  # prepare file list
    for fname in files:  # copy scripts
        shutil.copy(os.path.join(dir, fname), temporarydirectory)
    return

copy() # invoke copy method

enabledBoo = tkinter.BooleanVar() # declare variable
passTimeWhenEmptyBoo = tkinter.BooleanVar() # declare variable
allowConsoleBoo = tkinter.BooleanVar()  # declare variable
allowBedRestBoo = tkinter.BooleanVar() # declare variable
allowWildernessRestBoo = tkinter.BooleanVar() # declare variable
allowWaitBoo = tkinter.BooleanVar() # declare variable
shareJournalBoo = tkinter.BooleanVar() # declare variable
shareFactionRanksBoo = tkinter.BooleanVar() # declare variable
shareFactionExpulsionBoo = tkinter.BooleanVar() # declare variable
shareFactionReputationBoo = tkinter.BooleanVar() # declare variable
shareTopicsBoo = tkinter.BooleanVar() # declare variable
shareBountyBoo = tkinter.BooleanVar() # declare variable
shareReputationBoo = tkinter.BooleanVar() # declare variable
shareMapExplorationBoo = tkinter.BooleanVar() # declare variable
shareVideosBoo = tkinter.BooleanVar() # declare variable
respawnAtImperialShrineBoo = tkinter.BooleanVar() # declare variable
respawnAtTribunalTempleBoo = tkinter.BooleanVar() # declare variable
playersRespawnBoo = tkinter.BooleanVar() # declare variable
bountyResetOnDeathBoo = tkinter.BooleanVar() # declare variable
bountyDeathPenaltyBoo = tkinter.BooleanVar() # declare variable
allowSuicideCommandBoo = tkinter.BooleanVar() # declare variable
allowFixmeCommandBoo = tkinter.BooleanVar() # declare variable
enablePlayerCollisionBoo = tkinter.BooleanVar() # declare variable
enforceDataFilesBoo = tkinter.BooleanVar() # declare variable

file = 'config.lua'  # point to the configuration
file = open(os.path.join(temporarydirectory, file), "r+")  # open configuration with read/write permission
content = file.readlines()  # read file to a variable

serverfile = 'tes3mp-server-default.cfg'  # point to the configuration
serverfile = open(os.path.join(temporarydirectory, serverfile), "r+")  # open configuration with read/write permission
servercontent = serverfile.readlines()  # read file to a variable

key = "passTimeWhenEmpty"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        passTimeWhenEmpty = line[27:]  # assign line to a variable and trim characters it
        passTimeWhenEmpty = passTimeWhenEmpty.strip()
        if (passTimeWhenEmpty == "false"):
            passTimeWhenEmptyBoo = False
        else:
            passTimeWhenEmptyBoo = True

key = "allowConsole"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        allowConsole = line[22:]  # assign line to a variable and trim characters before it
        allowConsole = allowConsole.strip()
        if (allowConsole == "false"):
            allowConsoleBoo = False
        else:
            allowConsoleBoo = True

key = "allowBedRest"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        allowBedRest = line[22:]  # assign line to a variable and trim characters before it
        allowBedRest = allowBedRest.strip()
        if (allowBedRest == "false"):
            allowBedRestBoo = False
        else:
            allowBedRestBoo = True

key = "allowWildernessRest"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        allowWildernessRest = line[29:]  # assign line to a variable and trim characters before it
        allowWildernessRest = allowWildernessRest.strip()
        if (allowWildernessRest == "false"):
            allowWildernessRestBoo = False
        else:
            allowWildernessRestBoo = True

key = "allowWait"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        allowWait = line[19:]  # assign line to a variable and trim characters before it
        allowWait = allowWait.strip()
        if (allowWait == "false"):
            allowWaitBoo = False
        else:
            allowWaitBoo = True

key = "shareJournal"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        shareJournal = line[22:]  # assign line to a variable and trim characters before it
        shareJournal = shareJournal.strip()
        if (shareJournal == "false"):
            shareJournalBoo = False
        else:
            shareJournalBoo = True

key = "shareFactionRanks"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        shareFactionRanks = line[27:]  # assign line to a variable and trim characters before it
        shareFactionRanks = shareFactionRanks.strip()
        if (shareFactionRanks == "false"):
            shareFactionRanksBoo = False
        else:
            shareFactionRanksBoo = True

key = "shareFactionExpulsion"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        shareFactionExpulsion = line[31:]  # assign line to a variable and trim characters before it
        shareFactionExpulsion = shareFactionExpulsion.strip()
        if (shareFactionExpulsion == "false"):
            shareFactionExpulsionBoo = False
        else:
            shareFactionExpulsionBoo = True

key = "shareFactionReputation"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        shareFactionReputation = line[32:]  # assign line to a variable and trim characters before it
        shareFactionReputation = shareFactionReputation.strip()
        if (shareFactionReputation == "false"):
            shareFactionReputationBoo = False
        else:
            shareFactionReputationBoo = True

key = "shareTopics"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        shareTopics = line[21:]  # assign line to a variable and trim characters before it
        shareTopics = shareTopics.strip()
        if (shareTopics == "false"):
            shareTopicsBoo = False
        else:
            shareTopicsBoo = True

key = "shareBounty"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        shareBounty = line[21:]  # assign line to a variable and trim characters before it
        shareBounty = shareBounty.strip()
        if (shareBounty == "false"):
            shareBountyBoo = False
        else:
            shareBountyBoo = True

key = "shareReputation"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        shareReputation = line[25:]  # assign line to a variable and trim characters before it
        shareReputation = shareReputation.strip()
        if (shareReputation == "false"):
            shareReputationBoo = False
        else:
            shareReputationBoo = True

key = "shareMapExploration"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        shareMapExploration = line[29:]  # assign line to a variable and trim characters before it
        shareMapExploration = shareMapExploration.strip()
        if (shareMapExploration == "false"):
            shareMapExplorationBoo = False
        else:
            shareMapExplorationBoo = True

key = "shareVideos"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        shareVideos = line[21:]  # assign line to a variable and trim characters before it
        shareVideos = shareVideos.strip()
        if (shareVideos == "false"):
            shareVideosBoo = False
        else:
            shareVideosBoo = True

key = "respawnAtImperialShrine"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        respawnAtImperialShrine = line[33:]  # assign line to a variable and trim characters before it
        respawnAtImperialShrine = respawnAtImperialShrine.strip()
        if (respawnAtImperialShrine == "false"):
            respawnAtImperialShrineBoo = False
        else:
            respawnAtImperialShrineBoo = True

key = "respawnAtTribunalTemple"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        respawnAtTribunalTemple = line[33:]  # assign line to a variable and trim characters before it
        respawnAtTribunalTemple = respawnAtTribunalTemple.strip()
        if (respawnAtTribunalTemple == "false"):
            respawnAtTribunalTempleBoo = False
        else:
            respawnAtTribunalTempleBoo = True

key = "playersRespawn"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        playersRespawn = line[24:]  # assign line to a variable and trim characters before it
        playersRespawn = playersRespawn.strip()
        if (playersRespawn == "false"):
            playersRespawnBoo = False
        else:
            playersRespawnBoo = True

key = "bountyResetOnDeath"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        bountyResetOnDeath = line[28:]  # assign line to a variable and trim characters before it
        bountyResetOnDeath = bountyResetOnDeath.strip()
        if (bountyResetOnDeath == "false"):
            bountyResetOnDeathBoo = False
        else:
            bountyResetOnDeathBoo = True

key = "bountyDeathPenalty"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        bountyDeathPenalty = line[28:]  # assign line to a variable and trim characters before it
        bountyDeathPenalty = bountyDeathPenalty.strip()
        if (bountyDeathPenalty == "false"):
            bountyDeathPenaltyBoo = False
        else:
            bountyDeathPenaltyBoo = True

key = "allowSuicideCommand"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        allowSuicideCommand = line[29:]  # assign line to a variable and trim characters before it
        allowSuicideCommand = allowSuicideCommand.strip()
        if (allowSuicideCommand == "false"):
            allowSuicideCommandBoo = False
        else:
            allowSuicideCommandBoo = True

key = "allowFixmeCommand"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        allowFixmeCommand = line[27:]  # assign line to a variable and trim characters before it
        allowFixmeCommand = allowFixmeCommand.strip()
        if (allowFixmeCommand == "false"):
            allowFixmeCommandBoo = False
        else:
            allowFixmeCommandBoo = True

key = "enablePlayerCollision"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        enablePlayerCollision = line[31:]  # assign line to a variable and trim characters before it
        enablePlayerCollision = enablePlayerCollision.strip()
        if (enablePlayerCollision == "false"):
            enablePlayerCollisionBoo = False
        else:
            enablePlayerCollisionBoo = True

key = "enforceDataFiles"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        enforceDataFiles = line[26:]  # assign line to a variable and trim characters before it
        enforceDataFiles = enforceDataFiles.strip()
        if (enforceDataFiles == "false"):
            enforceDataFilesBoo = False
        else:
            enforceDataFilesBoo = True

key = "loginTime"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        loginTime = line[19:]  # assign line to a variable and trim characters before it
        loginTime = loginTime.strip()

key = "config.difficulty"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        difficulty = line[20:]  # assign line to a variable and trim characters before it
        difficulty = difficulty.strip()

key = "config.deathTime"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        deathTime = line[19:]  # assign line to a variable and trim characters before it
        deathTime = deathTime.strip()

key = "config.deathPenaltyJailDays"  # search phrase
for line in content:
    if key in line:  # search for the phrase
        deathPenaltyJailDays = line[30:]  # assign line to a variable and trim characters before it
        deathPenaltyJailDays = deathPenaltyJailDays.strip()

key = "enabled = "  # search phrase
for line in servercontent:
    if key in line:  # search for the phrase
        enabled = line[10:]  # assign line to a variable and trim characters before it
        enabled = enabled.strip()
        if (enabled == "false"):
            enabledBoo = False
        else:
            enabledBoo = True

key = "hostname = "  # search phrase
for line in servercontent:
    if key in line:  # search for the phrase
        hostname = line[10:]  # assign line to a variable and trim characters before it
        hostname = hostname.strip()

key = "maximumPlayers = "  # search phrase
for line in servercontent:
    if key in line:  # search for the phrase
        maximumPlayers = line[17:]  # assign line to a variable and trim characters before it
        maximumPlayers = maximumPlayers.strip()

key = "password = "  # search phrase
for line in servercontent:
    if key in line:  # search for the phrase
        password = line[11:]  # assign line to a variable and trim characters before it
        password = password.strip()

key = "localAddress = "  # search phrase
serverfile = os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg')  # pointing to the config
with open(serverfile) as serverfile:  # open file
    lines = serverfile.readlines()  # read file
for line_number, line in enumerate(lines, 1):  # number lines
    if key in line:  # search for the phrase
        localaddrline = line_number - 1
        localaddr = lines[localaddrline]
        localaddr = localaddr[15:]
        portline = line_number
        port = lines[portline]
        port = port[7:]

class Ui(QtWidgets.QMainWindow): # class for GUI

    def __init__(self): # initialise GUI function
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('mainwindow.ui', self) # Load the .ui file

        self.passTimeWhenEmpty = self.findChild(QtWidgets.QCheckBox, 'passTimeWhenEmpty') # Find the checkbox
        if passTimeWhenEmptyBoo == True: # Read value
            self.passTimeWhenEmpty.setCheckState(Qt.CheckState.Checked) # check box
        if passTimeWhenEmptyBoo == False: # Read value
            self.passTimeWhenEmpty.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.passTimeWhenEmpty.stateChanged.connect(self.passTimeWhenEmptyChecked) # call passTimeWhenEmptyChecked method

        self.allowConsole = self.findChild(QtWidgets.QCheckBox, 'allowConsole') # Find the checkbox
        if allowConsoleBoo == True: # Read value
            self.allowConsole.setCheckState(Qt.CheckState.Checked) # check box
        if allowConsoleBoo == False: # Read value
            self.allowConsole.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.allowConsole.stateChanged.connect(self.allowConsoleChecked) # call allowConsoleChecked method

        self.allowBedRest = self.findChild(QtWidgets.QCheckBox, 'allowBedRest') # Find the checkbox
        if allowBedRestBoo == True: # Read value
            self.allowBedRest.setCheckState(Qt.CheckState.Checked) # check box
        if allowBedRestBoo == False: # Read value
            self.allowBedRest.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.allowBedRest.stateChanged.connect(self.allowBedRestChecked) # call allowBedRestChecked method

        self.allowWildernessRest = self.findChild(QtWidgets.QCheckBox, 'allowWildernessRest') # Find the checkbox
        if allowWildernessRestBoo == True: # Read value
            self.allowWildernessRest.setCheckState(Qt.CheckState.Checked) # check box
        if allowWildernessRestBoo == False: # Read value
            self.allowWildernessRest.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.allowWildernessRest.stateChanged.connect(self.allowWildernessRestChecked) # call allowWildernessRestChecked method

        self.allowWait = self.findChild(QtWidgets.QCheckBox, 'allowWait') # Find the checkbox
        if allowWaitBoo == True: # Read value
            self.allowWait.setCheckState(Qt.CheckState.Checked) # check box
        if allowWaitBoo == False: # Read value
            self.allowWait.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.allowWait.stateChanged.connect(self.allowWaitChecked) # call allowWaitChecked method

        self.shareJournal = self.findChild(QtWidgets.QCheckBox, 'shareJournal') # Find the checkbox
        if shareJournalBoo == True: # Read value
            self.shareJournal.setCheckState(Qt.CheckState.Checked) # check box
        if shareJournalBoo == False: # Read value
            self.shareJournal.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.shareJournal.stateChanged.connect(self.shareJournalChecked) # call shareJournalChecked method

        self.shareFactionRanks = self.findChild(QtWidgets.QCheckBox, 'shareFactionRanks') # Find the checkbox
        if shareFactionRanksBoo == True: # Read value
            self.shareFactionRanks.setCheckState(Qt.CheckState.Checked) # check box
        if shareFactionRanksBoo == False: # Read value
            self.shareFactionRanks.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.shareFactionRanks.stateChanged.connect(self.shareFactionRanksChecked) # call shareFactionRanksChecked method

        self.shareFactionExpulsion = self.findChild(QtWidgets.QCheckBox, 'shareFactionExpulsion') # Find the checkbox
        if shareFactionExpulsionBoo == True: # Read value
            self.shareFactionExpulsion.setCheckState(Qt.CheckState.Checked) # check box
        if shareFactionExpulsionBoo == False: # Read value
            self.shareFactionExpulsion.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.shareFactionExpulsion.stateChanged.connect(self.shareFactionExpulsionChecked) # call shareFactionExpulsionChecked method

        self.shareFactionReputation = self.findChild(QtWidgets.QCheckBox, 'shareFactionReputation') # Find the checkbox
        if shareFactionReputationBoo == True: # Read value
            self.shareFactionReputation.setCheckState(Qt.CheckState.Checked) # check box
        if shareFactionReputationBoo == False: # Read value
            self.shareFactionExpulsion.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.shareFactionReputation.stateChanged.connect(self.shareFactionReputationChecked) # call shareFactionReputationChecked method

        self.shareTopics = self.findChild(QtWidgets.QCheckBox, 'shareTopics') # Find the checkbox
        if shareTopicsBoo == True: # Read value
            self.shareTopics.setCheckState(Qt.CheckState.Checked) # check box
        if shareTopicsBoo == False: # Read value
            self.shareTopics.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.shareTopics.stateChanged.connect(self.shareTopicsChecked) # call shareTopicsChecked method

        self.shareBounty = self.findChild(QtWidgets.QCheckBox, 'shareBounty') # Find the checkbox
        if shareBountyBoo == True: # Read value
            self.shareBounty.setCheckState(Qt.CheckState.Checked) # check box
        if shareBountyBoo == False: # Read value
            self.shareBounty.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.shareBounty.stateChanged.connect(self.shareBountyChecked) # call shareBountyChecked method

        self.shareReputation = self.findChild(QtWidgets.QCheckBox, 'shareReputation') # Find the checkbox
        if shareReputationBoo == True: # Read value
            self.shareReputation.setCheckState(Qt.CheckState.Checked) # check box
        if shareReputationBoo == False: # Read value
            self.shareReputation.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.shareReputation.stateChanged.connect(self.shareReputationChecked) # call shareReputationChecked method

        self.shareMapExploration = self.findChild(QtWidgets.QCheckBox, 'shareMapExploration') # Find the checkbox
        if shareMapExplorationBoo == True: # Read value
            self.shareMapExploration.setCheckState(Qt.CheckState.Checked) # check box
        if shareMapExplorationBoo == False: # Read value
            self.shareMapExploration.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.shareMapExploration.stateChanged.connect(self.shareMapExplorationChecked) # call shareMapExplorationChecked method

        self.shareVideos = self.findChild(QtWidgets.QCheckBox, 'shareVideos') # Find the checkbox
        if shareVideosBoo == True: # Read value
            self.shareVideos.setCheckState(Qt.CheckState.Checked) # check box
        if shareVideosBoo == False: # Read value
            self.shareVideos.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.shareVideos.stateChanged.connect(self.shareVideosChecked) # call shareVideosChecked method

        self.respawnAtImperialShrine = self.findChild(QtWidgets.QCheckBox, 'respawnAtImperialShrine') # Find the checkbox
        if respawnAtImperialShrineBoo == True: # Read value
            self.respawnAtImperialShrine.setCheckState(Qt.CheckState.Checked) # check box
        if respawnAtImperialShrineBoo == False: # Read value
            self.respawnAtImperialShrine.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.respawnAtImperialShrine.stateChanged.connect(self.respawnAtImperialShrineChecked) # call respawnAtImperialShrineChecked method

        self.respawnAtTribunalTemple = self.findChild(QtWidgets.QCheckBox, 'respawnAtTribunalTemple') # Find the checkbox
        if respawnAtTribunalTempleBoo == True: # Read value
            self.respawnAtTribunalTemple.setCheckState(Qt.CheckState.Checked) # check box
        if respawnAtTribunalTempleBoo == False: # Read value
            self.respawnAtTribunalTemple.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.respawnAtTribunalTemple.stateChanged.connect(self.respawnAtTribunalTempleChecked) # call respawnAtTribunalTempleChecked method

        self.playersRespawn = self.findChild(QtWidgets.QCheckBox, 'playersRespawn') # Find the checkbox
        if playersRespawnBoo == True: # Read value
            self.playersRespawn.setCheckState(Qt.CheckState.Checked) # check box
        if playersRespawnBoo == False: # Read value
            self.playersRespawn.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.playersRespawn.stateChanged.connect(self.playersRespawnChecked) # call playersRespawnChecked method

        self.bountyResetOnDeath = self.findChild(QtWidgets.QCheckBox, 'bountyResetOnDeath') # Find the checkbox
        if bountyResetOnDeathBoo == True: # Read value
            self.bountyResetOnDeath.setCheckState(Qt.CheckState.Checked) # check box
        if bountyResetOnDeathBoo == False: # Read value
            self.bountyResetOnDeath.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.bountyResetOnDeath.stateChanged.connect(self.bountyResetOnDeathChecked) # call bountyResetOnDeathChecked method

        self.bountyDeathPenalty = self.findChild(QtWidgets.QCheckBox, 'bountyDeathPenalty') # Find the checkbox
        if bountyDeathPenaltyBoo == True: # Read value
            self.bountyDeathPenalty.setCheckState(Qt.CheckState.Checked) # check box
        if bountyDeathPenaltyBoo == False: # Read value
            self.bountyDeathPenalty.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.bountyDeathPenalty.stateChanged.connect(self.bountyDeathPenaltyChecked) # call bountyDeathPenaltyChecked method

        self.allowSuicideCommand = self.findChild(QtWidgets.QCheckBox, 'allowSuicideCommand') # Find the checkbox
        if allowSuicideCommandBoo == True: # Read value
            self.allowSuicideCommand.setCheckState(Qt.CheckState.Checked) # check box
        if allowSuicideCommandBoo == False: # Read value
            self.allowSuicideCommand.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.allowSuicideCommand.stateChanged.connect(self.allowSuicideCommandChecked) # call allowSuicideCommandChecked method

        self.allowFixmeCommand = self.findChild(QtWidgets.QCheckBox, 'allowFixmeCommand') # Find the checkbox
        if allowFixmeCommandBoo == True: # Read value
            self.allowFixmeCommand.setCheckState(Qt.CheckState.Checked) # check box
        if allowFixmeCommandBoo == False: # Read value
            self.allowFixmeCommand.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.allowFixmeCommand.stateChanged.connect(self.allowFixmeCommandChecked) # call allowFixmeCommandChecked method

        self.enablePlayerCollision = self.findChild(QtWidgets.QCheckBox, 'enablePlayerCollision') # Find the checkbox
        if enablePlayerCollisionBoo == True: # Read value
            self.enablePlayerCollision.setCheckState(Qt.CheckState.Checked) # check box
        if enablePlayerCollisionBoo == False: # Read value
            self.enablePlayerCollision.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.enablePlayerCollision.stateChanged.connect(self.enablePlayerCollisionChecked) # call enablePlayerCollisionChecked method

        self.enforceDataFiles = self.findChild(QtWidgets.QCheckBox, 'enforceDataFiles') # Find the checkbox
        if enforceDataFilesBoo == True: # Read value
            self.enforceDataFiles.setCheckState(Qt.CheckState.Checked) # check box
        if enforceDataFilesBoo == False: # Read value
            self.enforceDataFiles.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.enforceDataFiles.stateChanged.connect(self.enforceDataFilesChecked) # call enforceDataFilesChecked method

        self.enabled = self.findChild(QtWidgets.QCheckBox, 'MasterServerEnabled') # Find the checkbox
        if enabledBoo == True: # Read value
            self.MasterServerEnabled.setCheckState(Qt.CheckState.Checked) # check box
        if enabledBoo == False: # Read value
            self.MasterServerEnabled.setCheckState(Qt.CheckState.Unchecked) # uncheck box
        self.enabled.stateChanged.connect(self.enabledChecked) # call enforceDataFilesChecked method

        self.loginTime = self.findChild(QtWidgets.QTextBrowser, 'loginTimeoutView') # Find the text browser
        self.loginTimeoutView.setHtml(loginTime) # Show the content of variable in html form

        self.button = self.findChild(QtWidgets.QPushButton, 'changeLoginTimeout') # Find the button
        self.button.clicked.connect(self.changeLoginTimeoutPressed)  # Connect Button to Method

        self.difficulty = self.findChild(QtWidgets.QTextBrowser, 'difficultyView') # Find the text browser
        self.difficultyView.setHtml(difficulty) # Show the content of variable in html form

        self.button = self.findChild(QtWidgets.QPushButton, 'changeDifficultyLevel') # Find the button
        self.button.clicked.connect(self.changeDifficultyLevelPressed)  # Connect Button to Method

        self.deathTime = self.findChild(QtWidgets.QTextBrowser, 'deathTimeView') # Find the text browser
        self.deathTimeView.setHtml(deathTime) # Show the content of variable in html form

        self.button = self.findChild(QtWidgets.QPushButton, 'changeDeathTime') # Find the button
        self.button.clicked.connect(self.changeDeathTimePressed)  # Connect Button to Method

        self.deathPenaltyJailDays = self.findChild(QtWidgets.QTextBrowser, 'deathPenaltyView') # Find the text browser
        self.deathPenaltyView.setHtml(deathPenaltyJailDays) # Show the content of variable in html form

        self.button = self.findChild(QtWidgets.QPushButton, 'changeDeathPenalty') # Find the button
        self.button.clicked.connect(self.changedeathPenaltyJailDaysPressed)  # Connect Button to Method

        self.localaddr = self.findChild(QtWidgets.QTextBrowser, 'localAddressView') # Find the text browser
        self.localAddressView.setHtml(localaddr) # Show the content of variable in html form

        self.button = self.findChild(QtWidgets.QPushButton, 'changeLocalAddress') # Find the button
        self.button.clicked.connect(self.changeLocalAddressPressed)  # Connect Button to Method

        self.port = self.findChild(QtWidgets.QTextBrowser, 'portView') # Find the text browser
        self.portView.setHtml(port) # Show the content of variable in html form

        self.button = self.findChild(QtWidgets.QPushButton, 'changePort') # Find the button
        self.button.clicked.connect(self.changePortPressed)  # Connect Button to Method

        self.hostname = self.findChild(QtWidgets.QTextBrowser, 'hostnameView') # Find the text browser
        self.hostnameView.setHtml(hostname) # Show the content of variable in html form

        self.button = self.findChild(QtWidgets.QPushButton, 'changeHostname') # Find the button
        self.button.clicked.connect(self.changeHostnamePressed)  # Connect Button to Method

        self.maximumPlayers = self.findChild(QtWidgets.QTextBrowser, 'playersView') # Find the text browser
        self.playersView.setHtml(maximumPlayers) # Show the content of variable in html form

        self.button = self.findChild(QtWidgets.QPushButton, 'changePlayers') # Find the button
        self.button.clicked.connect(self.changePlayersPressed)  # Connect Button to Method

        self.password = self.findChild(QtWidgets.QTextBrowser, 'passwordView') # Find the text browser
        self.passwordView.setHtml(password) # Show the content of variable in html form

        self.button = self.findChild(QtWidgets.QPushButton, 'changePassword') # Find the button
        self.button.clicked.connect(self.changePasswordPressed)  # Connect Button to Method

        self.button = self.findChild(QtWidgets.QPushButton, 'startServer')  # Find the button
        self.button.clicked.connect(self.startServerPressed)  # Connect Button to Method

        self.button = self.findChild(QtWidgets.QPushButton, 'startClient')  # Find the button
        self.button.clicked.connect(self.startClientPressed)  # Connect Button to Method

        self.button = self.findChild(QtWidgets.QPushButton, 'startBrowser')  # Find the button
        self.button.clicked.connect(self.startBrowserPressed)  # Connect Button to Method

        self.show() # Show the GUI

    def passTimeWhenEmptyChecked(self, state):
        if self.passTimeWhenEmpty.isChecked():  # check if the float value is true then
            self.passTimeWhenEmptyTrue()  # invoke method passTimeWhenEmptyTrue
        else:  # else if the float value is false then
            self.passTimeWhenEmptyFalse()  # invoke method passTimeWhenEmptyFalse

    def passTimeWhenEmptyTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.passTimeWhenEmpty = false", "config.passTimeWhenEmpty = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def passTimeWhenEmptyFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.passTimeWhenEmpty = true", "config.passTimeWhenEmpty = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def allowConsoleChecked(self, state):
        if self.allowConsole.isChecked():  # check if the float value is true then
            self.allowConsoleTrue()  # invoke method allowConsoleTrue
        else:  # else if the float value is false then
            self.allowConsoleFalse()  # invoke method allowConsoleFalse

    def allowConsoleTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.allowConsole = false", "config.allowConsole = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def allowConsoleFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.allowConsole = true", "config.allowConsole = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def allowBedRestChecked(self, state):
        if self.allowBedRest.isChecked():  # check if the float value is true then
            self.allowBedRestTrue()  # invoke method allowBedRestTrue
        else:  # else if the float value is false then
            self.allowBedRestFalse()  # invoke method allowBedRestFalse

    def allowBedRestTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.allowBedRest = false", "config.allowBedRest = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def allowBedRestFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.allowBedRest = true", "config.allowBedRest = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def allowWildernessRestChecked(self, state):
        if self.allowWildernessRest.isChecked():  # check if the float value is true then
            self.allowWildernessRestTrue()  # invoke method allowWildernessRestTrue
        else:  # else if the float value is false then
            self.allowWildernessRestFalse()  # invoke method allowWildernessRestFalse

    def allowWildernessRestTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.allowWildernessRest = false", "config.allowWildernessRest = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def allowWildernessRestFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.allowWildernessRest = true", "config.allowWildernessRest = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def allowWaitChecked(self, state):
        if self.allowWait.isChecked():  # check if the float value is true then
            self.allowWaitTrue()  # invoke method allowWaitTrue
        else:  # else if the float value is false then
            self.allowWaitFalse()  # invoke method allowWaitFalse

    def allowWaitTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.allowWait = false", "config.allowWait = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def allowWaitFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.allowWait = true", "config.allowWait = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareJournalChecked(self, state):
        if self.shareJournal.isChecked():  # check if the float value is true then
            self.shareJournalTrue()  # invoke method shareJournalTrue
        else:  # else if the float value is false then
            self.shareJournalFalse()  # invoke method shareJournalFalse

    def shareJournalTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareJournal = false", "config.shareJournal = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareJournalFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareJournal = true", "config.shareJournal = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareFactionRanksChecked(self, state):
        if self.shareFactionRanks.isChecked():  # check if the float value is true then
            self.shareFactionRanksTrue()  # invoke method shareFactionRanksTrue
        else:  # else if the float value is false then
            self.shareFactionRanksFalse()  # invoke method shareFactionRanksFalse

    def shareFactionRanksTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareFactionRanks = false", "config.shareFactionRanks = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareFactionRanksFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareFactionRanks = true", "config.shareFactionRanks = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareFactionExpulsionChecked(self, state):
        if self.shareFactionExpulsion.isChecked():  # check if the float value is true then
            self.shareFactionExpulsionTrue()  # invoke method shareFactionExpulsionTrue
        else:  # else if the float value is false then
            self.shareFactionExpulsionFalse()  # invoke method shareFactionExpulsionFalse

    def shareFactionExpulsionTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareFactionExpulsion = false", "config.shareFactionExpulsion = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareFactionExpulsionFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareFactionExpulsion = true", "config.shareFactionExpulsion = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareFactionReputationChecked(self, state):
        if self.shareFactionReputation.isChecked():  # check if the float value is true then
            self.shareFactionReputationTrue()  # invoke method shareFactionReputationTrue
        else:  # else if the float value is false then
            self.shareFactionReputationFalse()  # invoke method shareFactionReputationFalse

    def shareFactionReputationTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareFactionReputation = false", "config.shareFactionReputation = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareFactionReputationFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareFactionReputation = true", "config.shareFactionReputation = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareTopicsChecked(self, state):
        if self.shareTopics.isChecked():  # check if the float value is true then
            self.shareTopicsTrue()  # invoke method shareTopicsTrue
        else:  # else if the float value is false then
            self.shareTopicsFalse()  # invoke method shareTopicsFalse

    def shareTopicsTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareTopics = false", "config.shareTopics = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareTopicsFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareTopics = true", "config.shareTopics = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareBountyChecked(self, state):
        if self.shareBounty.isChecked():  # check if the float value is true then
            self.shareBountyTrue()  # invoke method shareBountyTrue
        else:  # else if the float value is false then
            self.shareBountyFalse()  # invoke method shareBountyFalse

    def shareBountyTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareBounty = false", "config.shareBounty = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareBountyFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareBounty = true", "config.shareBounty = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareReputationChecked(self, state):
        if self.shareReputation.isChecked():  # check if the float value is true then
            self.shareReputationTrue()  # invoke method shareReputationTrue
        else:  # else if the float value is false then
            self.shareReputationFalse()  # invoke method shareReputationFalse

    def shareReputationTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareReputation = false", "config.shareReputation = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareReputationFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareReputation = true", "config.shareReputation = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareMapExplorationChecked(self, state):
        if self.shareMapExploration.isChecked():  # check if the float value is true then
            self.shareMapExplorationTrue()  # invoke method shareMapExplorationTrue
        else:  # else if the float value is false then
            self.shareMapExplorationFalse()  # invoke method shareMapExplorationFalse

    def shareMapExplorationTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareMapExploration = false", "config.shareMapExploration = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareMapExplorationFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareMapExploration = true", "config.shareMapExploration = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareVideosChecked(self, state):
        if self.shareVideos.isChecked():  # check if the float value is true then
            self.shareVideosTrue()  # invoke method shareVideosTrue
        else:  # else if the float value is false then
            self.shareVideosFalse()  # invoke method shareVideosFalse

    def shareVideosTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareVideos = false", "config.shareVideos = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def shareVideosFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.shareVideos = true", "config.shareVideos = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def respawnAtImperialShrineChecked(self, state):
        if self.respawnAtImperialShrine.isChecked():  # check if the float value is true then
            self.respawnAtImperialShrineTrue()  # invoke method respawnAtImperialShrineTrue
        else:  # else if the float value is false then
            self.respawnAtImperialShrineFalse()  # invoke method respawnAtImperialShrineFalse

    def respawnAtImperialShrineTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.respawnAtImperialShrine = false", "config.respawnAtImperialShrine = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def respawnAtImperialShrineFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.respawnAtImperialShrine = true", "config.respawnAtImperialShrine = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def respawnAtTribunalTempleChecked(self, state):
        if self.respawnAtTribunalTemple.isChecked():  # check if the float value is true then
            self.respawnAtTribunalTempleTrue()  # invoke method respawnAtTribunalTempleTrue
        else:  # else if the float value is false then
            self.respawnAtTribunalTempleFalse()  # invoke method respawnAtTribunalTempleFalse

    def respawnAtTribunalTempleTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.respawnAtTribunalTemple = false", "config.respawnAtTribunalTemple = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def respawnAtTribunalTempleFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.respawnAtTribunalTemple = true", "config.respawnAtTribunalTemple = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def playersRespawnChecked(self, state):
        if self.playersRespawn.isChecked():  # check if the float value is true then
            self.playersRespawnTrue()  # invoke method playersRespawnTrue
        else:  # else if the float value is false then
            self.playersRespawnFalse()  # invoke method playersRespawnFalse

    def playersRespawnTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.playersRespawn = false", "config.playersRespawn = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def playersRespawnFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.playersRespawn = true", "config.playersRespawn = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def bountyResetOnDeathChecked(self, state):
        if self.bountyResetOnDeath.isChecked():  # check if the float value is true then
            self.bountyResetOnDeathTrue()  # invoke method bountyResetOnDeathTrue
        else:  # else if the float value is false then
            self.bountyResetOnDeathFalse()  # invoke method bountyResetOnDeathFalse

    def bountyResetOnDeathTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.bountyResetOnDeath = false", "config.bountyResetOnDeath = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def bountyResetOnDeathFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.bountyResetOnDeath = true", "config.bountyResetOnDeath = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def bountyDeathPenaltyChecked(self, state):
        if self.bountyDeathPenalty.isChecked():  # check if the float value is true then
            self.bountyDeathPenaltyTrue()  # invoke method bountyDeathPenaltyTrue
        else:  # else if the float value is false then
            self.bountyDeathPenaltyFalse()  # invoke method bountyDeathPenaltyFalse

    def bountyDeathPenaltyTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.bountyDeathPenalty = false", "config.bountyDeathPenalty = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def bountyDeathPenaltyFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.bountyDeathPenalty = true", "config.bountyDeathPenalty = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def allowSuicideCommandChecked(self, state):
        if self.allowSuicideCommand.isChecked():  # check if the float value is true then
            self.allowSuicideCommandTrue()  # invoke method allowSuicideCommandTrue
        else:  # else if the float value is false then
            self.allowSuicideCommandFalse()  # invoke method allowSuicideCommandFalse

    def allowSuicideCommandTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.allowSuicideCommand = false", "config.allowSuicideCommand = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def allowSuicideCommandFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.allowSuicideCommand = true", "config.allowSuicideCommand = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def allowFixmeCommandChecked(self, state):
        if self.allowFixmeCommand.isChecked():  # check if the float value is true then
            self.allowFixmeCommandTrue()  # invoke method allowFixmeCommandTrue
        else:  # else if the float value is false then
            self.allowFixmeCommandFalse()  # invoke method allowFixmeCommandFalse

    def allowFixmeCommandTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.allowFixmeCommand = false", "config.allowFixmeCommand = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def allowFixmeCommandFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.allowFixmeCommand = true", "config.allowFixmeCommand = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def enablePlayerCollisionChecked(self, state):
        if self.enablePlayerCollision.isChecked():  # check if the float value is true then
            self.enablePlayerCollisionTrue()  # invoke method enablePlayerCollisionTrue
        else:  # else if the float value is false then
            self.enablePlayerCollisionFalse()  # invoke method enablePlayerCollisionFalse

    def enablePlayerCollisionTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.enablePlayerCollision = false", "config.enablePlayerCollision = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def enablePlayerCollisionFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.enablePlayerCollision = true", "config.enablePlayerCollision = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def enforceDataFilesChecked(self, state):
        if self.enforceDataFiles.isChecked():  # check if the float value is true then
            self.enforceDataFilesTrue()  # invoke method enforceDataFilesTrue
        else:  # else if the float value is false then
            self.enforceDataFilesFalse()  # invoke method enforceDataFilesFalse

    def enforceDataFilesTrue(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.enforceDataFiles = false", "config.enforceDataFiles = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def enforceDataFilesFalse(self):  # start of the function
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.enforceDataFiles = true", "config.enforceDataFiles = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def enabledChecked(self, state):
        if self.enabled.isChecked():  # check if the float value is true then
            self.enabledTrue()  # invoke method enabledTrue
        else:  # else if the float value is false then
            self.enabledFalse()  # invoke method enabledFalse

    def enabledTrue(self):  # start of the function
        serverfilefile = open(os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in serverfilefile:  # listing for function
            changes = line.replace("enabled = false", "enabled = true")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        serverfilefile.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def enabledFalse(self):  # start of the function
        serverfilefile = open(os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in serverfilefile:  # listing for function
            changes = line.replace("enabled = true", "enabled = false")  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        serverfilefile.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def changeLoginTimeoutPressed(self):
        timeout = askstring("Login timout", "Input desired login timout")  # get login timout from user through dialog
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.loginTime = " + loginTime, "config.loginTime = " + timeout)  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def changeDifficultyLevelPressed(self):
        level = askstring("Difficulty level", "Input desired Difficulty level")  # get difficulty level from user through dialog
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.difficulty = " + difficulty, "config.difficulty = " + level)  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def changeDeathTimePressed(self):
        dtime = askstring("Death time", "Input desired death time")  # get the death time from user through dialog
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.deathTime = " + deathTime, "config.deathTime = " + dtime)  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def changedeathPenaltyJailDaysPressed(self):
        dptime = askstring("Death penalty jail days", "Input desired death penalty jail days")  # get the death penalty jail days from user through dialog
        file = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("config.deathPenaltyJailDays = " + deathTime, "config.deathPenaltyJailDays = " + dptime)  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'config.lua'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def changeLocalAddressPressed(self):
        newlocaladdress = askstring("Server local address", "Input desired server local address")  # get the server hostname from user through dialog
        with open(os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg'), 'r') as serverfile:  # open config
            data = serverfile.readlines()  # read config
        data[localaddrline] = "localAddress = " + newlocaladdress + "\n" # edit port
        with open(os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg'), 'w') as serverfile:
            serverfile.writelines(data)
        return  # use line numbers stored in variable to overwrite port with input from user

    def changePortPressed(self):
        newport = askstring("Server port", "Input desired server port")  # get the server port from user through dialog
        with open(os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg'), 'r') as serverfile:  # open config
            data = serverfile.readlines()  # read config
        data[portline] = "port = " + newport + "\n" # edit port
        with open(os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg'), 'w') as serverfile:
            serverfile.writelines(data)
        return  # use line numbers stored in variable to overwrite port with input from user

    def changeHostnamePressed(self):
        newhostname = askstring("Server hostname", "Input desired server hostname")  # get the server hostname from user through dialog
        serverfile = open(os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in serverfile:  # listing for function
            changes = line.replace("hostname = " + hostname, "hostname = " + newhostname)  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        serverfile.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def changePlayersPressed(self):
        newplayers = askstring("Maximum players", "Input desired amount of maximum players")  # get the amount of maximum players from user through dialog
        serverfile = open(os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in serverfile:  # listing for function
            changes = line.replace("maximumPlayers = " + maximumPlayers, "maximumPlayers = " + newplayers)  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        serverfile.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg'),
                    "w")  # open  config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def changePasswordPressed(self):
        newpassword = askstring("Server password", "Input desired server password")  # get the server password from user through dialog
        serverfile = open(os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg'),
                    'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in serverfile:  # listing for function
            changes = line.replace("password = " + password, "password = " + newpassword)  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        serverfile.close()  # close opened config file
        fout = open(os.path.join(temporarydirectory, './' + 'tes3mp-server-default.cfg'),
                    "w")  # open config file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened config file

    def startServerPressed(self):
        p = subprocess.run(os.path.join(temporarydirectory, './' + 'startServer.bat'))
        return  # execute startServer.bat file

    def startClientPressed(self):
        p = subprocess.run(os.path.join(temporarydirectory, './' + 'startClient.bat'))
        return  # execute startClient.bat file

    def startBrowserPressed(self):
        p = subprocess.run(os.path.join(temporarydirectory, './' + 'startBrowser.bat'))
        return  # execute startBrowser.bat file

    file.close()  # close file with configuration

app = QtWidgets.QApplication(sys.argv) # defines widget as app
window = Ui() # defines window
app.exec() # loops app
p = subprocess.run(os.path.join(temporarydirectory, './' + 'alterend.bat')) # removes all files in case of a crash/exit
p = subprocess.run(os.path.join(currentdirectory, './' + 'alterend2.bat')) # removes all files in case of a crash/exit