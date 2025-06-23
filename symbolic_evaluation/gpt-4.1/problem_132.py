import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Initialize the sum and tolerance
total = mp.mpf(0)
tol = mp.mpf('1e-15')
k = 0

# We'll iterate until terms become negligible or we reach a safe upper limit
max_iter = 10000  # Safe upper bound to prevent infinite loops

while k < max_iter:
    # Compute numerator: Gamma(k/2 + 1) * Gamma((k+3)/2)
    gamma1 = mp.gamma(k/2 + 1)
    gamma2 = mp.gamma((k + 3)/2)
    numerator = gamma1 * gamma2
    
    # Compute denominator components
    fact_k = mp.gamma(k + 1)      # k! = Gamma(k+1)
    gamma_k2 = mp.gamma(k + 2)    # Gamma(k+2)
    exp_term = mp.power(2, 2*k + 1)  # 2^(2k+1)
    gamma_k25 = mp.gamma(k + 2.5) # Gamma(k+2.5)
    
    denominator = fact_k * gamma_k2 * exp_term * gamma_k25
    
    # Calculate the term for current k
    term = numerator / denominator
    total += term
    
    # Check for convergence: break if term is below tolerance
    if mp.fabs(term) < tol:
        break
    
    k += 1

# Print the final result to 10 decimal places
print(mp.nstr(total, n=10))