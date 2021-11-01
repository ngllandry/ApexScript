# ApexScript
personal script for Apex Legends stats and r/apexlegends posts

1) Obtain reddit api from https://www.reddit.com/prefs/apps
2) Obtain ApexLegends api from https://apexlegendsapi.com/documentation.php

3) Must create a "config.py" file with the following format:

    clientID = "REDDIT API CLIENT ID"
    
    secretToken = "REDDIT API SECRET"
    
    grantType = "LOGIN METHOD"
    
    username = "REDDIT USERNAME"
    
    password = "REDDIT PASSWORD"
    
    apexstatuskey = "ApexLegendsStatus API Key"
    
    headers = {'User-Agent': 'MyBot/0.0.1'}
