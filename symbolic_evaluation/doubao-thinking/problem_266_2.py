import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)  # Initialize the sum
n = 0
tolerance = mp.mpf('1e-15')  # Tolerance for stopping the summation

while True:
    # Calculate the numerator components: (-1)^n, 4^n, and n!
    sign = (-1) ** n
    power_4n = 4 ** n
    factorial_n = mp.factorial(n)
    numerator = sign * power_4n * factorial_n

    # Calculate the denominator components: (n+1), (2n+1), and (2n+1)!
    term_n1 = n + 1
    term_2n1 = 2 * n + 1
    factorial_2n1 = mp.factorial(term_2n1)
    denominator = term_n1 * term_2n1 * factorial_2n1

    # Compute the current term and add to the sum
    term = numerator / denominator
    sum_result += term

    # Check if the term is smaller than the tolerance to stop summation
    if mp.fabs(term) < tolerance:
        break

    n += 1

# Print the result with 10 decimal places
print(mp.nstr(sum_result, n=10))