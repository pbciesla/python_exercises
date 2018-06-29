def binary_search(to_search, wanted):
    low = 0
    high = len(to_search)-1

    while low <= high:
        mid = (low + high) // 2
        if wanted == to_search[mid]:
            return mid
        elif wanted < to_search[mid]:
            high = mid - 1
        elif wanted > to_search[mid]:
            low = mid + 1
        else:
            return None
    return mid


nums = list(range(50000))
number = 1367

print(binary_search(nums, number))
