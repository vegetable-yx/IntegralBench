import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum to zero
s = mp.mpf(0)

# Precompute constant sqrt(2) for efficiency
sqrt2 = mp.sqrt(2)

# Tolerance for convergence (1e-15) and maximum terms to avoid infinite loops
tol = mp.mpf('1e-15')
max_terms = 1000

# Main summation loop
for m in range(max_terms + 1):
    # Arguments for the Beta function
    a = (m + 1) / 2
    b = (m + 2) / 2
    
    # Compute the Beta function value
    term_beta = mp.beta(a, b)
    
    # Denominator components:
    # 2^{(2m+1)/2} = 2^{m + 0.5} = 2^m * sqrt(2)
    pow2 = mp.power(2, m) * sqrt2
    fact_m = mp.factorial(m)
    fact_m1 = mp.factorial(m + 1)
    denominator = pow2 * fact_m * fact_m1
    
    # Current term value
    term = term_beta / denominator
    
    # Add term to the sum
    s += term
    
    # Check for convergence: break if term is below tolerance
    if mp.fabs(term) < tol:
        break

# Print the result to exactly 10 decimal places
print(mp.nstr(s, n=10))