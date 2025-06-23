import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a' (value chosen arbitrarily as 1.0)
a = 1.0

# Compute a squared and scaled argument for hypergeometric functions
a_sq = a**2
z = a_sq / 16

# Compute fundamental constants: sqrt(pi) and gamma functions
sqrt_pi = mp.sqrt(mp.pi)
gamma_34 = mp.gamma(mp.mpf(3)/4)  # Gamma(3/4)
gamma_54 = mp.gamma(mp.mpf(5)/4)  # Gamma(5/4)

# Precompute common factors for the first term
numerator1 = sqrt_pi * gamma_34**2
denominator1 = 8 * gamma_54
factor1 = numerator1 / denominator1

# Compute the first hypergeometric function: _1F_2(1; 3/4, 5/4; z)
hyp1 = mp.hyp1f2(1, [mp.mpf(3)/4, mp.mpf(5)/4], z)
term1 = factor1 * hyp1

# Precompute common factors for the second term
numerator2 = a_sq * gamma_54**2
denominator2 = 8 * sqrt_pi
factor2 = numerator2 / denominator2

# Compute the second hypergeometric function: _1F_2(1; 5/4, 3/2; z)
hyp2 = mp.hyp1f2(1, [mp.mpf(5)/4, mp.mpf(3)/2], z)
term2 = factor2 * hyp2

# Combine terms to get final result
result = term1 - term2

# Print result to 10 decimal places
print(mp.nstr(result, n=10))