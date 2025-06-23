import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Initialize the sum
s = mp.mpf(0)
# Tolerance for convergence (1e-15)
tol = mp.mpf('1e-15')
# Maximum terms to prevent infinite loop
max_terms = 1000
# Current term index
m = 0

while m < max_terms:
    # Compute the power part: 2^{-m}
    power_term = mp.power(2, -m)
    
    # Compute the two Gamma functions in the numerator
    gamma1 = mp.gamma(mp.mpf(m)/2 + mp.mpf('0.75'))  # Gamma(m/2 + 3/4)
    gamma2 = mp.gamma(mp.mpf(m)/2 + mp.mpf('1.25'))  # Gamma(m/2 + 5/4)
    numerator = power_term * gamma1 * gamma2
    
    # Compute the denominator: (m!)^2 * Gamma(m+2)
    fact_m = mp.factorial(m)
    gamma_denom = mp.gamma(m + 2)  # Equivalent to (m+1)!
    denominator = (fact_m ** 2) * gamma_denom
    
    # Compute the current term without the leading factor of 2
    term = numerator / denominator
    
    # Add the term to the sum
    s += term
    
    # Check for convergence: if |term| is below tolerance, break
    if mp.fabs(term) < tol:
        break
    
    m += 1

# Multiply by the leading factor of 2
result = 2 * s

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))