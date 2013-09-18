import random

def createlist():
    mylist = [] 
    for i in range(0,1000):
        n = random.randint(1,3)
        mylist.append(n)
    return mylist

def sortlist(mylist):
    i = len(mylist)-1
    j = 0
    while mylist[j] is 1 and j < len(mylist):
        j += 1
    while i > j:
        if mylist[i] is 1:
            mylist[i], mylist[j] = mylist[j], mylist[i]
            j += 1
            while mylist[j] is 1 and j < len(mylist):
                j += 1
        i -= 1
    j = len(mylist)-1
    while mylist[j] is 3 and j >= 0:
        j -= 1
    i = 0
    while i < j:
        if mylist[i] is 3:
            mylist[i], mylist[j] = mylist[j], mylist[i]
            j -= 1
            while mylist[j] is 3 and j >= 0:
                j -= 1
        i+=1
    return mylist

def checklist(mylist):
    for i in range(0, len(mylist)-1):
        if not mylist[i] <= mylist[i+1]:
            print("list was not correctly sorted:")
            print(mylist)
            break

def main():
    for i in range(0, 10000):
        mylist = createlist()
        checklist(sortlist(mylist))

main()
