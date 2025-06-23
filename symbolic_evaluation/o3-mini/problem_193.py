import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define constants
sqrt2 = mp.sqrt(2)  # square root of 2
alpha = 1 + sqrt2   # (1 + sqrt(2))
beta = (sqrt2 - 1)**2  # (sqrt(2) - 1)^2

# Precompute logarithmic term: ln(1 + sqrt(2))
log_term = mp.log(alpha)

# Compute the polylogarithm terms
Li2_beta = mp.polylog(2, beta)           # Li_2(beta)
Li3_beta = mp.polylog(3, beta)           # Li_3(beta)
Li3_neg_beta = mp.polylog(3, -beta)      # Li_3(-beta)

# Compute each term in the expression
term1 = 4 * mp.pi * log_term**3
term2 = -12 * log_term * Li2_beta
term3 = 6 * Li3_beta
term4 = -6 * Li3_neg_beta

# Sum all terms and divide by 24
result = (term1 + term2 + term3 + term4) / 24

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))