#2501
q=input().split()
n , k = int(q[0]) , int(q[1]) #n=6, k=3
a=[]# [1,2,3,6]
for i in range(n):
    if n % (i+1)==0:
        a.append(i+1) # 약수 다구했다
if len(a)<k:
    print(0)
else:
    print(a[k-1])

    
#9506
while True:
    q = int(input())
    if q== -1:
        break
    else:
        a=[]# [1,2,3,6]
        for i in range(1,q):
            if q % (i)==0:
                a.append(i)
        b=0
        for j in a:
            b=j+b
        if b==q:
            print(q , '=' , ' + '.join(map(str,a)))
        else:
            print(f'{q} is NOT perfect.')
#1978
d=0#소수개수
a=int(input())
b=list(map(int,input().split()))  #[1,2,3]
for i in b:
    c=0
    for k in range(1,1+i):
        if i%k==0:
            c+=1
    if c==2:
        d+=1
print(d)