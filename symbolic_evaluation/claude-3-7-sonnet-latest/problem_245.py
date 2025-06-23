import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define numerator and denominator as mpmath floats
numerator = mp.mpf(1024)
denominator = mp.mpf(15)

# Compute the exact fraction
result = numerator / denominator

# Print result to 10 decimal places
print(mp.nstr(result, n=10))