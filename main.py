def Threesome(arr,x):
    sum=0
    arr.sort()
    print(arr)
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                sum = arr[i]+arr[j]+arr[k] 
                if sum == x:
                    return [i,j,k]
                    
arr=[2,4,6,8,10,1,3,5,7,9]
k=6
print(Threesome(arr,9))
