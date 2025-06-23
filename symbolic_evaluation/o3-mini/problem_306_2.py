import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf('0.25'))

# Square the gamma value
gamma_sq = gamma_val ** 2

# Compute denominator: 2 * sqrt(2 * pi)
denom = 2 * mp.sqrt(2 * mp.pi)

# First term: Gamma(1/4)^2 / (2 * sqrt(2 * pi))
term1 = gamma_sq / denom

# Compute the argument for the logarithm: (sqrt(2) + 1) / sqrt(2)
sqrt2 = mp.sqrt(2)
log_arg = (sqrt2 + 1) / sqrt2

# Compute the natural logarithm of the argument
log_val = mp.log(log_arg)

# Second term: pi * ln((sqrt(2)+1)/sqrt(2))
term2 = mp.pi * log_val

# Final result: term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))