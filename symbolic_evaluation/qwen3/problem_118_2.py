import mpmath as mp
mp.dps = 15  # Set decimal places for calculations

# Compute Gamma(1/4)
gamma_value = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the fourth power
gamma_power = gamma_value**4

# Calculate denominator 16*pi
denominator = 16 * mp.pi

# Compute final result
result = gamma_power / denominator

# Print with 10 decimal precision
print(mp.nstr(result, n=10))