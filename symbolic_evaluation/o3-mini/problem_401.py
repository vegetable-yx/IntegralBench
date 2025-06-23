import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign numerator and denominator as mpmath floats
numerator = mp.mpf(1)
denominator = mp.mpf(2)

# Compute the result: 1 divided by 2
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))