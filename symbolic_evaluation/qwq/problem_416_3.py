import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate e^(π/4)
exponent_term = mp.exp(mp.pi/4)

# Multiply sqrt(2) by e^(π/4)
product = sqrt2 * exponent_term

# Subtract 1 from the product
numerator = product - 1

# Divide by 2 to get final result
result = numerator / 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))