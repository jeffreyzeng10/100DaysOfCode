print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
split = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

pay = "{:.2f}".format((total*(1+tip/100))/split,2)

print("Each person should pay: $"+str(pay))
