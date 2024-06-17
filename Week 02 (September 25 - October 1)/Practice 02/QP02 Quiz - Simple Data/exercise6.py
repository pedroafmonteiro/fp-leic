principalamount = int(input("Principal Amount: "))
interestrate = float(input("Interest Rate: "))
frequency = int(input("Frequency (per year): "))

formula = principalamount*(1 + (interestrate / frequency)) ** (frequency * 2)

print(round(formula,3))