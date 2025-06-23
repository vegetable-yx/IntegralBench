import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Define the numerator and denominator of the fraction
numerator = mp.mpf(1)
denominator = mp.mpf(4)

# Compute the exact value of 1/4
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))