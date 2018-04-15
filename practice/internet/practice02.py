i = int(input("Please input profit: "))
if i <= 100000:
    stake = i * 0.1
elif i <= 200000:
    stake = 100000 * 0.1 + (i - 100000) * 0.075
elif i <= 400000:
    stake = 10000 + 7500 + (i - 200000) * 0.05
elif i <= 600000:
    stake = 10000 + 7500 + 10000 + (i - 400000) * 0.03
elif i <= 1000000:
    stake = 10000 + 7500 + 10000 + 6000 + (i - 600000) * 0.015
else:
    stake = 10000 + 7500 + 10000 + 6000 + 6000 + (i - 1000000) * 0.01
print(stake)

