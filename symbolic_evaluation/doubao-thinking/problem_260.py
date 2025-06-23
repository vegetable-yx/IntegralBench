import mpmath as mp

mp.dps = 15

# Initialize sum for the series expansion
series_sum = mp.mpf(0)
k = 0
term = mp.mpf(1)  # First term (k=0)

# Compute terms until they become smaller than 1e-15
while True:
    series_sum += term
    k += 1
    # Calculate next term components
    sign = (-1) ** k
    factorial_k = mp.factorial(k)
    denominator = (2*k + 1) * (factorial_k ** 2) * (4 ** k)
    term = sign / denominator
    # Check for convergence
    if mp.fabs(term) < 1e-15:
        break

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * series_sum

# Print result to 10 decimal places
print(mp.nstr(result, n=10))