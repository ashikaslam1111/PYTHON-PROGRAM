num=int(input(">>"))
li=[]
while(num>0):
    x=num%10
    num=num//10
    li.append(x)

d=(len(li))
print(f"the are {d} digit in the number")