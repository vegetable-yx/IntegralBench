import mpmath as mp
mp.dps = 15

sum_result = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')

while True:
    # Calculate 2^n using mpmath power function
    power_term = mp.power(2, n)
    
    # Calculate factorials for denominator components
    factorial_2n = mp.factorial(2*n)
    factorial_n = mp.factorial(n)
    
    # Calculate arguments for gamma functions
    gamma_arg1 = (mp.mpf('1.5') + n) / 2  # (3/2 + n)/2
    gamma_arg2 = (mp.mpf('0.5') + n) / 2  # (1/2 + n)/2
    
    # Compute gamma function values
    gamma_val1 = mp.gamma(gamma_arg1)
    gamma_val2 = mp.gamma(gamma_arg2)
    
    # Calculate current term in the series
    numerator = power_term * gamma_val1 * gamma_val2
    denominator = factorial_2n * factorial_n
    term = numerator / denominator
    
    # Add term to cumulative sum
    sum_result += term
    
    # Check convergence using absolute value of term
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

print(mp.nstr(sum_result, n=10))