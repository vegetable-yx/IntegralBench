import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_terms = mp.mpf(0)
n = 0
epsilon = mp.mpf('1e-15')  # Convergence threshold

while True:
    # Calculate components of the term
    pow32 = mp.power(32, n)
    gamma_n_plus_3_2 = mp.gamma(n + mp.mpf('1.5'))
    gamma_n_plus_1 = mp.gamma(n + 1)
    factorial_2n = mp.gamma(2*n + 1)  # Equivalent to (2n)!
    gamma_2n_plus_5_2 = mp.gamma(2*n + mp.mpf('2.5'))
    
    # Compute current term
    numerator = pow32 * gamma_n_plus_3_2 * gamma_n_plus_1
    denominator = factorial_2n * gamma_2n_plus_5_2
    current_term = numerator / denominator
    
    sum_terms += current_term  # Add term to the sum
    
    # Check if term is below precision threshold
    if mp.fabs(current_term) < epsilon:
        break
    
    n += 1

result = 8 * sum_terms  # Multiply sum by 8 as per the formula
print(mp.nstr(result, n=10))