import mpmath as mp
mp.dps = 15

# Calculate Beta function B(1/4, 1/2)
beta_value = mp.beta(1/4, 1/2)

# Calculate the logarithmic and pi terms
pi_term = 3 * mp.pi / 2
log_term = mp.log(2)
combined_terms = pi_term + log_term

# Compute final result
result = 2 * beta_value * combined_terms

print(mp.nstr(result, n=10))