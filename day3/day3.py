refri = {}
a = open("data.txt", 'r')

while (True):
    line = a.readline()
    if line == "":
        break
        a.close()
    else:
        name, quantity = line.split()
        refri[name] = int(quantity)

def add():
    inputName1 = raw_input("Name: ")
    inputAmount1 = input("Amount: ")
    refri[inputName1] = inputAmount1

def delete():
    inputName2 = raw_input("Name: ")
    while (True):
        inputAmount2 = input("Amount: ")
        if (refri[inputName2]<inputAmount2):
            print "Out of range. Please input proper amount!"
        else:
            refri[inputName2] = refri[inputName2] - inputAmount2
            break

def check():
    print refri

while (True):
    print '1. INSERT ITEM'
    print '2. DELETE ITEM'
    print '3. CHECK ITEMS'
    print '4. EXIT'
    choice = input()
    if (choice==1):
        add()
    elif (choice==2):
        delete()
    elif (choice==3):
        check()
    elif (choice==4):
        a = open("data.txt", 'w')
        for i in refri.keys():
            a.write(str(i) + ' ' + str(refri[i]) + '\n')
        break