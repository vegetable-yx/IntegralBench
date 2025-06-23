import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate numerator and denominator separately
numerator = mp.mpf(128)
denominator = mp.mpf(153)

# Perform the division
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))