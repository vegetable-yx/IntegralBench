import mpmath as mp

mp.dps = 15  # Set internal precision

sum_result = mp.mpf(0)
m = 0
while True:
    # Calculate numerator (-4)^m using exact integer operations
    sign = (-1)**m
    four_power = mp.power(4, m)
    numerator = sign * four_power
    
    # Calculate denominator components
    factorial_term = mp.factorial(2*m)
    linear_term = m + 1
    squared_term = (2*m + 1)**2
    
    # Combine denominator parts
    denominator = linear_term * factorial_term * squared_term
    
    # Compute current term and add to sum
    term = numerator / denominator
    sum_result += term
    
    # Check convergence criterion
    if mp.fabs(term) < 1e-15:
        break
    
    m += 1

print(mp.nstr(sum_result, n=10))