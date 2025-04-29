num=int(input("Give the number to find the factorial:"))
f=1

if num==1:
    print(f"factorial is {num}")
elif num==0:
    print(f'factorial is 1')
else:
    for i in range(1,num+1):
        f=f*i
    print(f)
    