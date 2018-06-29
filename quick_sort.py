def quick_sort(to_sort):
    length = len(to_sort)
    left = []
    right = []
    if length < 2:
        return to_sort
    else:
        mid = to_sort[0]
        for i in to_sort[1:]:
            if i < mid:
                left.append(i)
            elif i > mid:
                right.append(i)
    return quick_sort(left) + [mid] + quick_sort(right)


print(quick_sort([2, 6, 12, 4, 78, 52, 10, 3, 65, 9, 45, 0]))
