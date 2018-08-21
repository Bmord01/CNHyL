import json
import os

def createTeam(sID,inName):
    tDict={"Name":inName,
           "Id":sID,    
           "Wins":0,
           "Losses":0,
           "Ties":0,
           "Otwins":0,
           "Otlosses":0,
           "Shootout":0}
    team.append(tDict)
    return

#Code 1
def editTeam(teamIn):
    print("Select Team Number from List:")
    for item in teamList:
        print(item,":" ,teamList[item])
        
    print()
    tID=int(input("Enter Team number (0 to exit team edit): ").strip())
    tID-=1
    if tID < 0:
        return
    for item in teamIn[tID]:
        print (item,":",teamIn[tID][item])

    print()
    for item in teamIn[tID]:
        print ("<" + item + ">", end=" ")
    print()
    
    editID=input("Enter Field to Edit: ").title().strip()
    
    while(editID == 'Id' or editID=='Name'):
        print("Cannot change this")
        editID=input("Enter Field to Edit: ").title().strip()

    if editID in teamIn[tID]:
        editChange=int(input("Enter new value: "))
        teamIn[tID][editID]=editChange
    else:
        return
    #print()
    for item in teamIn[tID]:
        print (item,":",teamIn[tID][item])
    return

#Code 2
def createPlayer():
    teamID=int(input("Enter team number for player: "))
    if teamID == 0:
        return
    
    FName = input("Enter player First Name: ")
    if len(FName) == 0:
        return
    
    LName = input("Enter player Last Name: ")
    if len(LName) == 0:
        return
    
    Number = int(input("Enter player Jersey Number: "))
    if Number < 1:
        return
    
    pID=teamID
    pDict={"Team_id":pID,
           "Number":Number,
           "Fname":Fname,
           "Lname":LName,
           "Goals":0,
           "Assists":0,
           "Penalties":0,
           "Pminutes":0}
    player.append(pDict)
    return

#Code 3
def editPlayer(playerIn):
    if(len(playerIn) == 0):
        print()
        print("No Players to Edit")
        return
    print("Select Player Number: ")
    for item in playerIn:
        print(item["Fname"],item["Lname"] ,":",item["Number"])
        
    edit=int(input("Enter Number: "))
    for item in playerIn:
        if item["Number"]==edit:
            for index in item:
                if index != "Pminutes":
                    print(index , ":" , item[index])
                else:
                    print(index, ":", '{}:00'.format(item['Pminutes']))
                    
            editField = input("Enter edit field: ").strip().title()
            editValue = int(input("Enter new value: ").strip())
            item[editField]=editValue
    return
#Code 4
def createGame(teamIn):
    print("Enter information - 0 will exit function")
    tID = int(input("Enter Team 1 Number: "))
    if tID == 0:
        return
    
    t1Score=int(input("Enter Team 1 Score: "))
    if t1Score == 0:
        return
    
    otID= int(input("Enter Team 2 Number: "))
    if otID == 0:
        return

    t2Score=int(input("Enter Team 2 Score: "))
    if t2Score == 0:
        return
    
    isOT = input("Is Overtime? (y = yes, n = no): ")
    isSO = input("Is Shootout? (y = yes, n = no): ")
    if isOT.lower()== 'y':
        bOT=True
    else:
        bOT=False
    if isSO.lower() =='y':
        bSO=True
    else:
        bSO=False
                
    sDict={"Team":tID,
           "OTeam":otID,
           "Score":t1Score,
           "OScore":t2Score}
    schedule.append(sDict)
    sDict={"Team":otID,
           "OTeam":tID,
           "Score":t2Score,
           "OScore":t1Score}
    
    schedule.append(sDict)
    
    if t1Score>t2Score:
        for item in teamIn:
            if bOT & bSO:
                if item['Id']==tID:
                    item['Otwins']+=1
                    item['Shootout']+=1
                if item['Id']==otID:
                    item['Otlosses']+=1
                    item['Shootout']+=1
            elif bOT:
                if item['Id']==tID:
                    item['Otwins']+=1
                if item['Id']==otID:
                    item['Otlosses']+=1
            else:
                if item['Id']==tID:
                    item['Wins']+=1
                if item['Id']==otID:
                    item['Losses']+=1
    else:   
        for item in teamIn:
            if bOT & bSO:
                if item['Id']==tID:
                    item['Otlosses']+=1
                    item['Shootout']+=1
                if item['Id']==otID:
                    item['Otwins']+=1
                    item['Shootout']+=1
            elif bOT:
                if item['Id']==tID:
                    item['Otlosses']+=1
                if item['Id']==otID:
                    item['Otwins']+=1
            else:
                if item['Id']==tID:
                    item['Losses']+=1
                if item['Id']==otID:
                    item['Wins']+=1
    return
#Code 5
def PrintTeams(inTeam):
    teamNumber = int(input("Select Team number to Print (0 = all Teams): "))
    print()
    if teamNumber == 0:
        for item in inTeam:
            for field in item:
                print(field + " = " + str(item[field]))
            print()
    else:
        for field in inTeam[teamNumber]:
            print(field + " = " + str(inTeam[teamNumber-1][field]))
    return
#Code 6
def PrintPlayers(playerIn):
    playerNumber = int(input("Select Players Team Number to Print (0 = all Players): "))
    print()
    if playerNumber == 0:
        for item in playerIn:
            for field in item:
                if field == "Team_id":
                    print("Team = " + teamList[item[field]])
                print(field + " = " + str(item[field]))
            print()
    else:
        for item in playerIn:
            if item["Team_id"] == playerNumber:
                for field in item:
                    if field == "Team_id":
                        print("Team = " + teamList[item[field]])
                    print(field + " = " + str(item[field]))
            print()     
    return

