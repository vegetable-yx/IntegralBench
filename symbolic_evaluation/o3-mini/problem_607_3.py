import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate constants
sqrt2 = mp.sqrt(2)  # Square root of 2
a = sqrt2 - 1       # Positive argument for dilogarithm: √2 - 1 ≈ 0.4142
b = 1 - sqrt2       # Negative argument for dilogarithm: 1 - √2 ≈ -0.4142

# Compute dilogarithm values
dilog_a = mp.polylog(2, a)  # Li₂(√2 - 1)
dilog_b = mp.polylog(2, b)  # Li₂(1 - √2)

# First term: half the difference of the dilogarithms
term1 = 0.5 * (dilog_a - dilog_b)

# Compute logarithmic term: ln((1 + √2)/2)
log_arg = (1 + sqrt2) / 2
log_term = mp.log(log_arg)

# Second term: (π/4) * ln((1 + √2)/2)
term2 = (mp.pi / 4) * log_term

# Sum both terms for final result
result = term1 + term2

# Print result to 10 decimal places
print(mp.nstr(result, n=10))