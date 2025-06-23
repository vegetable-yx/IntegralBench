import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate numerator and denominator
numerator = mp.mpf(2)
denominator = mp.pi

# Compute the final result
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))