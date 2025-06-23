import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Calculate numerator: Gamma(1/4) raised to the 8th power
numerator = gamma_1_4**8

# Calculate denominator components
pi_squared = mp.pi**2
denominator = 6144 * pi_squared

# Compute final result by dividing numerator by denominator
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))