def fab(n):
    a=0
    b=1

    if n <=0:
        print("Entered Value are Negative kindly enter positive values:",n)
    elif n==1:
        print(a)
        print(b)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c

            print(c)

            if c>=89:
                break

n= (int(input("Enter your required fibinachci:")))
fab(n)