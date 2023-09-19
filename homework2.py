'''
q1
listnum = []
for i in range(2):
    word = input("Enter a word: \n")
    if len(word)  == 4:
        listnum.append(word)

q2

numlist2 = []
count = 0

while True:
    if count == 5:
        break
    else:
        word = input("enter your words: \n")
        if word[:3].isdigit() == True:
            if word[4:].isalpha() == True:
                if word[3] == "@":
                    if int(word[:3]) % 3 == 0:
                        word = str(int(word[:3])/ 3) + word[4:]
                        numlist2.append(word)
                        count += 1
                    elif int(word[:3] % 2 == 0:
                        numlist2.append(word)
                        count += 1
                    else:
                        print("Try again")
                        continue
                else:
                    print("Try again")
                    continue
            else:
                print("Try again")
                continue
        else:
            print("Try again")
            continue
            
q3

List = []
count = 0
while True:
    if count != 5:
        num = int(input("Enter a number: \n"))
        if num % 3 == 0 and num % 5 == 0:
            List.append(num)
            count += 1
        else:
            print("entry rejected,Try again. ")
            continue
        
    elif len(List) == 3:
        break
    else:
        break
    
q4

string = ""
count = 0

while True:
    if count != 5:
        letter = input("Enter a letter: \n")
        if letter.isalpha() == True:
            string += letter
            print(string)
            count ++
        else:
            print("Your letter must be alpha not digit. ")
            continue
        
    else:
        break

q5


List = []
index = 0

while True:
    sentence = input("Enter a sentence: \n")
    for i in sentence:
        List.append(i[index])
        index ++

q6

specialBox = []
count = 0

while count != 1:
    word = input("Enter a 2 letter word")
    if word[0].isalpha() == True:    
        if word[0] in "ABCDEFGabcdefg":
            if word[1].isdigit() == True:
                if word[1] in "56789":
                    specialBox.append(word)
                    count ++
                else:
                    print("Second digit must be between 5,6,7,8,9, inclusive.")
                    print("Try again.")
                    continue
            else:
                print("second digit must be a digit.")
                print("Try again.")
                continue
        else:
            print("First word must be between A to G")
            print("Try again.")
            continue
    else:
        print("First word must be alpha.")
        print("Try again.")
        continue

q7

import random as r

d1 = str(r.randint(0,9))
d2 = str(r.randint(0,9))
w1 = r.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ")
w2 = r.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ")

randomPassword = d1 + d2 + w1 + w2

print(randomPassword)


q8 


import random as r
randomNum = r.randint(10,39)
count = 0

while True:
    if count == 6:
        print("You lost!")
        break
    guess = int(input("Guess the random number: \n"))
    if guess < randomNum:
        print("Number is greater than your guess")
        count += 1 
        continue
    if guess > randomNum:
        print("Number is smaller than your guess")
        count += 1
        continue
    if guess == randomNum:
        print("Correct! Congratulations")
        print(f"Number of tries taken: {count}")
        break

q9

vowels = "aeiouAEIOU"
index = 0
word = input("Enter a word: \n")
while True:
    if index == len(word):
        break
    for i in word:
        index += 1
        if i in vowels:
            print(f"The vowel {i} is in your word index {index}.")

q10

lists = []
index = 0

while len(lists) != 5:
    word = input("Enter a word \n")
    if word == "qqq":
        break
    
    elif index > 0:
        if len(word) > len(lists[index - 1]): 
            lists.append(word)
            index += 1
        else:
            print("Entry rejected")
            continue
    
    elif index == 0:
        lists.append(word)
        index += 1
        
print(lists)

'''
