N,C=map(int,input().split())
arr=[int(input())for _ in range(N)]

def router_counter(distance):
    count=1
    start=arr[0]
    for i in range(1,N):
        if start+distance<=arr[i]:
            count+=1
            start=arr[i]
    return count

arr.sort()
start,end=1,arr[-1]-arr[0]

while start<=end:
    mid=(start+end)//2
    if router_counter(mid)>=C:
        answer=mid
        start=mid+1
    else:
        end=mid-1                   

print(answer)
