import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum and set tolerance for convergence
total = mp.mpf(0)
tolerance = mp.mpf('1e-15')
n = 0
max_iter = 1000  # Prevent infinite loops

# Start the summation
while n < max_iter:
    # Calculate the sign: (-1)^n
    sign = mp.mpf(1) if n % 2 == 0 else mp.mpf(-1)
    
    # Compute 4^n
    power_term = mp.power(4, n)
    
    # Compute gamma((3 + 4n)/4)
    gamma_arg1 = (3 + 4*n) / 4
    gamma1 = mp.gamma(gamma_arg1)
    
    # Compute gamma((1 + 4n)/4)
    gamma_arg2 = (1 + 4*n) / 4
    gamma2 = mp.gamma(gamma_arg2)
    
    # Compute denominator: Gamma(1 + 2n) = (2n)!
    denom = mp.gamma(1 + 2*n)
    
    # Compute the current term
    numerator = sign * power_term * gamma1 * gamma2
    term = numerator / denom
    
    # Add term to total
    total += term
    
    # Check for convergence
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Print the result to 10 decimal places
print(mp.nstr(total, n=10))