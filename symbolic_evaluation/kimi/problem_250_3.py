import mpmath as mp
mp.dps = 15

# Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Calculate sqrt(2) - 1
adjusted_term = sqrt2 - 1

# Multiply by pi to get the final result
result = mp.pi * adjusted_term

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))