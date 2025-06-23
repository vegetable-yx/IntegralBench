import mpmath as mp

mp.dps = 15  # Set internal precision

sum_result = mp.mpf(0)
k = 0
while True:
    # Calculate numerator components
    sign = (-1) ** k
    pow_2 = mp.power(2, 4*k + 1)
    
    # Calculate denominator components
    k_term = k + 1
    odd_term = (2*k + 1) ** 2
    factorial_term = mp.factorial(2*k)
    
    # Compute current term
    term = (sign * pow_2) / (k_term * odd_term * factorial_term)
    
    sum_result += term
    
    # Check convergence (term smaller than 1e-15)
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1

print(mp.nstr(sum_result, n=10))