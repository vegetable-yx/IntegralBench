import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression
sqrt_2 = mp.sqrt(2)  # Compute √2
pi_power = mp.pi ** (3/2)  # Compute π^(3/2)

# Calculate Gamma(1/4) and its square
gamma_1_4 = mp.gamma(mp.mpf(1)/4)  # Compute Γ(1/4)
gamma_squared = gamma_1_4 ** 2  # Square the Gamma value

# Combine components to get final result
numerator = sqrt_2 * pi_power
result = numerator / gamma_squared

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))