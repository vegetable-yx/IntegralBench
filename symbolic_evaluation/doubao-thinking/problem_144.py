import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)
n = 0
threshold = mp.mpf('1e-15')  # Threshold to terminate summation

while True:
    # Calculate numerator components
    numerator_factor1 = n + 1
    numerator_factor2 = mp.power(2, 2 * n + 1)
    numerator = numerator_factor1 * numerator_factor2
    
    # Calculate denominator components
    factorial_n = mp.factorial(n)
    denominator_part1 = factorial_n ** 2  # (n!)^2
    denominator_part2 = (2 * n + 3) ** 2  # (2n+3)^2
    factorial_2n1 = mp.factorial(2 * n + 1)  # (2n+1)!
    
    # Combine denominator components
    denominator = denominator_part1 * denominator_part2 * factorial_2n1
    
    # Compute current term value
    term = numerator / denominator
    
    # Add term to the cumulative sum
    sum_result += term
    
    # Check if term is below precision threshold
    if mp.fabs(term) < threshold:
        break
    
    n += 1

# Print result with exactly 10 decimal places
print(mp.nstr(sum_result, n=10))