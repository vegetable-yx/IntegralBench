import mpmath as mp

# Set internal decimal places for sufficient precision
mp.dps = 15

# Compute Γ(1/4)
gamma_quarter = mp.gamma(mp.mpf(1)/4)

# Raise Γ(1/4) to the 8th power
gamma_quarter_power8 = gamma_quarter**8

# Compute π squared
pi_squared = mp.pi**2

# Calculate denominator: 512 * π²
denominator = 512 * pi_squared

# Final result: (Γ(1/4)^8) / (512π²)
result = gamma_quarter_power8 / denominator

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))