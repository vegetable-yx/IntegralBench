import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum
result = mp.mpf(0)
# Tolerance for convergence
tol = mp.mpf('1e-15')
k = 0

while True:
    # Calculate Gamma((k+1)/2)
    gamma1 = mp.gamma((k + 1) / 2)
    
    # Calculate Gamma(1 + k/2)
    gamma2 = mp.gamma(1 + k / 2)
    
    # Calculate k! (factorial)
    fact_k = mp.factorial(k)
    
    # Calculate Gamma(k+2)
    gamma_k2 = mp.gamma(k + 2)
    
    # Calculate Gamma((2k+3)/2)
    gamma_denom = mp.gamma((2*k + 3) / 2)
    
    # Compute denominator: k! * Gamma(k+2) * Gamma((2k+3)/2)
    denominator = fact_k * gamma_k2 * gamma_denom
    
    # Compute the term: [Gamma((k+1)/2) * Gamma(1+k/2) * 2^{-k}] / denominator
    term = (gamma1 * gamma2 * mp.power(2, -k)) / denominator
    
    # Check for convergence
    if mp.fabs(term) < tol:
        break
        
    # Add term to result
    result += term
    k += 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))