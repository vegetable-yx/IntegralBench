import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)
k = 0
tolerance = mp.mpf('1e-15')  # Tolerance for convergence

while True:
    # Calculate numerator: gamma((2k + 3)/2)
    numerator = mp.gamma((2 * k + 3) / 2)
    # Calculate denominator: (2k)! * gamma(k + 2)
    factorial_term = mp.factorial(2 * k)
    gamma_term = mp.gamma(k + 2)
    denominator = factorial_term * gamma_term
    # Compute the current term in the series
    term = (mp.sqrt(mp.pi) * numerator) / denominator
    sum_result += term
    # Check if the term is smaller than the tolerance
    if mp.fabs(term) < tolerance:
        break
    k += 1

# Multiply by 2 as per the original integral expression
result = 2 * sum_result

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))