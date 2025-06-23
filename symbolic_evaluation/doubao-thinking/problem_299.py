import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate individual gamma functions
gamma_1_4 = mp.gamma(mp.mpf(1)/4)  # Gamma(1/4)
gamma_1_2 = mp.gamma(mp.mpf(1)/2)  # Gamma(1/2) = sqrt(pi)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)  # Gamma(3/4)

# Compute the numerator and denominator
numerator = 2 * mp.pi * gamma_1_4 * gamma_1_2
denominator = gamma_3_4

# Calculate the final result
result = numerator / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))