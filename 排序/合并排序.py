def merge_sort(l):
    lenth = len(l)
    if lenth <= 1:
        return l
    mid = lenth // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left, right)


def merge(left, right):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res

l1 = [1,4,6,84,42,1,2,5,4,6,78,56,74,6,7,8,9,3,5,6,2,1,4,6]
l1 = merge_sort(l1)
print(l1)
