from collections import Counter
import sys
def binary_search(a,x):
    start=0
    end=len(a)-1
    cnt=0
    while start<=end:
        mid=(start+end)//2
        if x==a[mid]:
            return mid
        elif x>a[mid]:
            start=mid+1
        else:
            end=mid-1
    return -1

n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
c=Counter(arr1)
arr1.sort()
ret=[0 for _ in range(m)]
for i in range(m):
    idx=binary_search(arr1,arr2[i])
    if idx==-1:
        continue
    ret[i]=c[arr2[i]]

print(" ".join([str(i) for i in ret]).rstrip())