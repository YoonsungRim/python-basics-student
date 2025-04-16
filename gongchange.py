import sys
x=input()
N , M = map(int, x.split())

a={}
for i in range(N):
    a[i+1]=i+1
    #a{1:1,2:2,3:3,4:4...b:b}

for x in sys.stdin:
    i , j = map(int, x.split()) #만약 i=3, j=1
    ii=a[i]
    jj=a[j]
    a[i]=jj
    a[j]=ii

print(' '.join(map(str,a.values())))