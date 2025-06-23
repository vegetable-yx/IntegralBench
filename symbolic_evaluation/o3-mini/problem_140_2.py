import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma functions separately
gamma_34 = mp.gamma(3/4)
gamma_114 = mp.gamma(11/4)
gamma_74 = mp.gamma(7/4)
gamma_134 = mp.gamma(13/4)

# Compute sqrt(pi) once
sqrt_pi = mp.sqrt(mp.pi)

# Compute the two hypergeometric functions
hyp2f1_term1 = mp.hyp2f1(-0.5, 0.25, 11/4, 4)
hyp2f1_term2 = mp.hyp2f1(-0.5, 0.75, 13/4, 4)

# Calculate the first term: sqrt(pi) * Gamma(3/4) / (8 * Gamma(11/4)) * hyp2f1_term1
term1 = (sqrt_pi * gamma_34) / (8 * gamma_114) * hyp2f1_term1

# Calculate the second term: sqrt(pi) * Gamma(7/4) / (8 * Gamma(13/4)) * hyp2f1_term2
term2 = (sqrt_pi * gamma_74) / (8 * gamma_134) * hyp2f1_term2

# Combine terms and multiply by 16
result = 16 * (term1 - term2)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))