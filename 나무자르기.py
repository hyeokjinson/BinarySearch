n,m=map(int,input().split())
arr1=list(map(int,input().split()))

def binary_search(arr,x):
    start=1
    end=arr[-1]
    while start<=end:
        mid=(start+end)//2
        count=0
        for i in arr:
            if i>=mid:
               count+=i-mid
        if count>=x:
            start=mid+1
        else:
            end=mid-1
    return end

arr1.sort()
print(binary_search(arr1,m))
