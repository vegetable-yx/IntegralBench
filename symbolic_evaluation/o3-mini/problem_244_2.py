import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 8th power
gamma_power = gamma_val ** 8

# Compute pi squared
pi_sq = mp.pi ** 2

# Calculate the denominator: 128 * pi^2
denominator = 128 * pi_sq

# Divide numerator by denominator to get the result
result = gamma_power / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))