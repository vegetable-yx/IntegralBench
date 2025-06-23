import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the exact analytical expression components
pi_term = mp.pi
constant_term = 2

# Calculate the numerator and denominator
numerator = pi_term - constant_term
denominator = 16

# Compute the final result
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))