profit = int(input("Total profit of the year: "))
bonus = float()
thresholds = [1000000, 1000000, 2000000, 2000000, 4000000]
rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
for i in range(len(thresholds)):

    if profit <= thresholds[i]:
        bonus += profit * rates[i]
        print(f"We should keep ${bonus} to out staff for this outlet.")
        exit()

    bonus += thresholds[i] * rates[i]
    profit -= thresholds[i]
bonus += profit * rates[5]
print(f"We should keep ${bonus} to out staff for this outlet.")
