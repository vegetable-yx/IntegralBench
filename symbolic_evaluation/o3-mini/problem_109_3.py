import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Square the Gamma(1/4) value
gamma_sq = gamma_val ** 2

# Compute the denominator: 4 * sqrt(2 * pi)
denom = 4 * mp.sqrt(2 * mp.pi)

# Divide the squared gamma by the denominator
result = gamma_sq / denom

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))