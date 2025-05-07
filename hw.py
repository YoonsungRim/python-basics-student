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
#