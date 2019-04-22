import kahootBot
import sys

LookupTable = {
    "r":0,
    "b":1,
    "y":2,
    "g":3
}
def main():
    print("\n\n\npress \"0\" to end the game \n\n\n")
    gamecode = input("gamecode: ")

    while True:
        amountofBots = int(input("Bots: "))
        
        if amountofBots < 1 or amountofBots > 20:
            print("number not accepted")
            continue
        else:
            break
    

    special_name = ""
    while True:
        names = str(input("names? (y/n)"))
        if names.lower() != "y" and names.lower() != "n":
            print("incorrect input")
            continue
        else:
            if names.lower() == "y":
                names = True
                special_name = input("special name: ")
            else:
                names = False
            break
    
    totalBots = []
    for _ in range(amountofBots):
        if names:
            totalBots.append(kahootBot.BotInstance(gamecode,kahootBot.BotInstance.special_names(special_name)))
        else:
            totalBots.append(kahootBot.BotInstance(gamecode))
    
    while True:
        answer = ""
        while True:
            answer = str(input("\nanswer?"))
            if answer.lower() not in ('r','b','y','g') and answer != "0":
                continue
            else:
                if answer == "0":
                    print("\ngame ended")
                    for i in range(len(totalBots)):
                        totalBots[i].stop()
                    sys.exit(0)
                else:
                    break
        
        for i in range(len(totalBots)):
            totalBots[i].choose(LookupTable[answer.lower()])
        
        


if __name__ == "__main__":
    main()
