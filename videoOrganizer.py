#! python3

# Organize videos folder.

import shutil, os, re

tvShows = ['The Americans', 'Luke Cage', 'Family Guy', 'Ballers', 'Anthony Bourdain', 'Westworld', 'American Dad', 'Archer', 'Better Call Saul', 'Black Sails', 'The Expanse', 'Family Guy', 'Halt and Catch Fire', 'House of Cards', "It's Always Sunny in Philadelphia", 'Maron', 'Mr Robot', 'Narcos', 'Shameless', 'Sherlock', 'Silicon Valley', 'The Strain', 'True Detective', 'Workaholics'
           'The.Americans','Luke.Cage', 'Family.Guy', 'Ballers', 'Anthony.Bourdain', 'Westworld', 'American.Dad', 'Archer', 'Better.Call.Saul', 'Black.Sails', 'The.Expanse', 'Family.Guy', 'Halt.and.Catch.Fire', 'House.of.Cards', "It's.Always.Sunny.in.Philadelphia", 'Maron', 'Mr.Robot', 'Narcos', 'Shameless', 'Sherlock', 'Silicon.Valley', 'The.Strain', 'True.Detective', 'Workaholics']

tvShowFolders = ['The Americans', 'Luke Cage', 'Family Guy', 'Ballers', 'Anthony Bourdain', 'Westworld', 'American Dad', 'Archer', 'Better Call Saul', 'Black Sails', 'The Expanse', 'Family Guy', 'Halt and Catch Fire', 'House of Cards', "It's Always Sunny in Philadelphia", 'Maron', 'Mr Robot', 'Narcos', 'Shameless', 'Sherlock', 'Silicon Valley', 'The Strain', 'True Detective', 'Workaholics']

os.chdir('G:\\ftp\\Videos\\')

for show in os.listdir():
    if any(tvShow in show for tvShow in tvShows):
        print('Moving the show... ' + show)
        nameRegex = re.compile(r'^(\D+)\.{1,10}')
        if nameRegex.search(show) is not None:
            showName = nameRegex.search(show)
            #print(showName.group())
            nameSub = re.compile(r'\.{1,10}')
            newName = nameSub.sub(' ', showName.group())
            #print(newName)
            nameSub1 = re.compile(r'(\s)$')
            newName2 = nameSub1.sub('', newName)
            if newName2 in tvShowFolders:
                shutil.move(show, 'G:\\ftp\\Videos\\tv\\' + newName2)
            else:
                print("Can't move " + show + " because the folder '" + newName2 + "' does not exist")
        else:
            nameRegex = re.compile(r'^(\D+)\s{1,10}')
            showName = nameRegex.search(show)
            #print(showName.group())
            #nameSub = re.compile(r'\.{1,10}')
            #newName = nameSub.sub(' ', showName.group())
            #print(newName)
            nameSub1 = re.compile(r'(\s)$')
            newName2 = nameSub1.sub('', showName.group())
            if newName2 in tvShowFolders:
                shutil.move(show, 'G:\\ftp\\Videos\\tv\\' + newName2)
            else:
                print("Can't move " + show + " because the folder '" + newName2 + "' does not exist")
    else:
        pass
