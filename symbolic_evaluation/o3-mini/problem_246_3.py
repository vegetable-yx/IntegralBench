import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Raise Gamma(1/4) to the 8th power
gamma_power8 = gamma_val**8

# Compute pi squared
pi_sq = mp.pi**2

# Compute denominator: 32 * pi^2
denom = 32 * pi_sq

# Compute the final result: Gamma(1/4)^8 / (32 * pi^2)
result = gamma_power8 / denom

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))