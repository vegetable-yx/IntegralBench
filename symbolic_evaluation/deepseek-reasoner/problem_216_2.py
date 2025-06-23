import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute each component of the expression separately
sqrt_pi = mp.sqrt(mp.pi)  # Calculate square root of pi
gamma_14 = mp.gamma(mp.mpf(1)/4)  # Compute Gamma(1/4)
hyp_term = mp.hyp1f2(mp.mpf(1)/4, mp.mpf(1)/2, mp.mpf(3)/4, -1)  # Hypergeometric function 1F2

# Combine components to get final result
result = sqrt_pi * gamma_14 * hyp_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))