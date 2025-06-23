import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the square root of 42
sqrt_42 = mp.sqrt(42)

# Multiply by pi
pi_sqrt_42 = mp.pi * sqrt_42

# Divide by 2 to get the final result
result = pi_sqrt_42 / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))