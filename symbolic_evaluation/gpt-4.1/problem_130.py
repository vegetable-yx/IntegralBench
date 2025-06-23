import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Initialize constants and variables
sqrt2 = mp.sqrt(2)
s = mp.mpf(0)          # Sum accumulator
tol = mp.mpf('1e-20')  # Tolerance for term convergence
max_terms = 10000      # Maximum number of terms to prevent infinite loops

# Initialize recurrence variables for factorial and powers of 2
k = 0
current_fact = mp.mpf(1)  # Start with 0! = 1
power2 = mp.mpf(1)        # Start with 2^0 = 1

# Sum the series until convergence or max_terms reached
while k < max_terms:
    # Compute arguments for gamma functions
    arg1 = mp.mpf(k + 1) / 2
    arg2 = mp.mpf(k + 2) / 2
    
    # Calculate gamma values for numerator
    gamma1 = mp.gamma(arg1)
    gamma2 = mp.gamma(arg2)
    numerator = gamma1 * gamma2
    
    # Compute denominator: (k+1) * (k!)^3 * 2^k
    denom = (k + 1) * (current_fact ** 3) * power2
    
    # Compute current term with sqrt(2) factor
    term = sqrt2 * numerator / denom
    s += term
    
    # Check for convergence
    if mp.fabs(term) < tol:
        break
    
    # Update recurrence relations for next term
    k += 1
    current_fact *= k  # k! for next iteration
    power2 *= 2       # 2^k for next iteration

# Print result to exactly 10 decimal places
print(mp.nstr(s, n=10))