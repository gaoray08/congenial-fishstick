
'''
Invite someone to enter a string in this format:
i. the middle letter needs to be @ e.g ab@57 
ii. the length must be 5
iii. the first 2 characters must be letters
iv. last two characters must be numbers
v. the last digit must not be a mulitple of 3. 

If validation fails, the program will reprompt the person to re-enter with "Please re-enter again!"

3 of such strings, once validated will be collected into a special list. 

The program will additionally process each string n this list  by multiplying the 2 digits at the back with 2. 
and all letters will be uppercased.

e.g cd@57------> CD@114
 
Output in this format:
Word ouput is [ AF@34, CK@100, JY@58] 
'''

stringList = []
count = 0

while True:
    if count == 3:
        break
    
    string = input("Enter a string: \n")
    middleLetter = string[len(string) // 2]
    
    if middleLetter != "@":
        print("Your middle letter needs to be @")
        print("Please re-enter again!")
        continue
    
    if len(string) != 5:
        print("The length of your string needs to be 5!")
        print("Please re-enter again!")
        continue
    
    if string[:2].isalpha() == False:
        print("Your first 2 characters must be letters")
        print("Please re-enter again!")
        continue
    
    if string[-2:].isdigit() == False:
        print("Your last 2 characters must be integers!")
        print("Please re-enter again!")
        continue
    
    if int(string[-1]) == 0:
        continue
    
    elif int(string[-1]) % 3 == 0: 
        print("Your last character must not be a multiple of 3!")
        print("Please re-enter again!")
        continue
    
    else:
        stringNumbers = string[-2:]
        doubled = int(stringNumbers) * 2
        string = string[:3] + str(doubled)
        stringList.append(string)
        count += 1
        continue
    
print(stringList)
    
