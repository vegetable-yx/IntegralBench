import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum to zero
s = mp.mpf(0)
k = 0
tolerance = mp.mpf('1e-20')  # Convergence tolerance
max_iter = 1000  # Maximum number of iterations to prevent infinite loops

# Sum the series until terms become negligible
while k < max_iter:
    # Convert integer k to mpmath float for precise gamma function arguments
    kf = mp.mpf(k)
    
    # Compute arguments for the gamma functions in the numerator
    arg1 = kf/2 + 1
    arg2 = (kf + 3)/2
    
    # Evaluate gamma functions for the numerator
    gamma1 = mp.gamma(arg1)
    gamma2 = mp.gamma(arg2)
    numerator = gamma1 * gamma2
    
    # Compute denominator components
    fact_k = mp.factorial(k)       # k!
    fact_k1 = mp.factorial(k+1)    # (k+1)!
    exp_term = 2**(2*k + 1)        # 2^(2k+1)
    
    # Assemble denominator: k! * [(k+1)!]^2 * 2^(2k+1)
    denom = fact_k * (fact_k1**2) * exp_term
    
    # Compute the current term in the series
    term = numerator / denom
    
    # Add term to the sum
    s += term
    
    # Check for convergence (term magnitude below tolerance)
    if mp.fabs(term) < tolerance:
        break
    
    k += 1

# Print the final result to exactly 10 decimal places
print(mp.nstr(s, n=10))