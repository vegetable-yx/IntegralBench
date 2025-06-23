import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant expression inside the Gamma and Psi functions
a = 11 + mp.sqrt(120)

# Calculate the two arguments for Gamma and Psi functions
arg1 = (a + 1) / 4
arg2 = (a + 3) / 4

# Compute Gamma ratio: Gamma(arg1) / Gamma(arg2)
gamma_ratio = mp.gamma(arg1) / mp.gamma(arg2)

# Compute the difference of digamma functions: Psi(arg2) - Psi(arg1)
digamma_diff = mp.digamma(arg2) - mp.digamma(arg1)

# Compute the second term: sqrt(pi)/4 * Gamma_ratio * digamma_diff
term2 = (mp.sqrt(mp.pi) / 4) * gamma_ratio * digamma_diff

# Compute the first term: pi/8
term1 = mp.pi / 8

# Sum both terms
result = term1 + term2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))