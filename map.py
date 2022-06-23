#Don't change the code below 
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#Don't change the code above 

#Write your code below this row 
#split number
first_num = int(str(position[0]))
second_num = int(str(position[1]))

#update map
map[second_num-1].pop(first_num-1)
map[second_num-1].insert(first_num-1, "X")


#  Don't change the code below 
print(f"{row1}\n{row2}\n{row3}")