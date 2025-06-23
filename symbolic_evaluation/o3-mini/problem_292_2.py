import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Raise Gamma(1/4) to the 8th power
gamma_power = gamma_val**8

# Calculate pi squared
pi_sq = mp.pi**2

# Compute denominator: 128 * pi^2
denom = 128 * pi_sq

# Divide numerator by denominator
result = gamma_power / denom

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))