import mpmath as mp

mp.dps = 15

total = mp.mpf(0)
k = 0

while True:
    # Calculate numerator: 4^k
    numerator = mp.power(4, k)
    
    # Calculate denominator components
    squared_term = (2*k + 1)**2
    linear_term = k + 1
    factorial_term = mp.fac(2*k)
    
    # Combine denominator components
    denominator = squared_term * linear_term * factorial_term
    
    # Compute current term in the series
    term = numerator / denominator
    
    # Add term to total sum
    total += term
    
    # Break loop if term becomes smaller than working precision epsilon
    if mp.fabs(term) < mp.eps:
        break
    
    k += 1

# Print result with exactly 10 decimal places
print(mp.nstr(total, n=10))