import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_terms = mp.mpf(0)
n = 0
eps = mp.mpf('1e-15')  # Precision threshold to stop summation

while True:
    # Calculate numerator components
    power_36 = mp.power(36, n)
    factorial_2n = mp.fac(2 * n)
    
    # Calculate gamma function components
    gamma_numerator = mp.gamma(n + mp.mpf('3/4'))
    gamma_numerator_sq = mp.power(gamma_numerator, 2)
    gamma_denominator = mp.gamma(2 * n + mp.mpf('3/2'))
    
    # Compute term components
    gamma_ratio = gamma_numerator_sq / gamma_denominator
    term = (power_36 / factorial_2n) * gamma_ratio
    
    sum_terms += term
    
    # Check if term is below precision threshold
    if mp.fabs(term) < eps:
        break
    
    n += 1

# Multiply by sqrt(3) and format result
result = mp.sqrt(3) * sum_terms
print(mp.nstr(result, n=10))