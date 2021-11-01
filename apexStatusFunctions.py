import requests
import json
import authFile as authFile
import config as cfg

#API documentation:
#https://apexlegendsapi.com/documentation.php

def get_uid(username):
    apexStatusKey = "https://api.mozambiquehe.re/bridge?version=5&platform=PC&player=" + username + "&auth=" + cfg.apexstatuskey
    res = requests.get(apexStatusKey)
    playerDict = res.json()
    x = playerDict.get("global")
    y = str(x.get("uid"))
    return y

def get_player_info(username):
    apexStatusKey = "https://api.mozambiquehe.re/bridge?version=5&platform=PC&player=" + username + "&auth=" + cfg.apexstatuskey
    res = requests.get(apexStatusKey)
    playerDict = res.json()
    x = playerDict.get("global")
    formatted = json.dumps(x, indent=2)
    print(formatted)

def get_match_history(username): #must whitelist key before use
    uid = get_uid(username)
    apexStatusKey = "https://api.mozambiquehe.re/games?auth=" + cfg.apexstatuskey + "&uid=" + uid
    res =  requests.get(apexStatusKey)
    matchDict = res.json()
    formatted = json.dumps(matchDict, indent=2)
    print(formatted)