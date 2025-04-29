st="hello everyone"

# print(st[::-1])

reversed_str=''

for i in range(1,len(st)+1):
     reversed_str+=st[-i]
print(reversed_str)