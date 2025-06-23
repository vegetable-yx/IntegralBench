import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root term sqrt(6π)/4
sqrt_6pi = mp.sqrt(6 * mp.pi)
sqrt_term = sqrt_6pi / 4

# Calculate the ratio of Gamma functions Γ(3/4)/Γ(5/4)
gamma_num = mp.gamma(mp.mpf(3)/4)
gamma_den = mp.gamma(mp.mpf(5)/4)
gamma_ratio = gamma_num / gamma_den

# Calculate the hypergeometric function 1F2(3/4; 5/4, 1/2; 9/4)
hypergeom = mp.hyper([mp.mpf(3)/4], [mp.mpf(5)/4, mp.mpf(1)/2], mp.mpf(9)/4)

# Combine all components to get the final result
result = sqrt_term * gamma_ratio * hypergeom

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))