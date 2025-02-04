USD= int(input("how much you want to covert: "))
def coverter(USD):
    inr = USD *83
    print(USD, "USD = ", inr," INR" )

coverter(USD)
;


n =int(input(" please provide the number: "))

def check(n):
    if (n%2==0):
        print(n, " is ODD")
    elif (n %2 != 0):
        print(n, "is even")
    
check(n)