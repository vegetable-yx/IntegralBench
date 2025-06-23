import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator
numerator = 2023
denominator = 2022

# Compute the fraction: 2023/2022
fraction = mp.mpf(numerator) / mp.mpf(denominator)

# Apply the negative sign to get the final result
result = -fraction

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))