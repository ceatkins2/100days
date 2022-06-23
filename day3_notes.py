# num = int(input("What is the number: "))
# if num % 2 == 0:
#     print("You got an even number fam")
# else:
#     print("odd")

print("welcome to the rollercoaster")
height = int(input("What is your heigh in cm ? "))
bill =  0

if height >=120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? "))
    if age <12:
        print("Admission is $5")
        bill = 5
    elif age<=18 :
        print("Admission is $7")
        bill = 7
    elif age >=45 and age <=55:
        print("Admission is free")
        bill = 0
    else:
        print("Admission is $12")
        bill = 12

    wants_photo =input("Do you want a Photo taken? Y or N. ")
    if wants_photo =="Y":
        #Add $3 to bill
        bill +=3
        print(f"Your total is {bill}")
    else:
        print(f"your total is {bill}")

else:
    print("scram short stuff")