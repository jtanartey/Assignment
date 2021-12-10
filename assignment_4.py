
#the function is to make starting the game easy
#it starts from the living room then moves to the dining room then the kitcen and ends there
def living_room():
    living_room = ["couches", "TV","centre table","game consoles"]
    print (living_room)

    ques_3 = int(input("How many steps do you want take?\n"))
    if ques_3 < 5:
        dining_room = ["dining table","chairs","books","fruits"]
        print (dining_room)
        ques_4 = int(input("How many steps do you want take?\n"))

        if ques_4 < 5:
            kitchen = ["microwave","stove","fridge","food","food processor"]
            print (kitchen)
            print ("Can't go further")          
            
        else:
            print ("You hit a wall!!")
    else:
        print ("You hit a wall")

print ("Welcom!!!")
start = input(print("Do you want to enter the house?(y/n)\n"))
if start == "y" or "Y":
    living_room()
else:
    print("Game Ended")
