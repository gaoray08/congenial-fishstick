'''
flag = True
numlist = []

while flag:
    number = input("Enter a number: \n")
    if (number == "q") or (number == "Q"):
        print(f"The number entered is {number}, which doesn't fufill the requirement. Thus, it will not run anymore.")
        flag = False
        
    elif number == "":
        continue
    
    elif number == "Damn":
        print("daniel")
        print("tutututututu")
        
    else:
        print("The number has been appended into the list.")
        numlist.append(number)
        print(numlist)
        
        
print(numlist)


apple = input("Please enter a 4d number: \n"
if apple.isdigit():
    print("Yes, all made of digits")
else:
    print("No, not all made of digits")
              
'''

orange = input("Enter a name: \n")
if orange.isalpha():
    print("Yes, all are letters")
else:
    print("No, not all are letters")

    
               
