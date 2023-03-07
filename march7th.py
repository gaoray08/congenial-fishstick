'''
mr lee's example
'''
myList = [] #declaring blank list
i = 0       #declaring a counter

while len(myList) < 4:
  myList.append(i)
  i += 1    #if number of items in myList is lesser than 4, increase counter

print(myList)

'''
sumlist = list(range(10,30))
use a while loop to total all the elements and print out 
will not be credited if sum() is used
'''
sumlist = list(range(10, 30))
i = 0
sum = 0

while i < len(sumlist):
  sum += sumlist[i]
  i += 1

print(sum)

'''
Create a program using while loop where a person enters 10 numbers. The number will only be collected in the list if it is a odd number and divisible by 3
'''
numlist = []
counter = 0

while counter < 11:
  number = int(input("Enter a number \n"))
  if number % 2 == 1 and number % 3 == 0:
    numlist.append(number)

  counter += 1

print(numlist)
