'''
Input 5 words and print:
Word with highest no. vowel + vowel count
Word with 2+ vowels
Total no. vowels
'''

wordlist = []
vowels = "aeiou"
numofvowels = []

for i in range(5):
  currentWord = input("Enter your word \n")
  wordlist.append(currentWord)
  
for word in wordlist:
  word = word.lower() # standardize input types
  print(f'\nword -> {word}')
  count = 0
  for vowel in vowels:
    print(f'current vowel -> {vowel}')
    if vowel in word:
      print(f'current vowel {vowel} is in {word}')
      count = count + 1
    else:
      print(f'current vowel {vowel} is not in {word}')
  numofvowels.append(count)
  

for number in numofvowels:
    if number >= 2:
        position = numofvowels.index(number)
print("The word with the highest number of vowels is", wordlist[position], "and the number of vowels it has is ", number)
print("The word with 2 or more vowels is", wordlist[position])
print("The total number of vowels as a whole is ", sum(numofvowels))
    

      
     
      
