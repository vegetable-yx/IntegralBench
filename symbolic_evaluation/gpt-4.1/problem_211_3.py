import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant term: 2 * J_0(1)
constant_term = 2 * mp.besselj(0, 1)

# Initialize the series sum
series_sum = mp.mpf(0)

# Set tolerance and maximum terms to ensure convergence
tolerance = mp.mpf('1e-15')
max_terms = 10000
k = 1

# Sum the series until terms become negligible
while k <= max_terms:
    # Compute Bessel function J_{2k}(1)
    j_val = mp.besselj(2*k, 1)
    
    # Compute denominator: 4k^2 - 0.25
    denominator = 4*k**2 - 0.25
    
    # Compute the term: -J_{2k}(1) / (4k^2 - 0.25)
    term = -j_val / denominator
    
    # Add term to series sum
    series_sum += term
    
    # Check for convergence
    if mp.fabs(term) < tolerance:
        break
    
    k += 1

# Calculate the final result
result = constant_term + series_sum

# Print result to 10 decimal places
print(mp.nstr(result, n=10))