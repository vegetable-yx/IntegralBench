import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Gamma(1/4) and square it
gamma_1_4 = mp.gamma(mp.mpf(1)/4)
gamma_1_4_sq = gamma_1_4 ** 2

# Compute 2^(3/4) using mpmath power function
two_power = mp.power(2, mp.mpf(3)/4)

# Compute Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Calculate numerator (pi * Gamma(1/4)^2)
numerator = mp.pi * gamma_1_4_sq

# Calculate denominator (2^(3/4) * Gamma(3/4))
denominator = two_power * gamma_3_4

# Compute final result
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))