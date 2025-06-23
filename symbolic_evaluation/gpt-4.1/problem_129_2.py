import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute constant factor: 2^(3/2) = 2 * sqrt(2)
constant_factor = 2 * mp.sqrt(2)

# Initialize the sum and start at k=0
series_sum = mp.mpf(0)
k = 0
# Tolerance for term convergence (1e-15)
tol = mp.mpf('1e-15')
max_iter = 1000  # Safeguard against non-convergence

while k < max_iter:
    # Compute 2^(-k/2)
    power_term = mp.power(2, -k / 2.0)
    
    # Compute denominator (k!)^2
    factorial_k = mp.factorial(k)
    denom = factorial_k ** 2
    
    # Compute arguments for beta function
    a = (k + 3) / 2.0
    b = k / 2.0 + 1
    
    # Evaluate beta function B(a, b)
    beta_val = mp.beta(a, b)
    
    # Compute current term: [2^(-k/2) / (k!)^2] * B(a, b)
    term = power_term / denom * beta_val
    
    # Add term to the series sum
    series_sum += term
    
    # Check for convergence (if term magnitude drops below tolerance)
    if mp.fabs(term) < tol:
        break
    
    k += 1

# Multiply the series sum by the constant factor
result = constant_factor * series_sum

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))