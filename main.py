import sys
from random import randint
from kahootBot import BotInstance

total_bots = []

def game():
    while True:
        for i in range(len(total_bots)):
            t = total_bots[i].choose(randint(0,3))
            if t == "stop":
                return


        
        
# player input of the code for joining the server
def main():
    gamecode = input("gamecode: ")
    amountofBots = None
    try:
        amountofBots = int(input("how many bots do you want to join the game? "))
    except:
        print("wrong format")
        return


    if amountofBots<=0 or amountofBots>10:
        print("incorrect value specified")
        return

    if amountofBots == 1:
        name = input("name? ")
        if name == "":
            name = BotInstance.name_chooser()
        total_bots.append(BotInstance(gamecode,name))

    else:

        
        special_name = ""
        customnamescase = str(input("custom names? ")).lower()
        if customnamescase == "yes" or customnamescase == "y":
            customnamescase = True
            special_name = input("name:")
        else:
            customnamescase = False


        for _ in range(amountofBots):
            if not customnamescase:
                total_bots.append(BotInstance(gamecode))
            else:
                total_bots.append(BotInstance(gamecode,BotInstance.special_names(special_name)))

    game()
    
    from time import sleep

    sleep(5)
    for i in total_bots:
        i.stop()
if __name__ != "__main__":
    print("can't run file as imported package")

main()