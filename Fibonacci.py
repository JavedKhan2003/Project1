n=int(input("Enter the numbers for checking: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes,  the number  is in Fibonacci Series.")
    else:
        print("No, the number is not in Fibonacci Series.")
