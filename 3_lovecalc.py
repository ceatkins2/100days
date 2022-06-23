# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Convert strings to lower case
name1_lower = name1.lower()
name2_lower =name2.lower()

#init scores
score_true = 0
score_love = 0


#find "true"

if "t" in name1_lower or name2_lower:
    score_true += name1_lower.count('t') + name2_lower.count('t')
if "r" in name1_lower or name2_lower:
    score_true += name1_lower.count('r') + name2_lower.count('r')
if "u" in name1_lower or name2_lower:
    score_true += name1_lower.count('u') + name2_lower.count('u')
if "e" in name1_lower or name2_lower:
    score_true += name1_lower.count('e') + name2_lower.count('e')

#find "love"
if "l" in name1_lower or name2_lower:
    score_love += name1_lower.count('l') + name2_lower.count('l')
if "o" in name1_lower or name2_lower:
    score_love += name1_lower.count('o') + name2_lower.count('o')
if "v" in name1_lower or name2_lower:
    score_love += name1_lower.count('v') + name2_lower.count('v')
if "e" in name1_lower or name2_lower:
    score_love += name1_lower.count('e') + name2_lower.count('e')

#Get results and concat as STR then convert to INT
str_total_score = str(score_true) + str(score_love)
int_total_score = int(str_total_score)

#Display Test results
if int_total_score <10 or int_total_score > 90:
    print(f"Your score is {int_total_score}, you go together like coke and mentos")
elif int_total_score > 40 and int_total_score < 50:
    print(f"You score is {int_total_score}, you are alright togehter")
else:
    print(f"Your score is {int_total_score}")


### Tests
# print(f"TRUE :: {score_true} LOVE :: {score_love}")
# #print(f"{total_score}")
# print(type(str_total_score))
# print(type(int_total_score))
