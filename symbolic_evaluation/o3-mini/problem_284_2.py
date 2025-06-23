import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate common constant: sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute log(1 + sqrt(2))
log_val = mp.log(1 + sqrt2)

# Square the logarithm: [log(1 + sqrt(2))]^2
log_sq = log_val ** 2

# Compute term1: (4 - pi) * [log(1 + sqrt(2))]^2
term1 = (4 - mp.pi) * log_sq

# Compute term2: 8 * Li_2(2 - sqrt(2))
term2 = 8 * mp.polylog(2, 2 - sqrt2)

# Compute term3: 8 * Li_2(sqrt(2) - 1)
term3 = 8 * mp.polylog(2, sqrt2 - 1)

# Combine terms: (term1 + term2 - term3) / 8
result = (term1 + term2 - term3) / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))