import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Compute Gamma(5/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)

# Calculate the constant factor: (9/4) * Gamma(3/4) * Gamma(5/4)
const_factor = (mp.mpf(9)/4) * gamma_3_4 * gamma_5_4

# Compute the hypergeometric function {}_1F_2(1/2; 3/4, 5/4; 1/16)
hyp = mp.hyper([mp.mpf(1)/2], [mp.mpf(3)/4, mp.mpf(5)/4], mp.mpf(1)/16)

# Multiply constant factor by hypergeometric result
result = const_factor * hyp

# Print final result to 10 decimal places
print(mp.nstr(result, n=10))