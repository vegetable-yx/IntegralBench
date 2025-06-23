import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Precompute frequently used constants
ln2 = mp.log(2)
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithmic term: (1 + sqrt(2)) / 2
log_arg = (1 + sqrt2) / 2
log_term = mp.log(log_arg)

# Compute the four distinct arguments for the polylogarithm functions
arg1 = 1 - 1/sqrt2   # For Li₂(1 - 1/√2)
arg2 = 1 + 1/sqrt2   # For Li₂(1 + 1/√2)
arg3 = 0.5 - 1/sqrt2 # For Li₂(1/2 - 1/√2)
arg4 = 0.5 + 1/sqrt2 # For Li₂(1/2 + 1/√2)

# Calculate the polylogarithm terms
Li2_arg1 = mp.polylog(2, arg1)  # Li₂(1 - 1/√2)
Li2_arg2 = mp.polylog(2, arg2)  # Li₂(1 + 1/√2)
Li2_arg3 = mp.polylog(2, arg3)  # Li₂(1/2 - 1/√2)
Li2_arg4 = mp.polylog(2, arg4)  # Li₂(1/2 + 1/√2)

# Compute the five additive components of the main expression
term1 = 4 * ln2 * log_term
term2 = 2 * Li2_arg1
term3 = -2 * Li2_arg2
term4 = Li2_arg3
term5 = -Li2_arg4

# Combine all terms and multiply by 1/8
combined_terms = term1 + term2 + term3 + term4 + term5
result = combined_terms / 8

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))