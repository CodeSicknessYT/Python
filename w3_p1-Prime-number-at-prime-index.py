def isPrime(n):
    if(n==0 or n==1):
        return False
    else:
        for i in range(2,int(n/2)+1):
            if(n%i==0):
                return False
        return True

f=int(input("how many values?\n"))
lis=[]
print("enter values here\n")
for i in range(f):
    r=int(input())
    if(r>1 and r<100):
        lis.insert(i,r)
    else:
        print("Invalid Input")
        continue

for i in range(len(lis)):
    if(isPrime(lis[i])):
        if(isPrime(i)):
            print(lis[i]," , ",i)