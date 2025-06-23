import mpmath as mp

mp.dps = 15  # Initialize sum and variables
sum_part = mp.mpf(0)
n = 0
epsilon = mp.mpf('1e-15')

while True:
    # Calculate components for the current term
    gamma_n_plus_3_2 = mp.gamma(n + mp.mpf('3/2'))
    gamma_n_plus_1 = mp.gamma(n + 1)
    pow_32_n = mp.power(32, n)
    numerator = pow_32_n * gamma_n_plus_3_2 * gamma_n_plus_1
    
    gamma_2n_plus_1 = mp.gamma(2*n + 1)
    gamma_2n_plus_5_2 = mp.gamma(2*n + mp.mpf('5/2'))
    denominator = gamma_2n_plus_1 * gamma_2n_plus_5_2
    
    term = numerator / denominator
    sum_part += term  # Accumulate the term
    
    # Check for convergence
    if mp.fabs(term) < epsilon:
        break
    n += 1

result = 8 * sum_part  # Multiply by the series coefficient
print(mp.nstr(result, n=10))