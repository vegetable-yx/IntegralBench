import mpmath as mp

# Set internal decimal places for intermediate calculations
mp.dps = 15

# Calculate numerator: [Gamma(1/4)]^4
gamma_val = mp.gamma(mp.mpf('0.25'))
gamma_power = gamma_val**4

# Calculate denominator: 64 * sqrt(2 * pi)
denom_part = mp.sqrt(2 * mp.pi)
denominator = 64 * denom_part

# Final result: numerator / denominator
result = gamma_power / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))