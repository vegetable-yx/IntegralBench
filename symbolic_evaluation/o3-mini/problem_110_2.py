import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma functions
gamma_3_4 = mp.gamma(mp.mpf(3)/4)  # Gamma(3/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)  # Gamma(5/4)

# Calculate the constant factor: sqrt(pi) * Gamma(3/4) / (2 * Gamma(5/4))
constant_factor = (mp.sqrt(mp.pi) * gamma_3_4) / (2 * gamma_5_4)

# Compute the hypergeometric function 2F1(-1/2, 1/4; 5/4; 1/4)
hyp_val = mp.hyp2f1(mp.mpf(-1)/2, mp.mpf(1)/4, mp.mpf(5)/4, mp.mpf(1)/4)

# Multiply constant factor by hypergeometric value
result = constant_factor * hyp_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))