def sort_array(source_array):
    odd_array = [i for i in source_array if i%2 != 0]
    odd_array.sort()
    j = 0
    ans = []
    for i in source_array:
        if i%2 != 0:
            ans.append(odd_array[j])
            j += 1
        else:
            ans.append(i)
    return ans