def quicksort(L, left, right):
    i = left
    j = right

    if i >= j:
        return L
    key = L[left]
    while i < j:    
        while L[j] > key and i < j:
            j -= 1
        L[i] = L[j]
    
        while L[i] < key and i < j:
            i += 1
        L[j] = L[i]
    
    L[i] = key

    quicksort(L, left, i-1)
    quicksort(L, j+1, right)
    return L  

L = [1, 8, 4, 9, 7, 5]
quicksort(L, 0, len(L)-1)
print(L)
