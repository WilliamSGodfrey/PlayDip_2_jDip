# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 09:49:26 2014

@author: 0r2754
"""
import sys
import requests
from urllib import urlopen
from bs4 import BeautifulSoup


def Main():
    
    folderpath = 'D:\0r2754\wsg\Dip'
    
    #GameID = 84190
    #lURL = "http://www.playdiplomacy.com/game_history.php?game_id=" + str(GameID) + "&gdate=1&phase=B"
    
    #URL = 'http://www.playdiplomacy.com/game_history.php?game_id=84190&gdate=1&phase=B'
        
    # Start a session so we can have persistant cookies
    session = requests.session()

    # This is the form data that the page sends when logging in
    payload = {
        'page_act' :  '',
        'username': 'WilliamSGodfrey',
        'password': 'wsg1983X'
    }
    
    # This logs in to the website
    session.post('http://www.playdiplomacy.com/login.php', data=payload)

    request = session.get('http://www.playdiplomacy.com/game_history.php?game_id=84190&gdate=1&phase=O')
    rawsoup = BeautifulSoup(request.text)
    rawsoup = rawsoup.find_all('td', class_='maphistory')
    rawsoup = str(rawsoup[0])
    rawsoup = rawsoup.replace('<b>','').replace('</b>','').replace('<br/>','\n').replace('-&','\n')
    rawsoup = rawsoup.replace('to hold','H')
    
    rawlist = rawsoup.splitlines()[1:-1]

    filepath = folderpath + '    
    
    with open(filepath,'w') as outf:
        for idx, value in enumerate(rawlist):
            if 'FRANCE' in value or 'ENGLAND' in value or 'RUSSIA' in value or 'TURKEY' in value or 'ITALY' in value or 'AUSTRIA' in value or 'GERMANy' in value or 'gt;' in value:
                next
            else:
                print value
                outf.write(value + '\n')

Main()
