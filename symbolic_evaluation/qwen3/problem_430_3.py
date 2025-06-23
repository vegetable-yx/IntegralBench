import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate numerator and denominator as arbitrary-precision floats
numerator = mp.mpf(2023)
denominator = mp.mpf(2022)

# Compute the exact fraction with high precision
exact_fraction = numerator / denominator

# Apply the negative sign
result = -exact_fraction

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))