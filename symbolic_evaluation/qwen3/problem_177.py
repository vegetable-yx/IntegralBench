import mpmath as mp

mp.dps = 15  # Set internal precision

sum_total = mp.mpf(0)
n = 0
max_n = 50  # Prevent infinite outer loop

while n < max_n:
    # Calculate n-dependent components
    term_n = ((-1)**n) * (3**(2*n + 1)) / ((2*n + 1) * mp.factorial(2*n + 1))
    
    sum_m = mp.mpf(0)
    m = 0
    max_m = 1000  # Prevent infinite inner loop
    
    while m < max_m:
        # Calculate m-dependent components
        factorial_2m = mp.factorial(2*m)
        term_m = (factorial_2m**2) / ((2**4)**m * (mp.factorial(m)**4))
        
        # Calculate gamma function components
        gamma_num = mp.gamma(n + mp.mpf('1.5')) * mp.gamma(m + 1)
        gamma_den = mp.gamma(n + m + mp.mpf('2.5'))
        gamma_ratio = gamma_num / gamma_den
        
        # Calculate term and add to m-sum
        term = term_n * term_m * gamma_ratio
        sum_m += term
        
        # Break if term is below precision threshold
        if mp.fabs(term) < 1e-15:
            break
        m += 1
    
    sum_total += sum_m
    
    # Break if m-sum contribution is negligible
    if mp.fabs(sum_m) < 1e-15:
        break
    n += 1

result = (mp.pi / 2) * sum_total
print(mp.nstr(result, n=10))