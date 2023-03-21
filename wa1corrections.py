wordlist = []

for i in range(3): 
    word = input("Enter the word: \n")
    counter = 0
    for letter in word:
        if letter in "aeiouAEIOU":
            counter += 1
            
    if counter >= 2:
        word = "Big " + word
        wordlist.append(word)
    else:
        word = "Small " +word
        wordlist.append(word)
        
print(wordlist)
        
        
