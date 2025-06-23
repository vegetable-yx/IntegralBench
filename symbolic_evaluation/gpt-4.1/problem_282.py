import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (example values, can be adjusted)
a = mp.mpf(1)  # Example value for a
b = mp.mpf(1)  # Example value for b

# Precompute the multiplicative factor a^{-1/2}
pre_factor = a**(-mp.mpf('0.5'))

# Initialize the series sum
series_sum = mp.mpf(0)
n = 0
max_iter = 10000  # Maximum iterations to prevent infinite loop
tolerance = mp.mpf('1e-15')  # Tolerance for convergence

# Sum the series until convergence
while n < max_iter:
    # Compute (b*a)^{2n}
    base_power = (b * a)**(2 * n)
    
    # Compute factorial of 2n
    factorial_2n = mp.factorial(2 * n)
    
    # Compute Gamma(n + 1/4)
    gamma_n_plus_quarter = mp.gamma(n + mp.mpf('0.25'))
    
    # Square of Gamma(n + 1/4)
    gamma_sq = gamma_n_plus_quarter**2
    
    # Compute Gamma(2n + 1/2)
    gamma_2n_half = mp.gamma(2 * n + mp.mpf('0.5'))
    
    # Calculate the term: [ (b*a)^{2n} / (2n)! ] * [ Gamma(n+1/4)^2 / Gamma(2n+1/2) ]
    term = (base_power / factorial_2n) * (gamma_sq / gamma_2n_half)
    
    # Add term to the series sum
    series_sum += term
    
    # Check for convergence (if term is below tolerance)
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Multiply the series sum by the pre-factor
result = pre_factor * series_sum

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))