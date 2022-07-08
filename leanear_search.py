pos=-1
def search(list,n):
    i=0

    while i < len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False

list=[55,65,48,98,32,45]
n=65
if search(list,n):
    print("Entered value are in the list",pos)

else:
    print('Not found')





pos=-1
def search(list,n):

    for i in range (len(list)):
        if list[i] == n:
            globals()["pos"]=i
            return True
        else:
            return False


list=[55,65,48,98,32,45]
n=55

if search(list,n):
    print("Entered value are in the list",pos+1)

else:
    print('Not found')