import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_quarter = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 4th power
gamma_quarter_p4 = gamma_quarter**4

# Compute the denominator: 16 * sqrt(2 * pi)
denom_factor = 16 * mp.sqrt(2 * mp.pi)

# Compute the final result: [Gamma(1/4)^4] / [16 * sqrt(2 * pi)]
result = gamma_quarter_p4 / denom_factor

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))