def binary_array_to_number(arr):  
    ans = sum(arr[i]*2**(len(arr)-i-1) for i in range(len(arr)))
    return ans