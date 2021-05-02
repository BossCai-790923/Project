profit = int(input("Total profit of the year: "))
x=profit
bonus = 0.0
thresholds = [1000000, 1000000, 2000000, 2000000, 4000000]
rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
for z in range(1):

    for i in range(len(thresholds)):

        if profit <= thresholds[i]:
            bonus += profit * rates[i]
            break
        if profit>thresholds[i]:
            bonus += thresholds[i] * rates[i]
            profit -= thresholds[i]
        # if profit>thresholds[4]:
        #     x=profit-thresholds[4]
        #     bonus += x * 0.01
        if x>10000000:
            bonus=(x-10000000)*rates[5]+395000
            break



else:
    print(f"We should keep ${bonus} to out staff for this outlet.")
    exit()
