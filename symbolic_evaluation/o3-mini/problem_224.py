import mpmath as mp

# Set internal decimal precision to 15 for accurate results
mp.dps = 15

# Calculate ln(2) and then square it
ln2 = mp.log(2)
ln2_squared = ln2 ** 2

# Compute π/4 multiplied by ln²(2)
term1 = (mp.pi / 4) * ln2_squared

# Compute dilogarithm Li₂(1/2)
dilog_half = mp.polylog(2, 0.5)

# Compute dilogarithm Li₂(-1/2)
dilog_neg_half = mp.polylog(2, -0.5)

# Combine terms: π/4 * ln²2 + Li₂(1/2) - Li₂(-1/2)
result = term1 + dilog_half - dilog_neg_half

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))