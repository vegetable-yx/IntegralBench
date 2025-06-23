import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum and k counter
s = mp.mpf(0)
k = 0
# Tolerance for convergence (1e-15) since we require 10 decimal places
tol = mp.mpf('1e-15')

while True:
    # Compute factorial squared term: 1/(k!)^2
    fact_sq = mp.power(mp.factorial(k), -2)
    
    # Compute 2^{-k}
    power_term = mp.power(2, -k)
    
    # Gamma function arguments
    arg1 = mp.mpf(2*k + 3) / 4  # (2k+3)/4
    arg2 = mp.mpf(2*k + 5) / 4  # (2k+5)/4
    arg3 = mp.mpf(2*k + 3) / 2  # (2k+3)/2
    
    # Compute gamma functions
    gamma1 = mp.gamma(arg1)
    gamma2 = mp.gamma(arg2)
    gamma3 = mp.gamma(arg3)
    
    # Combine gamma terms: Gamma((2k+3)/4) * Gamma((2k+5)/4) / Gamma((2k+3)/2)
    gamma_ratio = (gamma1 * gamma2) / gamma3
    
    # Compute the current term in the series
    term = fact_sq * power_term * gamma_ratio
    
    # Add term to the sum
    s += term
    
    # Check for convergence: break if term is below tolerance
    if mp.fabs(term) < tol:
        break
    
    # Increment k for next term
    k += 1

# Multiply the sum by 2 for the final result
result = 2 * s

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))