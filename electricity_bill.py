def calc_bill(units):
    if units <= 100:
        return units * 5
    elif units <= 300:
        return (100 * 5) + (units - 100) * 7
    else:
        return (100 * 5) + (200 * 7) + (units - 300) * 10
print(calc_bill(350))
