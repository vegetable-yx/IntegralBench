import mpmath as mp

# Set internal decimal places for sufficient precision
mp.dps = 15

# Compute gamma(1/4)
gamma_quarter = mp.gamma(mp.mpf('0.25'))

# Raise gamma(1/4) to the 8th power
gamma_8th = gamma_quarter**8

# Compute denominator components
sqrt2 = mp.sqrt(2)  # Square root of 2
pi_squared = mp.pi**2  # Pi squared

# Combine denominator: 1024 * sqrt(2) * pi^2
denom = 1024 * sqrt2 * pi_squared

# Compute final result: gamma(1/4)^8 / denominator
result = gamma_8th / denom

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))