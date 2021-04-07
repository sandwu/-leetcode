def bubble_sort(l):
    for i in range(len(l), -1, -1):
        for j in range(1, i):
            if l[j-1] > l[j]:
                l[j-1], l[j] = l[j], l[j-1]
    return l


def bubble_sort2(l):
    for i in range(len(l), -1, -1):
        flag = 1
        for j in range(1, i):
            if l[j-1] > l[j]:
                l[j-1], l[j] = l[j], l[j-1]
                flag = 0
        if flag == 1:
            return l
    return l
  
l1 = [1,4,6,84,42,1,2,5]
l2 = [1,4,6,84,42,1,2,5]

l1 = bubble_sort(l1)
l2 = bubble_sort2(l2)

