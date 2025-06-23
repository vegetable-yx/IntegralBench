import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate gamma(1/4) and gamma(3/4) once for reuse
gamma_1_4 = mp.gamma(1/4)
gamma_3_4 = mp.gamma(3/4)

# Compute common factor: gamma(1/4) / gamma(3/4)
gamma_ratio = gamma_1_4 / gamma_3_4

# Calculate the first term: (π^{3/2} * gamma_ratio) / 16
pi_sqrt = mp.sqrt(mp.pi)  # sqrt(π)
pi_3_2 = mp.pi * pi_sqrt  # π^{3/2}
term1 = (pi_3_2 * gamma_ratio) / 16

# Compute the hypergeometric function: _2F_1(-1/2, 1/4; 3/4; 1/2)
hyp_val = mp.hyp2f1(-0.5, 0.25, 0.75, 0.5)

# Calculate the second term: (sqrt(π) * gamma_ratio) / 8 * hyp_val
term2 = (pi_sqrt * gamma_ratio) / 8 * hyp_val

# Sum the two terms
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))