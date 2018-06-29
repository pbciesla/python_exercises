def find_min_index(nums):
    min_index = 0
    for i in range(len(nums)):
        if nums[min_index] > nums[i]:
            min_index = i
    return min_index


def selection_sort(nums):
    result =[]
    nums_copy = nums.copy()
    for i in range(len(nums)):
        min_num_index = find_min_index(nums_copy)
        result.append(nums_copy.pop(min_num_index))
    return result


test_list = [5, 41, 52, 6, 3, 25, 78, 14, 6, 98, 24, 0, 36, 10, 68, 92]
print(selection_sort(test_list))

