while True:
    print("+ addtion")
    print("- subtraction")
    print("* multiplication")
    print("/ divison")
    ch=input("enter a operator:")
    n1=float(input('enter a number:'))
    n2=float(input('enter a number:'))
    if ch=="+":
        res=n1+n2
        print(res)
        break
    elif ch=="-":
        res=n1-n2
        print(res)
        break
    elif ch=="*":
        res=n1*n2
        print(res)
        break
    elif ch=="/":
        res=n1/n2
        print(res)
        break
    else:
        print("operator is not valid:")
        break
