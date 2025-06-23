import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate numerator and denominator
numerator = -2023
denominator = 2022

# Perform exact fraction division
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print result to 10 decimal places
print(mp.nstr(result, n=10))