import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Precompute constant factor: π²/4
pi_sq_over_4 = mp.pi**2 / 4

# Initialize sum
total = mp.mpf(0)

# Set bounds and threshold for early termination
n_max = 100
m_max = 100
threshold = mp.mpf('1e-30')

# Compute double sum
for n in range(0, n_max + 1):
    # Precompute factorial for n and (2n)!
    fac_n = mp.factorial(n)
    fac_2n = mp.factorial(2*n)
    
    for m in range(0, m_max + 1):
        # Precompute factorial for m, (2m)!, and (n+m+1)!
        fac_m = mp.factorial(m)
        fac_2m = mp.factorial(2*m)
        fac_nm = mp.factorial(n + m + 1)
        
        # Compute sign: (-1)^m
        sign = mp.mpf(-1)**m
        
        # Numerator: [(2n)!]^2 * [(2m)!]^2 * (-1)^m
        numerator = (fac_2n**2) * (fac_2m**2) * sign
        
        # Denominator: 2^(6n+4m) * (n!)^2 * (m!)^2 * (2m+1) * (n+m+1)!
        power_term = mp.power(2, 6*n + 4*m)
        fac_term = (fac_n**2) * (fac_m**2) * (2*m + 1) * fac_nm
        denominator = power_term * fac_term
        
        # Term value
        term = numerator / denominator
        total += term
        
        # Check for early termination in m-loop if term is negligible
        if m >= 5 and mp.fabs(term) < threshold:
            break
    
    # Optional: Check if the last term for this n was negligible and break outer loop?
    # Not implemented for safety; rely on n_max

# Multiply by constant factor
result = pi_sq_over_4 * total

# Print result to 10 decimal places
print(mp.nstr(result, n=10))