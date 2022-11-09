
li1=[]
li2=[]

n=int(input("enter any num for n>>"))
m=int(input("enter any num for m>>"))

for i in range(1, n+1):
    if (i% 2 == 0):
        li1.append(i)
    else:
        li2.append(i)

li3=li2+li1
print(li3)
x=(li3[m-1])
print(f"the number is {x}")