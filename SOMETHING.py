'''
#length check
while True:
    nricNum = input("Enter your NRIC number. \n")
    
    if len(nricNum) == 9:
        nricLetters = nricNum[:1] + nricNum [8:]
        nricNumbers = nricNum[1:8]
        if nricLetters.isalpha() == True:
            if nricNumbers.isdigit() == True:
                print("Accepted")
                break
            else:
                print("Rejected")
                continue
        else: 
            print("Rejected")
            continue
        
    else:
        print("Rejected")
        continue



while True:
    entry = input("Enter a 2 character entry: \n")
    
    if len(entry) == 2:
        entryPosition0 = entry[0]
        entryPosition1 = entry[1]
        
        if entryPosition0.isalpha() == True:
            print("Check 1 passed")
            if entryPosition0.isdigit() == True:
                print("Check 2 passed")
                print("accepted")
                break
            elif entryPosition1.isdigit() == True:
                print("Check 2 passed")
                print("accepted")
                break
            
            else:
                print("Check 2 Failed")
                print("rejected")
                continue
            
        elif entryPosition1.isalpha() == True:
            print("Check 1 passed")
            if entryPosition0.isdigit() == True:
                print("Check 2 passed")
                print("accepted")
                break
            elif entryPosition1.isdigit() == True:
                print("Check 2 passed")
                print("accepted")
                break
            
            else:
                print("Check 2 Failed")
                print("rejected")
                continue
        else:
            print("Check 1 Failed")
            print("rejected")
            continue
        
    else:
        print("rejected")
        continue
        


import random as r

number = r.randint(20,51)
done = False
counter = 5
print(f"You have {counter} tries.")
while counter > 0:

    guess = input("Guess a number between 20 and 50: \n")
    if guess.isdigit() == True:
        guess = int(guess)
    
        if guess == number:
            print("Correct!")
            done = True
            break
        
        elif guess > number:
            print("Lower")
            counter -= 1
            print(f"You have {counter} tries left!")
            continue
        
        elif guess < number:
            print("Higher")
            counter -= 1
            print(f"You have {counter} tries left!")
            continue
        
    else:
        print("Input numbers only!! ")
        continue
    
if done == False:
    print("Loser!!!")
    
else:
    print("Congratulations!!")
    
'''
    
