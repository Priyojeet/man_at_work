def is_group(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group([1,2,3,4], 3))
