import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the value of 'a' (can be changed as needed)
a = mp.mpf(1)

# Precompute common constants
gamma_14 = mp.gamma(mp.mpf(1)/4)
gamma_34 = mp.gamma(mp.mpf(3)/4)
sqrt_pi = mp.sqrt(mp.pi)

# Compute the argument for hypergeometric functions
z = -a**2 / 16

# Calculate coefficients for the first term
coeff1 = 2 * gamma_14**2 / sqrt_pi

# Compute the first hypergeometric function: _1F_2(1; 3/4, 5/4; z)
hyp1 = mp.hyp1f2(1, [mp.mpf(3)/4, mp.mpf(5)/4], z)

# Calculate the first term
term1 = coeff1 * hyp1

# Calculate coefficients for the second term
coeff2 = a * gamma_34**2 / (4 * sqrt_pi)

# Compute the second hypergeometric function: _1F_2(3/2; 5/4, 7/4; z)
hyp2 = mp.hyp1f2(mp.mpf(3)/2, [mp.mpf(5)/4, mp.mpf(7)/4], z)

# Calculate the second term
term2 = coeff2 * hyp2

# Combine terms for final result
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))