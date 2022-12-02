judgeSeen = int(input())
previousTime = 0
ananasPoints = 0
borovnicaPoints = 0 
playerAold = 0

for i in range(0, judgeSeen):
    sectionInfo = str(input())
    offenceTime = sectionInfo.split(" ")[0]
    playerA = sectionInfo.split(" ")[1]
    playerB = sectionInfo.split(" ")[2]
    
    # Player from team A got player from team B
    if int(playerA) < 4 and int(playerB) > 4:
        if int(offenceTime) - int(previousTime) <= 10 and int(playerA) == int(playerAold):
            ananasPoints += 50
        ananasPoints += 100

    if int(playerA) > 4 and int(playerB) < 4:
        if int(offenceTime) - int(previousTime) <= 10 and int(playerA) == int(playerAold):
            borovnicaPoints += 50
        borovnicaPoints += 100

    previousTime = int(offenceTime)
    playerAold = int(playerA) 
print(ananasPoints, borovnicaPoints)