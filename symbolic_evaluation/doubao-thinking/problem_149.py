import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π^(3/2)
pi_power = mp.pi ** (3/2)

# Calculate Γ(1/4)
gamma_1_4 = mp.gamma(1/4)

# Calculate numerator: π^(3/2) * Γ(1/4)
numerator = pi_power * gamma_1_4

# Calculate 2^(3/4)
two_power = 2 ** (3/4)

# Calculate Γ(3/4)
gamma_3_4 = mp.gamma(3/4)

# Calculate denominator: 2^(3/4) * Γ(3/4)
denominator = two_power * gamma_3_4

# Compute final result by dividing numerator by denominator
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))