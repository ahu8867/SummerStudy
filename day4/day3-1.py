f1 = open("subject.txt", 'r')
f2 = open("user.txt", 'r')
save1 = {}
list1 = []
list2 = []
list3 = []
list4 = []
while True:
    line1 = f1.readline()
    if line1 == "":
        break
        f1.close()
    else:
        code,name = line1.split()
        save1[name] = code
while True:
    line2 = f2.readline()
    if line2 == "":
        break
    else:
        list1 = line2.split()
        line2 = f2.readline()
        list2 = line2.split()
        line2 = f2.readline()
        list3 = line2.split()
        line2 = f2.readline()
        list4 = line2.split()
del list1[0], list2[0], list3[0], list4[0]
while True:
    print "1. Check all subjects"
    print "2. Apply for class"
    print "3. Delete applied subject"
    print "4. Check all applied subjects"
    choice = input()
    if (choice==1):
        print save1
    elif (choice==2):
        name1 = raw_input("write user name: ")
        classCode1 = raw_input("write classcode: ")
        if name1=="kjh":
            list1.append(classCode1)
        elif name1=="gsw":
            list2.append(classCode1)
        elif name1=="ldk":
            list3.append(classCode1)
        elif name1=="smh":
            list4.append(classCode1)
    elif(choice==3):
        name2 = raw_input("write user name: ")
        classCode2 = raw_input("write classcode: ")
        if name2=="kjh":
            index=list1.index(classCode2)
            del list1[index]
        elif name2=="gsw":
            index=list2.index(classCode2)
            del list2[index]
        elif name2=="ldk":
            index=list3.index(classCode2)
            del list3[index]
        elif name2=="smh":
            index=list4.index(classCode2)
            del list4[index]
    elif(choice==4):
        name3 = raw_input("write user name: ")
        if name3=="kjh":
            for item in list1:
                print save1[item]
        elif name3=="gsw":
            for item in list2:
                print save1[item]
        elif name3=="ldk":
            for item in list3:
                print save1[item]
        elif name3=="smh":
            for item in list4:
                print save1[item]
    elif(choice==5):
        break
