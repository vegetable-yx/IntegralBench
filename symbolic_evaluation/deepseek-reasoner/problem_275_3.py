import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate common components
sqrt3 = mp.sqrt(3)
sqrt_pi = mp.sqrt(mp.pi)

# Compute exponential terms
exp_3 = mp.exp(3)
exp_neg3 = mp.exp(-3)

# Compute special functions
erf_term = mp.erf(sqrt3)
erfi_term = mp.erfi(sqrt3)

# Calculate each term of the expression
term1 = (mp.mpf(3)/4) * sqrt_pi * exp_3 * erf_term
term2 = (mp.mpf(3)/4) * sqrt_pi * exp_neg3 * erfi_term

# Combine terms for final result
result = term1 + term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))