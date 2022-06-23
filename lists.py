import random

fruits = ["apple", "banana", "kiwi", "grape"]
# for i in range(0, len(fruits)):
#     print(f"{fruits[i]}")

#change an item
fruits[-1] = "gr4p3"

## add an item
fruits.append("orange")
print(fruits)
##pop out orange
last_fruit = fruits.pop()
print(f"im gonna remove {last_fruit}")
print(fruits)