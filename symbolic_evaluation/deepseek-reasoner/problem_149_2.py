import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate numerator: π^(3/2)
pi_power = mp.pi ** (3/2)

# Calculate denominator components
two_power = 2 ** (1/4)          # 2^(1/4)
gamma_term = mp.gamma(1/4)      # Γ(1/4)
gamma_squared = gamma_term ** 2 # Γ(1/4)^2

# Combine denominator components
denominator = two_power * gamma_squared

# Compute final result
result = pi_power / denominator

# Print result to 10 decimal places
print(mp.nstr(result, n=10))