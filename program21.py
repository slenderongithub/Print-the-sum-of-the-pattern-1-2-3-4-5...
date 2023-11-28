#WAP to print the following series till nth terms and find the sums: 1-2+3-4+5..... 

n=int(input("enter the number of terms: "))
s=0
for i in range(1,n+1):
    print(i,end="")
    if(i%2==0):
        print("+",end="")
        s=s+i
    else:
        print("-",end="")
        s=s-i
print("=",s) 
    