import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator as mpmath floats
numerator = mp.mpf(9)
denominator = mp.mpf(4)

# Compute the exact fraction
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))