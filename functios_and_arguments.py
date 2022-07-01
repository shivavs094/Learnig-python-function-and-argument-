# keyward variables lenth arguments

def person (name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('shiva',Age=27,Mob=944377,city="TN")

def person (name,**data):
    print(name)
    print(data)
person("\nshiva",age=27,city='salem',mob=000000 )