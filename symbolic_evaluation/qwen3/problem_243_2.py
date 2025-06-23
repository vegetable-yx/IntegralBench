import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Compute numerator: Gamma(1/4)^4
numerator = gamma_1_4**4

# Compute denominator: 24 * π²
denominator = 24 * mp.pi**2

# Calculate final result
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))