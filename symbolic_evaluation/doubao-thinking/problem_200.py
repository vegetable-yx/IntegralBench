import mpmath as mp

mp.dps = 15  # Set internal precision

# Initialize sum and variables for series expansion
series_sum = mp.mpf(0)
k = 0
term_tol = mp.mpf('1e-15')  # Term magnitude tolerance

while True:
    # Calculate alternating sign component
    sign = (-1) ** k
    
    # Calculate factorial component in denominator
    factorial_denom = mp.factorial(2 * k + 1)
    
    # Calculate gamma function components for integral part
    gamma_num = mp.gamma(k + mp.mpf('0.5'))
    gamma_denom = mp.gamma(k + 1)
    
    # Compute term for current k
    term = sign * (mp.sqrt(mp.pi) / 2) * gamma_num / (gamma_denom * factorial_denom)
    
    # Add term to series sum
    series_sum += term
    
    # Check convergence
    if mp.fabs(term) < term_tol:
        break
    
    k += 1

# Multiply by constant factor 2*sqrt(2)
result = 2 * mp.sqrt(2) * series_sum

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))