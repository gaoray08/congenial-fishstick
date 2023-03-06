'''
Get someone to enter the 5 clutches of
eggs, one at each time, the eggs will
be added onto a total. You need to arrange baskets to contain the eggs. Each basket can only contain  10 eggs. How
many baskets do I need?
'''

totaleggs = 0
baskets = 0

for i in range(5):
    eggs = input("Enter the number of eggs: \n")
    totaleggs = totaleggs + int(eggs)

baskets = totaleggs / 10

if totaleggs%10 != 0:
    baskets += 1

print("The number of eggs is {}, and the number of baskets needed is {}".format(totaleggs, int(baskets)))




'''
Generate a number list through the range function with a and b keyed in as arguments. Print out all the numbers, one at a time, except for those
that satisfy the following criteria:  i)
greater than 10 ii) odd number iii) divisible by 3 or 7.
'''

numlist = []

for i in range(2):
    number = input("Enter the number: \n")
    if int(number) < 10:
        print(f'{number} is lesser than 10')
        if int(number) % 2 != 0:
            print(f'{number} is an odd number')
            if int(number) % 3 != 0:
                print(f'The number {number} is not divisible by 3')
                if int(number) % 7 != 0:    
                    print(f'The number {number} is also not divisible by 7')
                    numlist.append(number)
                    print(f'{number} has been appended into numlist.')
                else:
                    print("But the number is divisible by 7")
            else:
                print("The number is divisible by 3")
                
for numbers in numlist:
    print(numbers)
    


'''
Create a program that will requests someone
to enter a sentence, the program will print out all letters and miss out the
vowels.
'''

sentence = input("Enter a sentence:")

for i in sentence:
    if i in "aeiouAEIOU":
        pass
    elif i == " ":
        pass
    else:
        print(i)
        
