import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize sum and tolerance
s = mp.mpf(0)
tol = mp.mpf('1e-15')
k = 0
term = mp.mpf(1)  # Initialize term to start loop

# Sum the series until terms become negligible
while abs(term) > tol:
    # Compute numerator: Γ(k/2 + 1) * Γ((k+3)/2)
    gamma1 = mp.gamma(k/2 + 1)
    gamma2 = mp.gamma((k + 3)/2)
    numerator = gamma1 * gamma2
    
    # Compute denominator components
    fact_k = mp.factorial(k)           # k!
    gamma_k2 = mp.gamma(k + 2)          # Γ(k+2)
    power_term = mp.power(2, 2*k + 1)  # 2^(2k+1)
    gamma_k52 = mp.gamma(k + 5/2)       # Γ(k+5/2)
    
    denominator = fact_k * gamma_k2 * power_term * gamma_k52
    
    # Compute current term and add to sum
    term = numerator / denominator
    s += term
    
    # Move to next term
    k += 1
    
    # Safeguard against slow convergence
    if k > 10000:
        break

# Print the result to 10 decimal places
print(mp.nstr(s, n=10))