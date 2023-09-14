import random
import string


def main():
    play = True
    tries = 0
    maxTries = 12 #Max tries 
    
    X = 0  #right color, right place
    Y = 0  #right color, wrong place
    
    colors = ['R','G','B','Y','P','W']
        
    file = open(".score.txt", "r")  #Oppening file and getting the score in score variable
    data = file.readlines()
    score = int(data[0].strip("\n"))
    file.close()
                
    file = open(".parties.txt", "r")    #Oppening file and getting the numbers of parties in nb variable
    data = file.readlines()
    nb = int(data[0].strip("\n")) 
    file.close()  
    
    """4 is the number of color we have to guess, to change this number,
    you also have to add an Fith in the while, or del the fourth"""
    code = random.sample(colors,4)
    
    
    print(code)
    print("Colors are Red : R, Green : G, Blue : B, Yellow : Y, Purple : P and White : W.\n")
    
    while play:
        tries = 0
        print("Your score is " + str(score))
        print("You have played  " + str(nb) + " times")
        while(tries < maxTries):
            code_test = code.copy()#copying the code to be able to change it without killing the real one later
            comb = []
                    #to try and guess 5 colors, just add a fifth
            first_l = input("Write your first letter :  ")
            comb.append(first_l)  #Adding the first letter guessed by the player in the list
                         
            second_l = input("Write your second letter :  ")
            comb.append(second_l)   #Adding the second letter guessed by the player in the list
                         
            third_l = input("Write your third letter :  ")
            comb.append(third_l)    #Adding the third letter guessed by the player in the list
                         
            fourth_l = input("Write your fourth letter :  ")
            comb.append(fourth_l)   #Adding the fourth letter guessed by the player in the list
            comb_test = comb.copy() #copying the combination to be able to change it without killing the real one later
            
            print(comb)
            for i in range(len(code_test)):
                if comb_test[i] == code_test[i]: 
                    X +=1
            for i in range(len(code_test)):
                for g in range(len(comb_test)):
                    if comb_test[g] == code_test[i] and g!=i:
                        comb_test[g] = 1          #changing the letters to 1 already compared to avoid duplicates in Y
                        code_test[i] = 0          #changing the letters to 0 already compared to avoid duplicates in Y
                        Y +=1
            tries += 1
            triesLeft = maxTries - tries
            print(str(triesLeft) + " tries left")
            print ("X = " + str(X))
            print ("Y = " + str(Y))
            X = 0 
            Y = 0
        if tries == maxTries:

            score += tries #Adding the number of tries to the score

                
            file = open(".score.txt", "w") #Adding the score in the file
            file.write(str(score))
            file.close
                

            nb += 1 #Adding one the number of parties played

                
            file = open(".parties.txt", "w") #Adding the number of parties in the file
            file.write(str(nb))
            file.close
            
        print("Your score is " + str(score))
        print("You have played  " + str(nb) + " times")
        answer = input("Do you want to play again, rest stats or quit ? 1/2/3\n")
            
        if(answer == "1"):  
            tries = 0           #Playing again
        elif(answer == "2"):
            score = 0                     #Reset scores and parties
            nb = 0
            file = open(".score.txt", "w") #Reseting the score in the file
            file.write(str(0))
            print("Score has been reset")
            file.close()
            
            file = open(".parties.txt", "w")    #Reseting the number of parties in the file
            file.write(str(0))
            print("Parties has been reset")
            file.close()
        elif(answer == "3"):
            play = False        #Stopping the game
main()