#Code 7
def PrintSchedule():
    teamSchedule = int(input("Enter Team To Print Schedule (0 for all shedule): "))
    print()
    if teamSchedule == 0:
        for item in schedule:
            if teamList[item["Score"]] > teamList[item["OScore"]]:
                print(teamList[item["Team"]] + " Wins vs " + teamList[item["OTeam"]])
            else:
                print(teamList[item["Team"]] + " Loses vs " + teamList[item["OTeam"]])
    else:
        for item in schedule:
            if item["Team"] == teamSchedule:
                if teamList[item["Score"]] > teamList[item["OScore"]]:
                    print(teamList[item["Team"]] + " Wins vs " + teamList[item["OTeam"]])
                else:
                    print(teamList[item["Team"]] + " Loses vs " + teamList[item["OTeam"]])
    return

    


#####################################################
def printTeams(team):
    for item in team:
        print(item)
    return

def printTeam(TID,team):
    for item in team:
        if item['Id'] == TID:
            print (item)
    return

def printPlayers(player):
    for item in player:
        print(item)
    return

def printPlayer(Lname,player):
    for item in player:
        if item["Lname"] == Lname:
            print(item)
    return

def main(sID,team,player,schedule):
    try:
        with open('JSON/team.json') as teamIn:
            team = json.load(teamIn)
    except:
        if len(team)==0:
            for item in teamList:
                sID=sID+1
                createTeam(sID,teamList[sID])
        with open('JSON/team.json', 'w') as outTeam:
            json.dump(team,outTeam)
        with open('JSON/team.json') as teamIn:
            team = json.load(teamIn)
            
    try:
        with open('JSON/player.json') as playerIn:
            player = json.load(playerIn)
    except:
        with open('JSON/player.json','w') as outPlayer:
            json.dump(player,outPlayer)
        with open('JSON/player.json') as playerIn:
            player = json.load(playerIn)

    try:
        with open("JSON/schedule.json") as scheduleIn:
            schedule = json.load(scheduleIn)
    except:
        with open('JSON/schedule.json', 'w') as outSchedule:
            json.dump(schedule,outSchedule)
        with open("JSON/schedule.json") as scheduleIn:
            schedule = json.load(scheduleIn)
    
    print("Welcome to CNHyL!")
    print()
    print("Enter option code")
    print("Exit Program                 = 0")
    print("Edit Team                    = 1")
    print("Create Player                = 2")
    print("Edit Player                  = 3")
    print("Create Game                  = 4")
    print("Print Teams                  = 5")
    print("Print Players                = 6")
    print("Print Past Schedule          = 7")
    print()
    choice=int(input("Enter Choice: "))
    while choice > 7:
        choice=int(input("Enter Choice: "))
    while choice !=0:
        if choice ==1:
            editTeam(team)
        elif choice ==2:
            createPlayer()
            
        elif choice ==3:
            editPlayer()
            
        elif choice ==4:
            createGame(team)
            
        elif choice ==5:
            PrintTeams(team)
            
        elif choice ==6:
            PrintPlayers(player)

        elif choice ==7:
            PrintSchedule()
        
        print()
        print("Enter option code")
        print("Exit Program                 = 0")
        print("Edit Team                    = 1")
        print("Create Player                = 2")
        print("Edit Player                  = 3")
        print("Create Game                  = 4")
        print("Print Teams                  = 5")
        print("Print Players                = 6")
        print("Print Past Schedule          = 7")
        print()
        with open('JSON/team.json', 'w') as outTeam:
            json.dump(team,outTeam)
        with open('JSON/player.json','w') as outPlayer:
            json.dump(player,outPlayer)
        with open('JSON/schedule.json', 'w') as outSchedule:
            json.dump(schedule,outSchedule)
        choice = int(input("Enter Choice: "))
        print()
    #createPlayer(1,"Bill","Test",42)
    #editTeam()
    #editPlayer()
    #createGame(1,2,2,3,False,False)
    return 0
#teamStruct     == [{ID,Name,Wins,Losses,Ties,OTWins,OTLosses,Shootouts}]
team=[]
#playerStruct   == [{TeamID,Number,First,Last,Goals,Assists,Penalties,PMin}]
player=[]
#ScheduleStruct == [{TID,OTID,Score,OScore}]
schedule=[]
x = 0;
#createGame(1,2,2,3,False,False)
teamList={
        1:"Anaheim Ducks",
        2:"Boston Bruins",
        3:"Buffalo Sabres",
        4:"Calgary Flames",
        5:"Carolina Hurricanes",
        6:"Chicago Blackhawks",
        7:"Colorado Avalanche",
        8:"Columbus Blue Jackets",
        9:"Dallas Stars",
        10:"Detroit Red Wings",
        11:"Edmonton Oilers",
        12:"Florida Panthers",
        13:"Los Angeles Kings",
        14:"Minnesota Wild",
        15:"Montreal Canadiens",
        16:"Nashville Predators",
        17:"New Jersey Devils",
        18:"New York Islanders",
        19:"New York Rangers",
        20:"Ottawa Senators",
        21:"Philadelphia Flyers",
        22:"Phoenix Coyotes",
        23:"Pittsburgh Penguins",
        24:"Saint Louis Blues",
        25:"San Jose Sharks",
        26:"Tampa Bay Lighting",
        27:"Toronto Maple Leafs",
        28:"Vancouver Canucks",
        29:"Vegas Golden Knights",
        30:"Washington Capitals",
        31:"Winnipeg Jets"
    }

sID=0;
main(sID,team,player,schedule)
