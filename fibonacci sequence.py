
n=int(input("Upper limit:"))

first=0
second=1
print(first,second,end=" ")
third=first+second

while(third<=n):
    
    print(third,end=" ")
    first=second
    second=third
    third=first+second    

