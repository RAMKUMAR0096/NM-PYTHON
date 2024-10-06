def remove_sequence(lst, n):
    return [x for i, x in enumerate(lst) if (i + 1) % n != 0]
print(remove_sequence([1, 2, 3, 4, 5, 6, 7, 8], 2))
