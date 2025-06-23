import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant
pi_value = mp.pi

# Compute numerator (π - 2)
numerator = pi_value - 2

# Divide by 4 to get final result
result = numerator / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))