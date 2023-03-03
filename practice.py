
print("Beautiful program that counts vowels and consonants.")
vowels = 0
consonants = 0

for letter in range(10):
    a = input("Enter a letter:")
    if a in "aeiouAEIOU":
        vowels += 1
        
    else:
        consonants += 1
        
        
print("The number of vowels is {} and the number of consonants is {}".format(vowels, consonants))

#qn 1b
'''
Create a program that asks for a sentence, and tell me whether the consonants added up is two times more than the sum of vowels. If yes, print "Mimi", else print "Andrea"
'''
vowels = []
consonants = 0

for i in range(10):
    letters = input("Enter the letters:")
    if letters in "aeiouAEIOU":
        vowels.append(letters)
    
    else:
        consonants += 1
        
print("The vowels are {}".format(vowels, consonants))

'''
Create a program that asks for a sentence, and tell me whether the consonants added up is two times more than the sum of vowels. If yes, print "Mimi", else print "Andrea"
'''

vowels = 0
consonants = 0
vowellist = []
consonantslist = []
sentence = input("Enter the sentence: \n")

for letters in sentence:
    if letters in "aeiouAEIOU":
        vowels += 1
        vowellist.append(letters)
    elif letters == " ":
        pass
    else:
        consonants += 1
        consonantslist.append(letters)
        
if vowels * 2 == consonants:
    print("Mimi")
    
else:
    print("Andrea")
