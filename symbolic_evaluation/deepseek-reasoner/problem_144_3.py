import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)  # Initialize the sum with mpmath precision
n = 0
tolerance = mp.mpf('1e-15')  # Convergence threshold

while True:
    # Calculate components of the numerator
    n_plus_1 = n + 1
    squared_term = n_plus_1 ** 2
    four_power = 4 ** n_plus_1
    numerator = squared_term * four_power

    # Calculate components of the denominator
    factorial_arg = 2 * n + 3
    factorial_term = mp.fac(factorial_arg)
    denominator = factorial_arg * factorial_term

    # Compute current term in the series
    term = numerator / denominator

    # Add term to cumulative sum
    sum_result += term

    # Check for convergence
    if mp.fabs(term) < tolerance:
        break

    n += 1

# Print result with exactly 10 decimal places
print(mp.nstr(sum_result, n=10))