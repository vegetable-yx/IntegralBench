import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# User must define the values of a and b here
a = mp.mpf('1.0')  # Example value, replace with desired value
b = mp.mpf('1.0')  # Example value, replace with desired value

# Initialize the sum for the series expansion
series_sum = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')
max_terms = 10000  # Prevent infinite loops

# Compute the series expansion until convergence
while n < max_terms:
    # Compute (b * a)^{2n}
    power_factor = (b * a) ** (2 * n)
    
    # Compute the beta function: B(n + 1.5, n + 1)
    beta_val = mp.beta(n + mp.mpf('1.5'), n + 1)
    
    # Compute denominator: (2n)! = gamma(2n + 1)
    factorial_denom = mp.gamma(2 * n + 1)
    
    # Calculate the current term in the series
    term = power_factor * beta_val / factorial_denom
    series_sum += term
    
    # Break if the term is below tolerance
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Multiply by a^{3/2} to get the final result
result = a ** mp.mpf('1.5') * series_sum

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))