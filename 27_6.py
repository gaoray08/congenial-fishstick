
evenlist = []
oddlist = []

for i in range(5):
    number = int(input("What is your number? \n"))
    if number % 2 == 0:
        evenlist.append(number)
        
    else:
        oddlist.append(number)
    
print(evenlist)
print(oddlist)


numListA = []
numListB = []
total = 0

for i in range(3):
    numA = int(input("Person A, enter your number \n"))
    numListA.append(numA)

for i in range(2):
    numB = int(input("Person B, enter your number \n"))
    numListB.append(numB)

for i in numListA:
    for j in numListB:
        number = i * j
        print(number)
        total = total + number


print(f'The total number is: {total}')


numListA = []
numListB = []
hongming = []
thana = []

for i in range(3):
    numA = input("Person A, enter a noun \n")
    numListA.append(numA)

for i in range(2):
    numB = input("Person B, enter a adjective \n")
    numListB.append(numB)

for i in numListA:
    for j in numListB:
        combinedWord = j + " " + i
        if len(combinedWord) > 14:
            hongming.append(combinedWord)
        else:
            thana.append(combinedWord)


print(hongming)
print(thana)


momo = []

while True:
    words = input("Enter words: \n")
    if words.isalpha() == True:
        momo.append(words)
    elif words == str(-1):
        print("Breaking...")
        print(momo)
        break 
    else:
        print("Number detected..")
        continue
        
