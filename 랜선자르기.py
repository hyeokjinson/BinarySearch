k,n=map(int,input().split())
arr=[]
for _ in range(k):
    arr.append(int(input()))

def binary_search(arr,x):
    start=1
    end=arr[-1]
    while start<=end:
        mid=(start+end)//2
        count=0
        for i in arr:
            if i>=mid:
                count+=i//mid
        if count>=x:
            start=mid+1
        else:
            end=mid-1
    return end
arr.sort()
print(binary_search(arr,n))