
def count (lis):
    even=0
    odd=0
    for i in lis:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lis=[20,35,44,56,55,59,25,34,77,84,99,398,50]
even,odd= count(lis)

print("even Count: {} \nthe Odd count is :  {}".format(even,odd))



def count(lst):
    name1=0
    name2=0

    for i in lst:
        if  (len(i)) <= 5:
            name1+=1
        else:
            name2+=1

    return name1,name2

lst=['venkatesan', 'selvi','shiva','pooja','thenmozhi','subhashchandrabose','tamilselvan','satheeshkumar',]
name1,name2= count(lst)

print(" number of lettes less than 5: {} \nnumber of lettes greater than 5: {}".format(name1,name2))