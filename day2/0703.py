import random
num1 = random.randrange(1,10)
num2 = random.randrange(1,10)
while(True):
    if (num1 == num2):
        num2 = random.randrange(1,10)
    else:
        break
num3 = random.randrange(1,10)
while(True):
    if (num3 == num1 or num3 == num2):
        num3 = random.randrange(1,10)
    else:
        break

array = [num1, num2, num3]
count1 = 0
count2 = 0

while(True):
    print "Please input 3 numbers: "
    inputnum1 = input()
    inputnum2 = input()
    inputnum3 = input()
    if (inputnum1 == array[0]):
        count1 = count1 + 1
    elif (inputnum1 in array and inputnum1 != array[0]):
        count2 = count2 + 1
    if (inputnum2 == array[1]):
        count1 = count1 + 1
    elif (inputnum2 in array and inputnum2 != array[1]):
        count2 = count2 + 1
    if (inputnum3 == array[2]):
        count1 = count1 + 1
    elif (inputnum3 in array and inputnum3 != array[2]):
        count2 = count2 + 1
    print count1, 'strike'
    print count2, 'ball'
    if(count1==3):
        break
    count1 = 0
    count2 = 0

