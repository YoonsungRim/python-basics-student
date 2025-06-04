#10773번
nums=[]
a=int(input())
for _ in range(a):
    b=int(input())
    if b!=0:
        nums.append(b)
    elif b==0:
        del nums[-1]
print(sum(nums))

#2164번
n=int(input())
list1=[]
for i in range(n):
    list1.append(i+1)
while len(list1)!=1:
    del list1[-1]
    a=list1.pop()
    list1.insert(0,a)
print(list1+1)
