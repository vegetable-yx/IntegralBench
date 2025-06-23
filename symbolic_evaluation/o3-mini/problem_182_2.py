import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the golden ratio conjugate and related constants
sqrt5 = mp.sqrt(5)
phi = (1 + sqrt5) / 2  # Golden ratio
phi_conjugate = (1 - sqrt5) / 2  # Conjugate of the golden ratio

# Compute the logarithm term: π * ln( (√5 + 1)/2 )
log_arg = phi  # This is (√5 + 1)/2
log_term = mp.pi * mp.log(log_arg)

# Compute the two dilogarithm terms
dilog_term1 = mp.polylog(2, phi_conjugate)  # Li₂( (1 - √5)/2 )
dilog_term2 = mp.polylog(2, phi)            # Li₂( (1 + √5)/2 )

# Combine terms: π*ln(...) + Li₂(conjugate) - Li₂(phi)
combined_terms = log_term + dilog_term1 - dilog_term2

# Multiply by 1/2 to get the final result
result = 0.5 * combined_terms

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))