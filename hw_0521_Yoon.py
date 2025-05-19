#1296
empty=input()
A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))
a=len(A-B)
b=len(B-A)
print(a+b)