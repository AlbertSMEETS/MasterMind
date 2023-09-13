import random
import string

play = True

X = 0  #right color, right place
Y = 0  #right color, wrong place

colors = ['R','G','B','Y','P','W']
code = random.sample(colors,4)
print(code)

tries = []
        #to try and guess 5 colors, just add a fifth.
first_l = input("Write your first letter :  ")
tries.append(first_l)
             
second_l = input("Write your second letter :  ")
tries.append(second_l)
             
third_l = input("Write your third letter :  ")
tries.append(third_l)
             
fourth_l = input("Write your fourth letter :  ")
tries.append(fourth_l)

print(tries)

while (play):
    for i in range(len(code)):
        if tries[i] == code[i]:
            X +=1
    for i in range(len(code)):
        for g in range(len(tries)):
            if tries[g] == code[i] and g!=i:
                Y +=1
    play = False

print (X,Y)
