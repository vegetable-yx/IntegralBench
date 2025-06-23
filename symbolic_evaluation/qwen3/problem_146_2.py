import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Calculate Gamma(1/4)^4
gamma_power = gamma_val**4

# Compute the denominator components
sqrt_2pi = mp.sqrt(2 * mp.pi)
denominator = 8 * sqrt_2pi

# Final result calculation
result = gamma_power / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))