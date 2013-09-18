#HW1-I.py
#Program by Valerie Lambert

"""
Suppose there exists an array A[1...n] of length n. Each item A[i] in
the array has a type t(A[i]) in (soc, mil, oth). We are looking for an
algorithm to sort this array such that all the soc-type items are at
the front of the array, and all the mil-type items are in the back.
The only actions permitted on the array are, for an i, look up 
t(A[i]), and, for i and j, swap A[i] and A[j].

We can have a sorting algorithm of O(n) by just iterating through the 
array twice. Once to find and move all of the first type of item to the 
front, and then again to find and move all of the third type of item to 
the back. By changing the number of items in the list by a factor of 
10, we can see that the time it takes to run the algorithm also 
increases by a factor of 10. The algorithm is as follows:

    Let i be the index for the last item
        and j be the index for the first non-soc item
    While i is more than j
        If t(A[i]) is soc then
            swap A[i] and A[j]
            Let j be the index of the next non-soc item
        Endif
        Let i be th eindex of the previous item
    Endwhile
    Let i be the index for the first item
        and j be the index for the last non-mil item
    While i is less than j
        If t(A[i]) is mil then
            swap A[i] and A[j]
            Let j be the index of the next non-mil item
        Endif
        Let i be the index of the next item
    Endwhile

On my machine, with n at 10,000 and running the algorithm 1000 times,
the average time is 11 seconds (without the checks).
"""
import random
import time

def createlist():
    mylist = [] 
    for i in range(0,10000):
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
            while mylist[j] is 1:
                j += 1
        i -= 1
    j = len(mylist)-1
    while mylist[j] is 3 and j >= 0:
        j -= 1
    i = 0
    while i < j:
        if mylist[i] is 3:
            mylist[i], mylist[j] = mylist[j], mylist[i]
            while mylist[j] is 3:
                j-=1
        i+=1
    return mylist

def checklist(mylist):
    for i in range(0, len(mylist)-1):
        if not mylist[i] <= mylist[i+1]:
            print("list was not correctly sorted:")
            print(mylist)
            break

def main():
    start_time = time.time()
    for i in range(0, 1000):
        mylist = createlist()
        checklist(sortlist(mylist))
    print(time.time() - start_time)

main()
