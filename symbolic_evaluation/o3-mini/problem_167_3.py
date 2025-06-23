import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute gamma(1/4)
gamma_val = mp.gamma(1/4)

# Raise gamma(1/4) to the 8th power
numerator = gamma_val ** 8

# Compute pi squared
pi_sq = mp.pi ** 2

# Calculate denominator: 512 * pi^2
denominator = 512 * pi_sq

# Final result: gamma(1/4)^8 / (512 * pi^2)
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))