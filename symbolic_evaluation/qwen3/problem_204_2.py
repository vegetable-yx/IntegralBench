import mpmath as mp

mp.dps = 15  # Set internal precision

result = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')  # Term magnitude threshold to stop summation

while True:
    # Calculate sign component (-1)^n
    sign = (-1) ** n
    
    # Compute 2^(n+2) using mpmath power function
    power_term = mp.power(2, n + 2)
    
    # Calculate factorial component (2n+1)!
    factorial_term = mp.factorial(2 * n + 1)
    
    # Compute Beta((2n+7)/4, (2n+5)/4)
    beta_a = (2 * n + 7) / 4
    beta_b = (2 * n + 5) / 4
    beta_val = mp.beta(beta_a, beta_b)
    
    # Calculate current term in series
    term = (sign * power_term / factorial_term) * beta_val
    
    # Add term to cumulative result
    result += term
    
    # Check termination condition
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Print final result with 10 decimal precision
print(mp.nstr(result, n=10))