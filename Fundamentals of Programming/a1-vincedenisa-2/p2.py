def productOfFactors(n):
    print("The product of the proper factors is: ")
    p=1
    for i in range(2, n):
        if n%i==0:
            p=p*i
    print(p)

n = int(input("Insert n: "))
productOfFactors(n)