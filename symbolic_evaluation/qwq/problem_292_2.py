import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Gamma(1/4)
gamma_value = mp.gamma(mp.mpf(1)/4)

# Compute Gamma(1/4)^4
gamma_power = gamma_value**4

# Calculate denominator 32*π
denominator = 32 * mp.pi

# Compute final result
result = gamma_power / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))