def maxSum(arr, k):

    arr.sort()

    lp = 0
    rp = len(arr) - 1

    sum = 0

    while lp < rp:
        if arr[lp] + arr[rp] > k:
            rp-=1
        else:
            sum = max(sum, arr[lp] + arr[rp])
            lp +=1
    
    return sum
