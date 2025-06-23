import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute the gamma functions needed
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)

# Compute the two hypergeometric functions
hyp1 = mp.hyp2f1(mp.mpf(-1)/2, mp.mpf(1)/4, mp.mpf(5)/4, mp.mpf(1)/16)
hyp2 = mp.hyp2f1(mp.mpf(-1)/2, mp.mpf(1)/4, mp.mpf(3)/4, mp.mpf(1)/16)

# Compute the constant factor: sqrt(pi) * Gamma(3/4) / (64 * Gamma(5/4))
sqrt_pi = mp.sqrt(mp.pi)
factor = (sqrt_pi * gamma_3_4) / (64 * gamma_5_4)

# Compute the two terms
term1 = factor * hyp1
term2 = (mp.mpf(1)/32) * hyp2

# Combine terms to get the final result
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))