import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^(3/2)
pi_power = mp.pi ** (3/2)

# Calculate Gamma(1/4) and square it
gamma_1_4 = mp.gamma(mp.mpf(1)/4)
gamma_1_4_sq = gamma_1_4 ** 2

# Calculate Gamma(3/4) and square it
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_3_4_sq = gamma_3_4 ** 2

# Compute the hypergeometric function 2F1(-1/2, 1/4; 3/4; 1/4)
hyp_val = mp.hyp2f1(mp.mpf(-1)/2, mp.mpf(1)/4, mp.mpf(3)/4, mp.mpf(1)/4)

# Calculate the numerator: pi^(3/2) * [Gamma(1/4)]^2
numerator = pi_power * gamma_1_4_sq

# Calculate the denominator: 32 * [Gamma(3/4)]^2
denominator = 32 * gamma_3_4_sq

# Compute the fraction: numerator / denominator
fraction = numerator / denominator

# Multiply by the hypergeometric function to get the final result
result = fraction * hyp_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))