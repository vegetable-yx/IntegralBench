import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 8th power
gamma_power = gamma_val**8

# Calculate pi squared
pi_sq = mp.pi**2

# Compute denominator: 512 * pi^2
denominator = 512 * pi_sq

# Divide numerator by denominator
result = gamma_power / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))