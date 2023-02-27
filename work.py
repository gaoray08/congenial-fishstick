'''
Input 5 words and print:
Word with highest no. vowel + vowel count
Word with 2+ vowels
Total no. vowels
'''

wordlist = []
vowels = "aeiou"

for i in range(2):
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
      count += 1

    else:
      