import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum
total = mp.mpf(0)
# Tolerance for convergence (1e-20 for high precision)
tolerance = mp.mpf('1e-20')
# Maximum number of terms to prevent infinite loops
max_n = 10000

# Iterate over terms until convergence or max_n
for n in range(0, max_n + 1):
    # Compute Gamma((n+3)/2)
    gamma1 = mp.gamma((n + 3) / 2)
    # Compute Gamma(n/2 + 1)
    gamma2 = mp.gamma(n/2 + 1)
    # Compute Gamma(n+3)
    gamma3 = mp.gamma(n + 3)
    
    # Compute the term: (n+1) * [Gamma((n+3)/2) * Gamma(n/2+1)] / Gamma(n+3)
    term = (n + 1) * gamma1 * gamma2 / gamma3
    
    # Add the term to the total sum
    total += term
    
    # Check if the term is below the tolerance to break early
    if mp.fabs(term) < tolerance:
        break

# Print the result to 10 decimal places
print(mp.nstr(total, n=10))