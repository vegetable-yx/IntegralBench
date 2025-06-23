import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_part = mp.mpf(0)  # Initialize the sum
n = 0  # Start the summation index at 0
epsilon = mp.mpf('1e-15')  # Convergence threshold

while True:
    # Calculate the sign for the current term (-1)^n
    sign = (-1) ** n
    # Compute 4^n (since 2^(2n) = 4^n)
    power_term = mp.power(4, n)
    # Compute (2n)! factorial
    factorial_term = mp.factorial(2 * n)
    # Compute the denominator part (n + 3/4)
    denominator_add = n + mp.mpf('3/4')
    # Combine all denominator components
    denominator = power_term * factorial_term * denominator_add
    # Calculate the current term
    term = sign / denominator
    # Add the term to the sum
    sum_part += term
    # Check if the term is smaller than the epsilon threshold
    if mp.fabs(term) < epsilon:
        break
    n += 1  # Increment index for next term

# Multiply the sum by sqrt(pi/2) to get the final result
result = mp.sqrt(mp.pi / 2) * sum_part

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))