list1=[]

n=int(input("Enter the size of the list:"))
print("Enter elements:")

for i in range(0,n):
    list1.append(int(input()))
    
for i in list1:
    if(i>0):
        print(i,end=" ")
        
