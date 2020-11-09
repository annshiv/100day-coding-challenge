import random
account = 0
for _ in range(7):
    bet = random.randint(1,10)
    luck = random.randint(1,10)
    print("Bet : ",bet)
    print("Lucky Draw : ",luck)
    if luck == bet:
        account += 800
    else:
        account -= 100
    print("Money in your game account : ",account)