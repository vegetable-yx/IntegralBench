import mpmath as mp

# Set the decimal places for internal precision
mp.dps = 15

# Compute Gamma(1/4) squared
gamma_term = mp.gamma(1/4)
gamma_sq = gamma_term ** 2

# Compute the hypergeometric function _2F_1(-1/2, 1/4; 3/4; 1/4)
hyp2f1_term = mp.hyp2f1(-0.5, 0.25, 0.75, 0.25)

# Calculate the constant factor: 2 * sqrt(2) / (3 * sqrt(pi))
constant_factor = (2 * mp.sqrt(2)) / (3 * mp.sqrt(mp.pi))

# Multiply the components together: constant_factor * gamma_sq * hyp2f1_term
result = constant_factor * gamma_sq * hyp2f1_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))