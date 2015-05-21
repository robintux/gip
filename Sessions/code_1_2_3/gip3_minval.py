def find_min(lst):
    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i

    return min_val
