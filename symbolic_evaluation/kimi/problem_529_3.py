import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate the numerical factors
factor_2 = mp.mpf(2)
factor_2023 = mp.mpf(2023)

# Compute the product of the factors
result = factor_2 * factor_2023

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))