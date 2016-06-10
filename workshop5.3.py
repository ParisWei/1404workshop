import random
time = float(input("How many quick picks?"))
while time >= 1:
    n = random.sample(range(0,45),6)
    time = time - 1
    print(sorted(n))
