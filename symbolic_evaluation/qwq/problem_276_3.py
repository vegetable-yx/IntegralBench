import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate sqrt(3) to use in erf and erfi functions
sqrt3 = mp.sqrt(3)

# Compute exponential terms e^3 and e^-3
exp_3 = mp.exp(3)
exp_minus3 = mp.exp(-3)

# Calculate error functions erf(sqrt(3)) and erfi(sqrt(3))
erf_term = mp.erf(sqrt3)
erfi_term = mp.erfi(sqrt3)

# Compute the two main terms in the summation
term1 = exp_3 * erf_term
term2 = exp_minus3 * erfi_term

# Sum the terms and multiply by sqrt(pi)/2
sum_terms = term1 + term2
result = (sqrt_pi / 2) * sum_terms

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))