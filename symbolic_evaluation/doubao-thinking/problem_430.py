import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the exact fraction: -2023/2022
numerator = -2023
denominator = 2022

# Compute the result as a high-precision floating-point number
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))