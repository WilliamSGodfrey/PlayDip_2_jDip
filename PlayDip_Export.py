# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 09:49:26 2014

@author: 0r2754
"""
#import sys
import requests
import getpass
#import os.path
# from urllib import urlopen
from bs4 import BeautifulSoup

def Main():
    
    
    username = raw_input('Enter your playdiplomacy.com name: ')
    password = raw_input('Enter your playdiplomacy.com password: ')
    #password = getpass.getpass('Enter your playdiplomacy.com password: ')
    
    GameID = raw_input('Game ID: ')
    CurrentTurn = False
    
    
    folderpath = 'D:\\0r2754\wsg\Dip'
    
    #GameID = 84190
    #lURL = "http://www.playdiplomacy.com/game_history.php?game_id=" + str(GameID) + "&gdate=1&phase=B"
    
    #URL = 'http://www.playdiplomacy.com/game_history.php?game_id=84190&gdate=1&phase=B'
    

    
    # Start a session so we can have persistant cookies
    session = requests.session()
    
    # This is the form data that the page sends when logging in
    payload = {
        'page_act' :  '',
        'username': username,
        'password': password
    }
    
    # This logs in to the website
    session.post('http://www.playdiplomacy.com/login.php', data=payload)

    Turn = -1
    filepath = folderpath + '\\' + str(GameID) + '.txt'
    with open(filepath,'a') as outf:
        outf.write('GAME' + str(GameID)
        
        while CurrentTurn != True:
            Turn = Turn + 1
            if Turn % 2 == 0:
                phase = ['O', 'R']
            else:
                phase = ['O', 'R', 'B']
        
            for idx, value in enumerate(phase):
                outf.write(str(1901 + Turn))
                request = session.get('http://www.playdiplomacy.com/game_history.php?game_id=' + str(GameID) + '&gdate=' + str(Turn) + '&phase=' + value)
                rawhtml = BeautifulSoup(request.text)
                rawhtml = rawhtml.find_all('td', class_='maphistory')
                rawhtml = str(rawhtml[0])
                rawhtml = rawhtml.replace('<b>','').replace('</b>','').replace('<br/>','\n').replace('-&','\n')
                rawhtml = rawhtml.replace('to hold','H')
                
                rawlist = rawhtml.splitlines()[1:-1]   
              
                for idx, value in enumerate(rawlist):
                    if 'FRANCE' in value or 'ENGLAND' in value or 'RUSSIA' in value or 'TURKEY' in value or 'ITALY' in value or 'AUSTRIA' in value or 'GERMANy' in value or 'gt;' in value:
                        next
                    else:
                        outf.write(value + '\n')
                        
            if Turn == 3:
                    CurrentTurn == True
Main()
