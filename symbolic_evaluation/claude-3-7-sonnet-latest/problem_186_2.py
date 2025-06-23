import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate square root of 24
sqrt_24 = mp.sqrt(24)

# Compute the term (5 + sqrt(24))
five_plus_sqrt24 = 5 + sqrt_24

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply (5 + sqrt(24)) by pi^2
numerator = five_plus_sqrt24 * pi_squared

# Divide by 32 to get final result
result = numerator / 32

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))