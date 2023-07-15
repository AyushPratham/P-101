import random;

def diceRoll(response):
    dice = random.randint(1,6)
    if(dice == 1):
        print("[---]")
        print("[-+-]")
        print("[---]")
    elif(dice == 2):
        print("[-+-]")
        print("[---]")
        print("[-+-]")
    elif(dice == 3):
        print("[-+-]")
        print("[-+-]")
        print("[-+-]")
    elif(dice == 4):
        print("[+-+]")
        print("[---]")
        print("[+-+]")
    elif(dice == 5):
        print("[+-+]")
        print("[-+-]")
        print("[+-+]")
    elif(dice == 6):
        print("[+-+]")
        print("[+-+]")
        print("[+-+]")
        
response =  input("Do you want to roll the dice(Y or N): ")

if(response == "Y"):
    diceRoll(response)
    

