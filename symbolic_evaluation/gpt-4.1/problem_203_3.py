import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Initialize the sum
total = mp.mpf(0)
k = 0
tolerance = mp.mpf('1e-15')  # Tolerance for convergence
max_iter = 1000  # Maximum iterations to prevent infinite loops

# Use series expansion to compute the expression
while k < max_iter:
    # Compute beta functions for current k
    beta1 = mp.beta(k + 1, 0.5)   # B(k+1, 1/2)
    beta2 = mp.beta(k + 2, 0.5)   # B(k+2, 1/2)
    
    # Compute the term: [B(k+1,1/2) - B(k+2,1/2)/2] * (-1)^k / (2k)!
    term_val = beta1 - beta2 / 2
    factorial_2k = mp.fac(2 * k)
    term = term_val * ((-1) ** k) / factorial_2k
    
    total += term  # Add term to total sum
    
    # Check for convergence: break if term is below tolerance
    if mp.fabs(term) < tolerance:
        break
    k += 1

# Multiply by factor 2 from the series representation
result = 2 * total

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))