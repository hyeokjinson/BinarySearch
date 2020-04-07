import sys
n=int(input())
arr1=list(map(int,input().split()))
n2=int(input())
arr2=list(map(int,input().split()))
def binary_search(arr,x):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if x==arr[mid]:
            return 1
        if x>arr[mid]:
            start=mid+1
        else:
            end=mid-1
    return 0
arr1.sort()
result=[]
for i in range(n2):
    result.append(binary_search(arr1,arr2[i]))

print(" ".join(str(i)for i in result).rstrip())
