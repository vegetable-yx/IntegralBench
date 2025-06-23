import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute the difference of digamma functions
psi_diff = mp.psi(mp.mpf('3/4')) - mp.psi(mp.mpf('1/4'))

# Compute the argument for the logarithm
log_arg = (mp.sqrt(2) + 1) / 2

# Compute the logarithmic term
log_term = 2 * mp.log(log_arg)

# Combine the digamma difference and logarithmic term
combined_terms = psi_diff + log_term

# Compute the constant multiplicative factor
factor = mp.pi * mp.sqrt(2) / 4

# Compute the final result
result = factor * combined_terms

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))