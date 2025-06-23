import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_terms = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')  # Tolerance to ensure 10 decimal accuracy

while True:
    # Calculate each component of the term
    power_10 = mp.power(10, 2 * n)  # Compute 10^(2n)
    numerator = (n + 2) * (n + 1)  # (n+2)(n+1) part
    fact_n = mp.factorial(n)  # n!
    fact_n_sq = fact_n ** 2  # (n!)^2
    denom1 = mp.factorial(2 * n)  # (2n)!
    denom2 = mp.factorial(3 + 2 * n)  # (3+2n)!
    denominator = denom1 * denom2  # Combine factorial terms
    
    term = (power_10 * numerator * fact_n_sq) / denominator
    sum_terms += term  # Accumulate the series sum
    
    if mp.fabs(term) < tolerance:  # Check convergence
        break
    
    n += 1

result = 125 * sum_terms  # Multiply by the series coefficient
print(mp.nstr(result, n=10))  # Print result to 10 decimal places