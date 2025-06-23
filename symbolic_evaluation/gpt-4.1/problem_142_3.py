import mpmath as mp

mp.dps = 15  # Set internal precision

sum_total will accumulate the series terms
sum_total = mp.mpf(0)
k = 0
epsilon = mp.mpf('1e-15')  # Convergence threshold

while True:
    # Calculate numerator (4^k)
    numerator = mp.power(4, k)
    
    # Calculate denominator components
    factorial_k = mp.factorial(k)
    denominator_part1 = mp.power(factorial_k, 2)
    denominator_part2 = 2 * k + 1
    gamma_part = mp.gamma(k + mp.mpf('1.5'))  # Gamma(k + 3/2)
    
    # Compute current term
    term = numerator / (denominator_part1 * denominator_part2 * gamma_part)
    sum_total += term
    
    # Check for convergence
    if mp.fabs(term) < epsilon:
        break
    
    k += 1

# Multiply by sqrt(pi)/2 to get final result
result = sum_total * mp.sqrt(mp.pi) / 2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))