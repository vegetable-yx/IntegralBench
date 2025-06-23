import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')  # Tolerance for stopping the summation
two_pow_3half = mp.sqrt(8)  # Precompute 2^(3/2) = sqrt(8)

while True:
    # Calculate sign (-1)^n using mpmath power to maintain precision
    sign = mp.power(-1, n)
    # Compute 2^(n + 3/2) = 2^n * 2^(3/2)
    two_power = two_pow_3half * mp.power(2, n)
    # Calculate (n!)^2
    n_fact_sq = mp.factorial(n) ** 2
    # Calculate denominator (2n+1)!^2
    denominator = mp.factorial(2 * n + 1) ** 2
    # Compute current term in the series
    term = sign * two_power * n_fact_sq / denominator
    
    sum_result += term  # Add term to the cumulative sum
    
    # Check if term magnitude is below tolerance
    if mp.fabs(term) < tolerance:
        break
    n += 1  # Increment n for next term

# Print result with exactly 10 decimal places using mpmath string formatting
print(mp.nstr(sum_result, n=10))