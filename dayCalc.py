#constants

from calendar import month


days_in_year = 365
days_in_month = 30
days_in_week = 7

#ask for age and convert to days since it's the smallest unit of time measurement
total = int(input("how many days: "))
total_constant = total

#calc years and days left over
years = total // days_in_year
total = total - (years * days_in_year)

#calc months and days left over
months = total // days_in_month
total = total - (months * days_in_month)

#calc weeks and days left over
weeks = total // days_in_week
total = total - (weeks * days_in_week)

#Print Final
print(f"{total_constant} is {years} years, {months} months, {weeks} weeks and {total} days")

#check if true
p = total_constant
q = (years * days_in_year) + (months * days_in_month) + (weeks * days_in_week) + total
print(f"if {p} is the sames as {q} this is accurate")
print(p==q)


#Tests
# print(f"age left over is (total) {total} days")
# print(f"years is {years} with {total} days left over")
# print(f"months is {months} with {total} days left over")
# print(f"weeks is {weeks} with {total} days left over")
