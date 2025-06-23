import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute ln(1 + sqrt(2)) once and reuse
sqrt2 = mp.sqrt(2)
ln_arg = 1 + sqrt2
ln_term = mp.log(ln_arg)

# Calculate each power of ln_term
ln_cubed = ln_term ** 3
ln_squared = ln_term ** 2

# Compute each term of the expression separately
term1 = mp.pi ** 3 / 144
term2 = (mp.pi / 18) * ln_cubed
term3 = (mp.pi / 12) * ln_squared
term4 = (mp.pi / 12) * ln_term

# Combine all terms to get the final result
result = term1 - term2 + term3 - term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))