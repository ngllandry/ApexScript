import requests
import json
import authFile as authFile
import config as cfg
import apexStatusFunctions as asf
import redditFunctions as rf


# Press the green button in the gutter to run the script.
if __name__ == '__main__':



    while True:
        menu = int(input("1 = Apex Reddit Stuff\n"
                     "2 = Player Stats Lookup\n"
                     "3 = YEET\n"
                     "Select 1, 2, or 3: "))
        if menu == 1: #REDDIT
            while True:
                options = int(input("1 = HAWT\n"
                                    "2 = New Posts\n"
                                    "3 = blah blah posts\n"
                                    "4 = LEAVE\n"
                                    "Select a number: "))
                if options == 1:
                    rf.get_hot_posts()
                elif options == 2:
                    rf.get_new_posts()
                #elif options == 3:
                elif options == 4:
                    break

        elif menu == 2: #PLAYER
            while True:
                options = int(input("1 = User information\n"
                                    "2 = Match history\n"
                                    "3 = GO BACK AHHHH\n"
                                    "Select 1, 2, or 3: "))
                if options == 1:
                    name = input("Enter player name: ")
                    asf.get_player_info(name)
                elif options == 2:
                    name = input("Enter player name: ")
                    asf.get_match_history(name)
                elif options == 3:
                    break
        elif menu == 3:
            break




    #res1 = requests.get(apexStatusKey)

    #parsed = json.loads(res1.json())
    #formatted = json.dumps(res1.json(), indent=2)
    #print(formatted)

    #print(res1.json())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
