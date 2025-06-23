import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate each component separately
# Square root of 2
sqrt2 = mp.sqrt(2)

# Gamma function at 3/4
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Gamma function at 5/4
gamma_5_4 = mp.gamma(mp.mpf(5)/4)

# Hypergeometric function 1F2 with parameters:
# a = 1/2, b1 = 3/4, b2 = 5/4, z = -1/2
hyp = mp.hyper([mp.mpf(1)/2], [mp.mpf(3)/4, mp.mpf(5)/4], mp.mpf(-1)/2)

# Combine all components
result = sqrt2 * gamma_3_4 * gamma_5_4 * hyp

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))