import mpmath as mp

mp.dps = 15  # Set internal precision

sum_result = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')

while True:
    # Calculate components for the series term
    sign = (-1)**n
    numerator_factor = 2*n + 1
    factorial_2n = mp.factorial(2*n)
    
    denominator_base = 4**(n + 1)
    denominator_sq = (n + 1)**2
    factorial_n_4 = mp.factorial(n)**4
    
    # Combine components to form term
    term = (sign * numerator_factor * factorial_2n) / (denominator_base * denominator_sq * factorial_n_4)
    
    sum_result += term
    
    # Check convergence using absolute term value
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Multiply accumulated sum by π/2 for final result
result = sum_result * mp.pi / 2

print(mp.nstr(result, n=10))