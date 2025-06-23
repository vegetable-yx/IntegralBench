import mpmath as mp

mp.dps = 15  # Set internal decimal precision

sum_result = mp.mpf(0)
n = 0

while True:
    # Calculate numerator components
    sign = (-1) ** n
    gamma_n_plus_1 = mp.gamma(n + 1)
    numerator = sign * mp.sqrt(mp.pi) * gamma_n_plus_1

    # Calculate denominator components
    factorial_2n = mp.factorial(2 * n)
    gamma_n_plus_1_5 = mp.gamma(n + 1.5)
    denominator = factorial_2n * gamma_n_plus_1_5

    # Compute current term in series
    term = numerator / denominator

    # Add term to cumulative sum
    sum_result += term

    # Break loop if term magnitude drops below precision threshold
    if mp.fabs(term) < 1e-15:
        break

    n += 1

# Final result is the computed sum (already includes 2* factor from original integral)
result = sum_result

# Print result with 10 decimal places
print(mp.nstr(result, n=10))