try:
    lis=[]
    print("Enter the values and stop to stop")
    while True:
        lis.append(int(input()))
except:
    max=0
    min=999
    sum=0
    count=0
    for i in lis:
        if(i<min):
            min=i
        if(i>max):
            max=i
    for i in lis:
        if(i==max or i==min):
            sum+=i
            count+=1
    avg=sum/count
    print("MAX :",max," MIN :",min," AVG :",avg)