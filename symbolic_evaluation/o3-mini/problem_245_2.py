import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Raise Gamma(1/4) to the 8th power
gamma_power8 = gamma_val**8

# Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute pi squared
pi_sq = mp.pi**2

# Calculate denominator: 512 * sqrt(2) * pi^2
denominator = 512 * sqrt2 * pi_sq

# Compute the final result: (Gamma(1/4)^8) / (512 * sqrt(2) * pi^2)
result = gamma_power8 / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))