import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Compute numerator: [Gamma(1/4)]^4
numerator = gamma_val**4

# Compute denominator: 32 * sqrt(2 * pi)
denominator = 32 * mp.sqrt(2 * mp.pi)

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))