import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

sum_result = mp.mpf(0)  # Initialize sum
n = 0                   # Term index counter
tolerance = mp.mpf('1e-15')  # Convergence threshold

while True:
    # Calculate parameters for Gamma functions
    gamma_arg1 = mp.mpf(3)/4 + mp.mpf(n)/2
    gamma_arg2 = mp.mpf(1)/4 + mp.mpf(n)/2
    
    # Compute numerator components
    two_pow_n = mp.power(2, n)
    gamma_product = mp.gamma(gamma_arg1) * mp.gamma(gamma_arg2)
    
    # Compute denominator components
    factorial_2n = mp.fac(2 * n)
    gamma_n_plus_1 = mp.gamma(1 + n)
    
    # Calculate current term value
    term = (two_pow_n / factorial_2n) * (gamma_product / gamma_n_plus_1)
    
    # Add term to cumulative sum
    sum_result += term
    
    # Check for convergence
    if mp.fabs(term) < tolerance:
        break
    
    n += 1  # Move to next term

# Print result with exactly 10 decimal places
print(mp.nstr(sum_result, n=10))