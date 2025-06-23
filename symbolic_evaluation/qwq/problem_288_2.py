import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute fundamental constants and terms
sqrt2 = mp.sqrt(2)
ln_term = mp.log(1 + sqrt2)  # ln(1+√2)

# Calculate powers of ln_term for reuse
ln3 = ln_term ** 3
ln2 = ln_term ** 2
ln1 = ln_term

# Compute numerator component terms
term1 = -3 * ln3
term2 = (mp.mpf(3)/2) * (mp.pi + 2*sqrt2) * ln2
term3 = -( (9 + 2*sqrt2*mp.pi) / 2 ) * ln1
term4 = (mp.pi + 3*sqrt2) / 2

# Combine terms and divide by 4
numerator = term1 + term2 + term3 + term4
result = numerator / 4

# Print with 10 decimal precision
print(mp.nstr(result, n=10))