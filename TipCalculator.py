print("Welcome to the tip calculator")
total_bill = input("Whats was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15 ? ")
people_per = input("How many people to split the bill? ")

tip_perA = int(tip) / 100 * float(total_bill) 
final_tip = tip_perA + float(total_bill)



result = float(final_tip) / int(people_per)


print(f"Each person should pay: ", round(result, 2))

