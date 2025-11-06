import copy

original_list = [1, 2, [3, 4], 5]
shallow_copied_list = copy.copy(original_list)
deep_copied_list = copy.deepcopy(original_list)
original_list[2][0] = 'changed'
print("Original list after modification:", original_list)
print("Shallow copied list:", shallow_copied_list)
print("Deep copied list:", deep_copied_list)
