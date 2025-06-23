import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

result = mp.mpf(0)  # Initialize sum with mpmath floating-point zero
n = 0

while True:
    # Calculate numerator components
    exponent = n + 1
    power_term = mp.power(4, exponent)  # 4^(n+1)
    square_term = mp.power(exponent, 2)  # (n+1)^2
    numerator = power_term * square_term

    # Calculate denominator components
    factorial_arg = 2 * n + 3
    factorial_term = mp.factorial(factorial_arg)  # (2n+3)!
    denominator = factorial_arg * factorial_term  # (2n+3)*(2n+3)!

    # Compute current term and add to result
    term = numerator / denominator
    result += term

    # Break loop when term magnitude drops below precision threshold
    if mp.fabs(term) < 1e-15:
        break

    n += 1

# Print final result with exactly 10 decimal places
print(mp.nstr(result, n=10))