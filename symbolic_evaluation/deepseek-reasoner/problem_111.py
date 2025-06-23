import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression
sqrt2 = mp.sqrt(2)  # Compute square root of 2
pi_squared = mp.pi ** 2  # Compute π squared

# Compute the difference term (8 - π²)
difference = 8 - pi_squared

# Multiply by sqrt(2)/2 to get final result
result = (sqrt2 / 2) * difference

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))