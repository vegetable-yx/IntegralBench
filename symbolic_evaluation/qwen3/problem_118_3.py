import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Gamma(1/4)
gamma_value = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 4th power
gamma_power = gamma_value ** 4

# Calculate denominator 16π
denominator = 16 * mp.pi

# Compute final result by dividing gamma^4 by denominator
result = gamma_power / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))