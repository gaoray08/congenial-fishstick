'''
listnum = []
for i in range(2):
    word = input("Enter a word: \n")
    if len(word)  == 4:
        listnum.append(word)
       

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


List = []
index = 0

while True:
    sentence = input("Enter a sentence: \n")
    for i in sentence:
        List.append(i[index])
        index ++
'''
