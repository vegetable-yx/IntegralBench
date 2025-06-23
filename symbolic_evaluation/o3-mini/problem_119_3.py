import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Raise Gamma(1/4) to the 8th power
gamma_val_8 = gamma_val**8

# Compute pi squared
pi_sq = mp.pi**2

# Calculate the denominator: 2048 * pi^2
denominator = 2048 * pi_sq

# Final result: Gamma(1/4)^8 / (2048 * pi^2)
result = gamma_val_8 / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))