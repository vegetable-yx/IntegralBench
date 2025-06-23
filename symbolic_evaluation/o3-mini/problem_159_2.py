import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Example values for a and b (can be modified by user)
a = mp.mpf(1)
b = mp.mpf(1)

# Precompute constant factor: a^(3/2)
a_factor = a**(mp.mpf(3)/2)

# Initialize the sum
total = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')
max_terms = 1000

# Sum the series until convergence
while n < max_terms:
    # Compute (a*b^2)^n
    ab2_power = (a * b**2)**n
    
    # Compute denominator factorial: (2n)!
    factorial_denom = mp.factorial(2*n)
    
    # Compute Gamma function arguments
    arg1 = n/mp.mpf(2) + mp.mpf(3)/2  # n/2 + 3/2
    arg2 = n/mp.mpf(2) + 1            # n/2 + 1
    arg3 = n + mp.mpf(5)/2             # n + 5/2
    
    # Evaluate Gamma functions
    gamma1 = mp.gamma(arg1)
    gamma2 = mp.gamma(arg2)
    gamma3 = mp.gamma(arg3)
    
    # Combine factors for current term
    term = a_factor * ab2_power / factorial_denom * gamma1 * gamma2 / gamma3
    
    total += term
    
    # Check for convergence
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Print final result to exactly 10 decimal places
print(mp.nstr(total, n=10))