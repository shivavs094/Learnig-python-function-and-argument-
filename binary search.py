pos=-1
def search (list ,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1

    return False

list=[4,5,34,65,700,100,200]
n=70
if search(list,n):
    print("founde the values",pos+1)
else:
    print("not Available")