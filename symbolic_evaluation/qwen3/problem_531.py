import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate numerator and denominator
numerator = mp.mpf(5)
denominator = mp.mpf(6)

# Compute the exact fraction
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))