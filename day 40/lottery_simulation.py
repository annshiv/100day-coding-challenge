import random
import matplotlib.pyplot as plt
account = 0
x = []
y = []
for i in range(7):
    x.append(i)
    bet = random.randint(1,10)
    luck = random.randint(1,10)
    # print("Bet : ",bet)
    # print("Lucky Draw : ",luck)
    if luck == bet:
        account += 800
    else:
        account -= 100
    y.append(account)
plt.plot(x,y)
plt.show()
print("Money in your game account : ",account)