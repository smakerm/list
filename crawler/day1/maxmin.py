
def maxmin(L, start, end):
    if end - start <= 1:
        return (max(L[end],L[start]), min(L[end],L[start]))
    else:
        max1, min1 = maxmin(L, start ,(start+end)//2)
        max2, min2 = maxmin(L, (start+end)//2+1, end)
        return (max(max1, max2), min(min1, min2))

L = [1,2,3,5,9,1,-2,-9,8,]
maxv, minv = maxmin(L, 0, len(L)-1)

print(maxv, minv)