import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute constants and intermediate values
sqrt2 = mp.sqrt(2)           # √2 ≈ 1.41421356237
inv_sqrt2 = 1 / sqrt2        # 1/√2 ≈ 0.70710678118

# Compute dilogarithm terms
dilog1 = mp.polylog(2, inv_sqrt2)   # Li₂(1/√2)
dilog2 = mp.polylog(2, -inv_sqrt2)  # Li₂(-1/√2)

# Compute logarithmic term: ln(1 + √2)
log_val = mp.log(1 + sqrt2)
log_sq = log_val ** 2        # ln²(1 + √2)

# Combine terms according to the expression
term1 = 16 * dilog1         # 16·Li₂(1/√2)
term2 = -16 * dilog2        # -16·Li₂(-1/√2)
term3 = 8 * log_sq          # 8·ln²(1 + √2)
term4 = -mp.pi ** 2         # -π²

# Sum all terms and divide by 128
total = term1 + term2 + term3 + term4
result = total / 128

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))