#1018번
q=input().split()
N , M = int(q[0]) , int(q[1])
a=[]
while input()!='':
    b=a.list(input()) #WWWBBWWWB
    alist=[]
    alist.append(b)#alist에 모든 체스판 입력 완료

comparelist=[]
for i in range(N-8):#(y좌표)
    for j in range(M-8):#(x좌표)
        c = alist[i][j:j+7]
        zero=0
        count=0
        for k in range(7):
            if c[k]=='W':
                if c[k+1]=='W':
                    continue
                if c[k+1]=='B':
                    count+=1
            else:
                if c[k]=='B':
                    if c[k+1]=='B':
                        continue
                    if c[k+1]=='W':
                        count+=1
        comparelist.append(count)


        d = alist[i][j:j+7]

#w로 시작할때:
#다음에 w가 있다면:+1
#   다음 다음에 W가 있다면:+1
#       다음 다음다음에 W가 있다면:+1
#다음에 B가 있다면:+0
#   다음 다음에 W가 있다면:+0
#       다음 다음 다음에 B가 있다면:+0

#1018번은 어려워서 아직 풀고있어요


#19532번
# a(x) +b(y) =c       2(x) +3(y) =12   2(x) +3(y) =12 
# d(x) +e(y) =f       1(x) -1(y) =1   -2(x) +2(y) =-2
list1=list(map(int,input().split()))
a,b,c,d,e,f=list1[0],list1[1],list1[2],list1[3],list1[4],list1[5] #2 3 12 1 -1 1

a1=a
b1=b
c1=c

if a>0 and d>0:
    diva=a/d
    d=d*(diva)*(-1)
    e=e*(diva)*(-1)
    f=f*(diva)*(-1)
else:
    d=d*(a/d)
    e=e*(a/d)
    f=f*(a/d)

#a=a+d
b=b+e
c=c+f
yanswer=c/b
xanswer=(c1-b1* yanswer)/a1
print(int(xanswer),int(yanswer))
#VS code에서는 잘 돌아가는데 문제에서는 틀렸다고 떠요