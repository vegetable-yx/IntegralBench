import mpmath as mp

mp.dps = 15  # Set internal decimal places for precision

# Calculate numerator: π^(3/2)
pi_power = mp.pi ** (3/2)

# Calculate denominator components
two_power = mp.mpf(2) ** (5/2)        # 2^(5/2)
gamma_val = mp.gamma(mp.mpf(3)/4)     # Γ(3/4)

# Combine denominator components
denominator = two_power * gamma_val

# Compute final result
result = pi_power / denominator

# Print with 10 decimal precision
print(mp.nstr(result, n=10))