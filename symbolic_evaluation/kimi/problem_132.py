import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate gamma functions components
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)
gamma_2 = mp.gamma(2)  # This equals 1! = 1

# Compute the gamma product term
gamma_term = (gamma_3_4 * gamma_5_4) / gamma_2

# Calculate the confluent hypergeometric function 1F1(1; 2; 1/4)
hypergeom_term = mp.hyp1f1(1, 2, mp.mpf(1)/4)

# Combine components for final result
result = gamma_term * hypergeom_term

# Print with 10 decimal precision
print(mp.nstr(result, n=10))