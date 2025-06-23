import mpmath as mp
mp.dps = 15

sum_result = mp.mpf(0)
k = 0

while True:
    # Calculate 4^k with full precision
    numerator = mp.power(4, k)
    
    # Compute factorial term (2k)!
    factorial_term = mp.factorial(2 * k)
    
    # Calculate denominator components
    linear_term = k + 1
    squared_term = (2*k + 1)**2
    denominator_part = linear_term * squared_term
    
    # Combine denominator components
    denominator = denominator_part * factorial_term
    
    # Calculate current series term
    term = numerator / denominator
    
    # Add term to cumulative sum
    sum_result += term
    
    # Check convergence (term < 1e-15)
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1

print(mp.nstr(sum_result, n=10))