import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum
total = mp.mpf(0)
k = 1
tolerance = mp.mpf('1e-20')  # Term magnitude stopping criterion
max_terms = 1000000  # Prevent infinite loops

while k <= max_terms:
    # Compute arguments for beta function
    a_arg = (k + mp.mpf('1.5')) / 2
    b_arg = (k + mp.mpf('0.5')) / 2
    
    # Compute beta(a, b) = Gamma(a)*Gamma(b)/Gamma(a+b)
    beta_val = mp.beta(a_arg, b_arg)
    
    # Compute current term: beta(a,b) / k^2
    term = beta_val / (k * k)
    
    # Add term to total
    total += term
    
    # Check convergence (term positive, so no abs needed)
    if term < tolerance:
        break
    
    k += 1

# Print result to exactly 10 decimal places
print(mp.nstr(total, n=10))