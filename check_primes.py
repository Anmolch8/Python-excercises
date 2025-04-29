num=int(input("Give a number to check if its prime:"))
prime_flag=True

if num<=0 or num==1:
    print("number is not prime")
    prime_flag=False
else:
    for d in range(2,int(num/2)+1):
        if num%d==0:
           prime_flag=False
           break
if(prime_flag):
         print("Number is prime")
else:
         print("Number is not prime")
