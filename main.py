import random
import string

play = True
tries = 0
maxTries = 12

X = 0  #right color, right place
Y = 0  #right color, wrong place

colors = ['R','G','B','Y','P','W']
code = random.sample(colors,4)
code_test = code.copy()
print(code)


while (play):
    while(tries < maxTries):
        comb = []
                #to try and guess 5 colors, just add a fifth
        first_l = input("Write your first letter :  ")
        comb.append(first_l)
                     
        second_l = input("Write your second letter :  ")
        comb.append(second_l)
                     
        third_l = input("Write your third letter :  ")
        comb.append(third_l)
                     
        fourth_l = input("Write your fourth letter :  ")
        comb.append(fourth_l)
        
        print(comb)
        for i in range(len(code_test)):
            if comb[i] == code_test[i]:
                X +=1
        for i in range(len(code_test)):
            for g in range(len(comb)):
                if comb[g] == code_test[i] and g!=i:
                    code_test[i] = 0
                    Y +=1
        tries += 1
        triesLeft = maxTries - tries
        print(str(triesLeft) + " tries left")
        print ("X = " + str(X))
        print ("Y = " + str(Y))
        X = 0 
        Y = 0 
    play = False
