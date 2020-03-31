def binary_search(a,x):
    start=0
    end=len(a)-1

    while start<=end:
        mid=(start+end)//2
        if x==a[mid]:
            return 1
        elif x>a[mid]:
            start=mid+1
        else:
            end=mid-1
    return 0

n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
arr1.sort()
for i in range(m):
    print(binary_search(arr1,arr2[i]))