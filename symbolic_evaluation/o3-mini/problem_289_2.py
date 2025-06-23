import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (example value, can be changed)
a = 1.0

# Compute constants and gamma functions
sqrt_pi = mp.sqrt(mp.pi)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Square the gamma values
gamma_1_4_sq = gamma_1_4**2
gamma_3_4_sq = gamma_3_4**2

# Compute the argument for the hypergeometric functions
arg = -a**2 / 4

# Calculate hypergeometric functions
# _1F_2(3/4; 3/2, 5/4; -a^2/4)
hyp1 = mp.hyper([mp.mpf(3)/4], [mp.mpf(3)/2, mp.mpf(5)/4], arg)

# _1F_2(1/4; 1/2, 3/4; -a^2/4)
hyp2 = mp.hyper([mp.mpf(1)/4], [mp.mpf(1)/2, mp.mpf(3)/4], arg)

# Compute the expression inside the brackets
bracket_expr = gamma_1_4_sq * hyp1 - gamma_3_4_sq * hyp2

# Calculate the prefactor: a/(8*sqrt(pi))
prefactor = a / (8 * sqrt_pi)

# Compute the final result
result = prefactor * bracket_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))