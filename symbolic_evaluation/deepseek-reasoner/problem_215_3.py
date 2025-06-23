import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate gamma function values
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_3_2 = mp.gamma(mp.mpf(3)/2)

# Compute the squared gamma(3/4) term
gamma_squared = gamma_3_4 ** 2

# Calculate the first part of the expression
gamma_ratio = gamma_squared / gamma_3_2

# Compute the hypergeometric function {}_1F_2
hypergeom = mp.hyper([mp.mpf(3)/4], [mp.mpf(1)/2, mp.mpf(5)/4], -mp.mpf(1)/16)

# Combine components for final result
result = gamma_ratio * hypergeom

# Print with 10 decimal precision
print(mp.nstr(result, n=10))