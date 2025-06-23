import mpmath as mp

mp.dps = 15  # Set internal decimal precision

sum_result = mp.mpf(0)
k = 0
while True:
    # Calculate components of the term
    four_power_k = mp.power(4, k)
    factorial_sq = mp.factorial(k) ** 2
    denominator = four_power_k * (k + mp.mpf('0.5')) * factorial_sq
    
    # Calculate current term and add to sum
    term = 1 / denominator
    sum_result += term
    
    # Break loop when term becomes smaller than 1e-20
    if mp.fabs(term) < mp.mpf('1e-20'):
        break
    k += 1

# Multiply sum by sqrt(pi) for final result
result = mp.sqrt(mp.pi) * sum_result

# Print with 10 decimal precision
print(mp.nstr(result, n=10))