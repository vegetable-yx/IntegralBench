import mpmath as mp

mp.dps = 15  # Set internal precision

# Initialize variables for the series summation
result = mp.mpf(0)
term = mp.mpf(1)  # First term (k=0)
k = 0
tolerance = mp.mpf('1e-15')  # Convergence tolerance

# Sum the series until terms are below tolerance
while True:
    result += term
    k += 1
    # Calculate the next term using the ratio of consecutive terms
    numerator = -4 * (k ** 2)
    denominator = (2 * k) * (2 * k - 1) * (2 * k + 1)
    term *= numerator / denominator
    if mp.fabs(term) < tolerance:
        break

# Multiply by 2 as per the original expression
result *= 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))