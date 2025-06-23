import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter a (arbitrary value chosen for computation)
a = mp.mpf(1)

# Compute constants and Gamma functions
# Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
# Gamma(5/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)
# sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)

# Compute the coefficient: [sqrt(pi) * a * Gamma(3/4)] / [4 * Gamma(5/4)]
numerator = sqrt_pi * a * gamma_3_4
denominator = 4 * gamma_5_4
coefficient = numerator / denominator

# Compute the argument for the hypergeometric function: -a^2/4
arg = -(a**2) / 4

# Evaluate the generalized hypergeometric function _1F_2(1/2; 3/4, 5/4; arg)
hyper_term = mp.hyper([mp.mpf(1)/2], [mp.mpf(3)/4, mp.mpf(5)/4], arg)

# Multiply coefficient by hypergeometric term to get final result
result = coefficient * hyper_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))