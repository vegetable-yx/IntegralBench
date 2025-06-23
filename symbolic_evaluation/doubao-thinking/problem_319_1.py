import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate numerator and denominator using exact values
numerator = mp.mpf(4)
denominator = mp.mpf(3)

# Compute the exact fraction
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))