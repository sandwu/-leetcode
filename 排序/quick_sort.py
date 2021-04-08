def quick_sort(l):
    if len(l) <= 1: return l
    pivot = l[0]
    left = [x for x in l[1:] if x <= pivot]
    right = [x for x in l[1:] if x > pivot]
    return quick_sort(left) + [pivot] +quick_sort(right)


def quick_sort2(l):
    left = 0
    right = len(l) - 1
    return q_sort(l, left, right)


def q_sort(l, left, right):
    if left < right:
        pivot = partition(l, left, right)
        q_sort(l, left, pivot-1)
        q_sort(l, pivot+1, right)
    return l


def partition(l, left, right):
    pivot = l[left]
    while left < right:
        while left < right and l[right] >= pivot:
            right -= 1
        l[left] = l[right]
        while left < right and l[left] <= pivot:
            left += 1
        l[right] = l[left]
    l[left] = pivot
    return left


l1 = [1,4,6,84,42,1,2,5,4,6,78,56,74,6,7,8,9,3,5,6,2,1,4,6]

l1 = quick_sort2(l1)
