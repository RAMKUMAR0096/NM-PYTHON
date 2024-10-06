def atm_distribution(amount):
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 1]
    distribution = {}
    
    for denom in denominations:
        distribution[denom] = amount // denom
        amount %= denom
    
    return distribution
print(atm_distribution(3865))
