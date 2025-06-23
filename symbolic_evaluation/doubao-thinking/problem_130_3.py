import mpmath as mp
mp.dps = 15

sum_result = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')

while True:
    # Calculate gamma functions for numerator
    gamma_n1 = mp.gamma((n + 1)/2)
    gamma_n2 = mp.gamma((n + 2)/2)
    numerator = gamma_n1 * gamma_n2
    
    # Calculate components
    power_term = mp.power(2, n)
    factorial_term = mp.factorial(n)**2
    gamma_denominator = mp.gamma((2*n + 3)/2)
    
    # Combine denominator components
    denominator = power_term * factorial_term * gamma_denominator
    
    # Calculate current term and add to sum
    term = mp.sqrt(2) * numerator / denominator
    sum_result += term
    
    # Check convergence
    if mp.fabs(term) < tolerance:
        break
    n += 1

print(mp.nstr(sum_result, n=10))