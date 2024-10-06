def operations(a, b):
    return {'add': a + b, 'subtract': a - b, 'multiply': a * b, 'divide': a / b if b != 0 else 'undefined'}
print(operations(10, 5))
