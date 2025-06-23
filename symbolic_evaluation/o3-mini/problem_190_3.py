import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute pi^3 / 192
term1 = mp.pi ** 3 / 192

# Calculate ln(1 + sqrt(2))
ln_val = mp.ln(1 + mp.sqrt(2))

# Compute (pi / 40) * [ln(1 + sqrt(2))]^2
term2 = (mp.pi / 40) * (ln_val ** 2)

# Compute ln(2)
ln2 = mp.ln(2)

# Calculate [ln(2) * ln(1 + sqrt(2))] / 20
term3 = (ln2 * ln_val) / 20

# Compute Li_2(1/2) using the polylog function
li2_val = mp.polylog(2, 0.5)

# Compute - (1/10) * Li_2(1/2)
term4 = - (1/10) * li2_val

# Sum all terms to get the final result
result = term1 - term2 + term3 + term4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))