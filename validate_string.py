def validate_string(s):
    return s.isalnum() and any(c.islower() for c in s) and any(c.isupper() for c in s) and any(c.isdigit() for c in s)
print(validate_string("Aa1"))
