import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator
numerator = mp.mpf(8)
denominator = mp.mpf(7)

# Compute the fraction 8/7
result = numerator / denominator

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))