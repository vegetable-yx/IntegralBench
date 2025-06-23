import mpmath as mp

mp.dps = 15

total = mp.mpf(0)
k = 0
tolerance = mp.mpf('1e-20')

while True:
    # Calculate denominator components separately
    numerator = mp.mpf(1)
    odd_term = mp.mpf(2*k + 1)
    power_term = mp.power(4, k)
    
    # Combine denominator components
    denominator = odd_term**3 * power_term
    
    # Calculate current term value
    term = numerator / denominator
    
    # Add term to total sum
    total += term
    
    # Check convergence condition
    if mp.fabs(term) < tolerance:
        break
    
    k += 1

# Apply final negative sign
result = -total

# Print with 10 decimal precision
print(mp.nstr(result, n=10))