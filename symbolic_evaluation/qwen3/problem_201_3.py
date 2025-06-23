import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

result = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')  # Tolerance for stopping the summation

while True:
    # Calculate sign component (-1)^n
    sign = (-1) ** n
    
    # Calculate 2^(2n + 1) using mpmath power
    power_of_2 = mp.power(2, 2 * n + 1)
    
    # Calculate (n!)^2 using mpmath factorial
    n_fact_sq = mp.factorial(n) ** 2
    
    # Calculate denominator components (2n)! and (2n+1)!
    denom1 = mp.factorial(2 * n)
    denom2 = mp.factorial(2 * n + 1)
    denominator = denom1 * denom2
    
    # Compute current term in the series
    term = (sign * power_of_2 * n_fact_sq) / denominator
    
    # Add term to the result
    result += term
    
    # Check if term is smaller than tolerance to stop summation
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))