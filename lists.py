#James Hooper
#Top 25 Games
game1 = "Minecraft"
game2 = "Scrap Mechanic"
game3 = "Terra Tech"
game4 = "Terraria"
game5 = "Avorion"
game6 = "Among Us"
game7 = "SSB Ultament"
game8 = "Unrailed"
game9 = "All the Mario Karts"
game10 = "Forts"
game11 = "Crash Of Cars"
game12 = "Drive A Head"
game13 = "Risk"
game14 = "Human Fall Flat"
game15 = "BTD 6"
game16 = "Ledend Of Zelda Breath Of The Wild"
game17 = "Lego Star wars full trilogy"
game18 = "Lego Lord Of the Rings"
game19 = "Wii Tanks"
game20 = "Star Control 2"
game21 = "Super Mario Galaxy (1&2)"
game22 = "Portal(1&2)"
game23 = "Mine Sweeper"
game24 = "Plants vs. Zombies (1)"
game25 = "BTD battles"

topGames = [game1,
            game2,
            game3,
            game4,
            game5,
            game6,
            game7,
            game8,
            game9,
            game10,
            game11,
            game12,
            game13,
            game14,
            game15,
            game16,
            game17,
            game18,
            game19,
            game20,
            game21,
            game22,
            game23,
            game24,
            game25] #length of list -1

if "Minecraft" in topGames:
    print("pass")
else:
    print("Fail")
if topGames[0] != "Minecraft":
    print(fail)
else:
    print("Pass")
for i in topGames:
    if ("Pokemon" in i) or ("Halo" in i):
        print("Fail")
    else:
        print("Pass")
    
##topGames.append("new Game")
##classList = ("Bob","Tim","Frank","Eric") #tupple cannot be changed Lists are made with [] not ()

##print(topGames[0],topGames[1],topGames[2],topGames[3],topGames[4])
##print(topGames[0:5])
##highScores = [500,1000,1500,2000,2500,3000,3500,4000]

##print(len(highScores))
##
##print(highScores[len(highScores) - 1])
##print(max(highScores))
##print(min(highScores))
##highScores.append(200)
##topScore = highscores.pop(0)
##print(highScores)
##highScores.clear()

##print(topGames.index("Star Control 2"))
