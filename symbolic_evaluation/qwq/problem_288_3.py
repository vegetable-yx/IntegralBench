import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute constants and intermediate values
sqrt2 = mp.sqrt(2)
ln_value = mp.log(1 + sqrt2)  # ln(1+√2)

# Calculate individual terms
term1 = mp.pi**2 / 16
term2 = (mp.pi / 2) * ln_value
term3 = (ln_value**2) / 2
term4 = (sqrt2 * ln_value) / 2
term5 = (sqrt2 - 1) / 2

# Combine all terms
result = term1 - term2 + term3 - term4 + term5

# Print result with 10 decimal places
print(mp.nstr(result, n=10))