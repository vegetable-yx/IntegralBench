import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate common constants
sqrt2 = mp.sqrt(2)  # √2

# Compute arguments for the dilogarithm functions
arg1 = 0.5 - 1/(2*sqrt2)  # 1/2 - 1/(2√2)
arg2 = 0.5 + 1/(2*sqrt2)  # 1/2 + 1/(2√2)

# Compute the difference of dilogarithms
li_diff = mp.polylog(2, arg1) - mp.polylog(2, arg2)

# Compute the first term: √2 * (Li₂(...) - Li₂(...))
term1 = sqrt2 * li_diff

# Compute the ratio: (√2 + 1) / (√2 - 1)
ratio = (sqrt2 + 1) / (sqrt2 - 1)

# Natural logarithm of the ratio
ln_ratio = mp.log(ratio)

# Compute the second term: (1/4) * [ln(ratio)]²
term2 = (1/4) * (ln_ratio ** 2)

# Compute the third term: ln(2) * ln(ratio)
term3 = mp.log(2) * ln_ratio

# Combine all terms
result = term1 + term2 - term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))