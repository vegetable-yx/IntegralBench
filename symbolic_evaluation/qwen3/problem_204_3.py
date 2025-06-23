import mpmath as mp
mp.dps = 15

result = mp.mpf(0)
tolerance = mp.mpf('1e-15')

for n in range(1000):
    # Calculate alternating sign component
    sign = (-1) ** n
    
    # Compute factorial denominator for Taylor series
    factorial_denom = mp.factorial(2 * n + 1)
    
    # Calculate coefficient for current term
    coeff = sign / factorial_denom
    
    # Compute parameters for beta function
    a_param = (2 * n + 7) / mp.mpf(4)
    b_param = (2 * n + 5) / mp.mpf(4)
    
    # Evaluate beta function using mpmath
    beta_val = mp.beta(a_param, b_param)
    
    # Compute scaling factor with 2^(n+2)
    scale_factor = mp.power(2, n + 2)
    
    # Calculate complete term for current n
    term = coeff * scale_factor * beta_val
    
    # Add term to cumulative result
    result += term
    
    # Check if term magnitude drops below precision threshold
    if mp.fabs(term) < tolerance:
        break

print(mp.nstr(result, n=10))