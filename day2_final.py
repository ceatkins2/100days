#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
#contanstants
print("Welcome to the tip calculator")
bill_total = float(input("What was the total bill: "))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

#calcs
tip_in_percent = float(tip_percentage / 100 )
total_tip = round((tip_in_percent * bill_total),2)
tip_per_person = round((total_tip / num_people), 2)
total_per_person = round((bill_total / num_people) + tip_per_person, 2)

#output
print(f"Each person should pay {total_per_person}")

#Test
# print(f"There are {num_people} splitting a {bill_total} bill at {tip_percentage} tip")
# print(f"A {tip_percentage} percent tip is {tip_in_percent}")
# print(f"total tip is {total_tip}")
# print(f"tip amount per person is {tip_per_person}")
# print(f"total per person is {total_per_person}")