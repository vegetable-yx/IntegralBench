import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

def compute_I(a):
    """
    Compute the series I(a) = \frac{\sqrt{\pi}}{2} \sum_{m=0}^{\infty} 
    \frac{\Gamma(m+2)}{(2m+3) \Gamma(m+5/2)} \frac{1}{(m!)^2} \left(\frac{a}{2}\right)^{2m}
    until terms are negligible (below 1e-15).
    """
    # Initialize the sum
    total = mp.mpf(0)
    m = 0
    # Precompute the constant factor: sqrt(pi)/2
    const = mp.sqrt(mp.pi) / 2
    # Tolerance for convergence (1e-15)
    tol = mp.mpf('1e-15')
    
    while True:
        # Compute gamma(m+2)
        gamma_m2 = mp.gamma(m + 2)
        # Compute gamma(m+5/2) = gamma(m + 2.5)
        gamma_m2p5 = mp.gamma(m + 2.5)
        # Compute gamma(m+1) for m! (since m! = gamma(m+1))
        gamma_m1 = mp.gamma(m + 1)
        # Compute (m!)^2
        m_fac_sq = gamma_m1 ** 2
        
        # Denominator: (2m+3) * gamma(m+5/2) * (m!)^2
        denom = (2*m + 3) * gamma_m2p5 * m_fac_sq
        # Power term: (a/2)^(2m)
        power_term = (a / 2) ** (2*m)
        
        # Compute the term for current m
        term = const * gamma_m2 / denom * power_term
        
        total += term
        
        # Check for convergence: break if term is below tolerance
        if mp.fabs(term) < tol:
            break
            
        m += 1
        
    return total

# Compute I(a) for a = 1.0
a_val = mp.mpf('1.0')
result = compute_I(a_val)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))