import sys
x=input()
N , M = map(int, x.split())

a={}
for i in range(N):
    a[i+1]=i+1
    #a{1:1,2:2,3:3,4:4...b:b}

for x in sys.stdin:
    list1=[]
    num=0
    i , j = map(int, x.split()) #만약 i=1, j=3
    for q in range(i,j+1):
        list1.append(a[q])#[1,2,3]
    list1=list1[::-1] #[3,2,1]
    for u in range(i,j+1):
        a[u]=list1[num]
        num+=1



print(' '.join(map(str,a.values())))