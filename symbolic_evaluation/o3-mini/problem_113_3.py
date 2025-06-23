import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant terms: sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)

# Calculate gamma(1/4) and raise to the third power
gamma_1_4 = mp.gamma(mp.mpf(1)/4)
gamma_1_4_cubed = gamma_1_4**3

# Calculate gamma(3/4) and raise to the second power
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_3_4_squared = gamma_3_4**2

# Compute the fraction: (sqrt(pi) * [gamma(1/4)]^3) / (16 * [gamma(3/4)]^2)
numerator = sqrt_pi * gamma_1_4_cubed
denominator = 16 * gamma_3_4_squared
fraction = numerator / denominator

# Calculate the hypergeometric function _3F_2(1/4, 1/4, 1; 3/4, 3/4; 1)
hyp = mp.hyp3f2(mp.mpf(1)/4, mp.mpf(1)/4, 1, mp.mpf(3)/4, mp.mpf(3)/4, 1)

# Multiply the fraction by the hypergeometric result
result = fraction * hyp

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))