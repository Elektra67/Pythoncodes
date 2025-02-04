n =int(input(" please provide the number: "))

def check(n):
    if (n%2==0):
        print(n, " is ODD")
    elif (n %2 != 0):
        print(n, "is even")
    
check(n)
