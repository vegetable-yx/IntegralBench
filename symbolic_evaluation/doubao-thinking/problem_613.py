import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator as mpmath floats
numerator = mp.mpf(1)
denominator = mp.mpf(5)

# Compute the result of 1/5
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))