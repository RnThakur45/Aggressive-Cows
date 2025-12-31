def isPossible(arr,c,m):
    cows = 1
    lastStall = arr[0]

    for num in arr:
        if(num - lastStall >= m):
            cows += 1
            lastStall = num
        
        if(cows == c):
            return True
    return False

def getDistance(arr, c):
    arr.sort()
    l = 1
    r =max(arr)-min(arr)  
    ans = -1

    while(l <= r):
        m = l + (r-l)//2
        if isPossible(arr, c , m):  #than right
            ans = m
            l = m + 1
        else:
            r = m -1 #else left
    return ans

print(getDistance([1,2,8,4,9], 3))