# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#combine names and make them lower case
combined_names = name1 + name2
lower_names =combined_names.lower()

#find and add TRUE
t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')
score_true = t + r + u + e

#find love
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
score_love = l + o + v + e

score = int(str(score_true) + str(score_love))

print(f"{score}")