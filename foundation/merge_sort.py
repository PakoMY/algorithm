def merge_sort(num):
    if len(num) <= 1:
        return num
    mid = len(num)/2
    left = merge_sort(num[:mid])
    right = merge_sort(num[mid:])
    return merge(left, right)

def merge(left, right):
    tmp = []
    point_l = point_r = 0
    while point_l < len(left) and point_r < len(right):
        if left[point_l] < right[point_r]:
            tmp.append(left[point_l])
            point_l += 1
        else:
            tmp.append(right[point_r])
            point_r += 1
    if point_l == len(left):
        for i in right[point_r:]:
            tmp.append(i)
    else:
        for i in left[point_l:]:
            tmp.append(i)
    return tmp
