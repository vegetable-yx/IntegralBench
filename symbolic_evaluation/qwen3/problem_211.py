import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_total = mp.mpf(0)  # Initialize summation variable
n = 0  # Start summation index at 0

while True:
    # Calculate numerator (-1)^n
    numerator = (-1) ** n
    
    # Calculate denominator Gamma(2n + 3/2)
    gamma_arg = 2 * n + mp.mpf('3/2')
    denominator = mp.gamma(gamma_arg)
    
    # Compute current term in series
    term = numerator / denominator
    
    # Add term to summation total
    sum_total += term
    
    # Check if term magnitude is below precision threshold
    if mp.fabs(term) < 1e-15:
        break
    
    n += 1  # Increment index for next term

# Multiply sum by sqrt(pi) to get final result
result = mp.sqrt(mp.pi) * sum_total

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))