import mpmath as mp

# Set internal decimal places for sufficient precision
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 4th power
gamma_fourth = gamma_val**4

# Compute the denominator: 8 * sqrt(2 * pi)
denom = 8 * mp.sqrt(2 * mp.pi)

# Divide to get the final result
result = gamma_fourth / denom

# Print result to 10 decimal places
print(mp.nstr(result, n=10))