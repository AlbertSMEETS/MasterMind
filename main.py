import random
import string

play = True
tries = 0
maxTries = 12 #Max tries 

X = 0  #right color, right place
Y = 0  #right color, wrong place

colors = ['R','G','B','Y','P','W']

 """4 is the number of color we have to guess, to change this number,
you also have to add an Fith in the while, or del the fourth"""
code = random.sample(colors,4)

print(code)
print("Colors are Red : R, Green : G, Blue : B, Yellow : Y, Purple : P and White : W.\n")

while (play):
    while(tries < maxTries):
        code_test = code.copy()  #copying the code to be able to change it without killing the real one later
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
                code_test[i] = 0             #changing the letters to 0 already compared to avoid duplicates in Y
        for i in range(len(code_test)):
            for g in range(len(comb)):
                if comb[g] == code_test[i] and g!=i:
                    code_test[i] = 0          #changing the letters to 0 already compared to avoid duplicates in Y
                    Y +=1
        tries += 1
        triesLeft = maxTries - tries
        print(str(triesLeft) + " tries left")
        print ("X = " + str(X))
        print ("Y = " + str(Y))
        X = 0 
        Y = 0 
    play = False
