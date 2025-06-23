import mpmath as mp

mp.dps = 15  # Set decimal precision to 15 digits

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Compute Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Calculate numerator components: π * [Γ(1/4)]²
pi_times_gamma_sq = mp.pi * (gamma_1_4 ** 2)

# Calculate denominator components: 2^(7/2) * [Γ(3/4)]²
two_power = 2 ** (mp.mpf(7)/2)
denominator = two_power * (gamma_3_4 ** 2)

# Compute the final result
result = pi_times_gamma_sq / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))