# def topten():
#     yield 1
#     yield 2
#     yield 3
#
#     yield 5
#
# val=topten()
# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))

# for i in val:
#     print(i)


def topten():
    n=0
    while n<=10:
        sq=n*n
        yield sq
        n+=1
val=topten()
for i in val:
    print(i)