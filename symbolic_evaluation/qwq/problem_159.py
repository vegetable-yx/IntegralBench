import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate each component of the expression
sqrt2 = mp.sqrt(2)
eight_sqrt2 = 8 * sqrt2  # 8√2

pi_pow = mp.pi ** 1.5  # π^(3/2)

gamma_14 = mp.gamma(mp.mpf(1)/4)  # Γ(1/4)
gamma_14_squared = gamma_14 ** 2  # Γ(1/4)^2

gamma_12 = mp.gamma(mp.mpf(1)/2)  # Γ(1/2)

# Combine all components according to the formula
result = (eight_sqrt2 * pi_pow * gamma_14_squared) / gamma_12

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))