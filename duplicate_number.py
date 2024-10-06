def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))
print(find_duplicates([1, 2, 3, 4, 2, 5, 6, 3]))
