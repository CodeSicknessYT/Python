def gandhi(n):
    if(n==0):
        return False
    while(n!=1):
        if(n%4!=0):
            return False
        n/=4
    return True

n=int(input("Enter the value to check Gandhi number: "))
if(gandhi(n)):
    print(n," is a Gandhi Number")
else:
    print(n," is not a Gandhi Number")