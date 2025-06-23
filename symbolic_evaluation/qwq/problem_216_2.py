import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute π^(3/2)
pi_power = mp.power(mp.pi, 1.5)

# Compute 2^(3/4)
two_power = mp.power(2, 0.75)

# Compute Gamma(3/4)
gamma_val = mp.gamma(0.75)

# Calculate denominator: 2^(3/4) * Gamma(3/4)
denominator = two_power * gamma_val

# Final result: π^(3/2) divided by denominator
result = pi_power / denominator

print(mp.nstr(result, n=10))