import mpmath as mp

mp.dps = 15  # Set internal precision

sum_total = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')

while True:
    # Calculate 2^n
    power_term = mp.power(2, n)
    
    # Calculate (2n)!
    factorial_term = mp.factorial(2 * n)
    
    # Calculate gamma function arguments
    gamma_arg1 = mp.mpf(n)/2 + mp.mpf('5/4')
    gamma_arg2 = mp.mpf(n)/2 + mp.mpf('3/4')
    
    # Compute gamma products
    gamma_product = mp.gamma(gamma_arg1) * mp.gamma(gamma_arg2)
    
    # Compute denominator gamma(n + 2)
    gamma_denom = mp.gamma(n + 2)
    
    # Compute current term
    term = (power_term / factorial_term) * (gamma_product / gamma_denom)
    
    # Add term to total sum
    sum_total += term
    
    # Check for convergence
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Multiply by 2 as per the formula
result = 2 * sum_total

# Print result with 10 decimal places
print(mp.nstr(result, n=10))