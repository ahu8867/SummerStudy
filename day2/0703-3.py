refri = {}

while (True):
    print '1. INSERT ITEM'
    print '2. DELITE ITEM'
    print '3. CHECK ITEMS'
    print '4. EXIT'
    choice = input()
    if (choice==1):
        inputName1 = raw_input("Name: ")
        inputAmount1 = input("Amount: ")
        refri[inputName1] = inputAmount1
    elif (choice==2):
        inputName2 = raw_input("Name: ")
        while(True):
            inputAmount2 = input("Amount: ")
            if (refri[inputName2]<inputAmount2):
                print "Out of range. Please input proper amount!"
            else:
                refri[inputName2] = refri[inputName2] - inputAmount2
                break
    elif (choice==3):
        print refri
    elif (choice==4):
        break