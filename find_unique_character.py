def first_unique(s):
    for i, char in enumerate(s):
        if s.count(char) == 1:
            return char
    return None
print(first_unique("swiss"))
