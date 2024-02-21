index = 0

while index != 5:
    print("Enter five numbers seperated by spacings. ")
    nums = input()
    splitted = nums.split(" ")
    totalSum = 0
    if len(splitted) == 5:
        if splitted[index].isdigit():
            if int(splitted[index]) < 10 or int(splitted[index]) > 99:
                print(i.index(), "number is invalid. Re-enter all your numbers.")
            else:
                totalSum += int(splitted[index])
                index += 1
        else:
            print(i.index(), "input is invalid. Re-enter all your numbers")
            continue
                
    else:
        print("Total number of input is not 5. Re-enter only five numbers.")
        continue
    
if totalSum % 10 == 0:
    print("Valid List.", totalSum)
else:
    print("Invalid List.", totalSum)index = 0

while index != 5:
    print("Enter five numbers seperated by spacings. ")
    nums = input()
    splitted = nums.split(" ")
    totalSum = 0
    if len(splitted) == 5:
        if splitted[index].isdigit():
            if int(splitted[index]) < 10 or int(splitted[index]) > 99:
                print(i.index(), "number is invalid. Re-enter all your numbers.")
            else:
                totalSum += int(splitted[index])
                index += 1
        else:
            print(i.index(), "input is invalid. Re-enter all your numbers")
            continue
                
    else:
        print("Total number of input is not 5. Re-enter only five numbers.")
        continue
    
if totalSum % 10 == 0:
    print("Valid List.", totalSum)
else:
    print("Invalid List.", totalSum)
