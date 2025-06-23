import mpmath as mp

mp.dps = 15  # Set internal decimal precision

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute (sqrt(5) - 2)
numerator = sqrt5 - 2

# Multiply by pi
product = mp.pi * numerator

# Divide by 2 to get final result
result = product / 2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))