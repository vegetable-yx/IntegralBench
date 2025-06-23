import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum
total = mp.mpf(0)
k = 0
# Tolerance for convergence (absolute error less than 1e-20)
tol = mp.mpf('1e-20')
max_terms = 1000  # Maximum number of terms to prevent infinite loops

while k < max_terms:
    # Precompute k! for efficiency
    k_factorial = mp.factorial(k)
    
    # Compute the base term: 2 * (1/2)^k / (k!)^2
    base_term = mp.mpf(2) * (mp.mpf('0.5')**k) / (k_factorial**2)
    
    # Compute gamma function arguments
    arg1 = mp.mpf('3/4') + mp.mpf(k)/2  # \frac{3}{4} + \frac{k}{2}
    arg2 = mp.mpf('5/4') + mp.mpf(k)/2  # \frac{5}{4} + \frac{k}{2}
    
    # Compute gamma products: Γ(arg1) * Γ(arg2)
    gamma_prod = mp.gamma(arg1) * mp.gamma(arg2)
    
    # Compute denominator: Γ(2 + k)
    denom = mp.gamma(2 + k)
    
    # Compute current term: base_term * gamma_prod / denom
    term = base_term * gamma_prod / denom
    
    # Add term to total
    total += term
    
    # Check for convergence: if term is below tolerance, break
    if mp.fabs(term) < tol:
        break
    
    k += 1

# Print the result to exactly 10 decimal places
print(mp.nstr(total, n=10))