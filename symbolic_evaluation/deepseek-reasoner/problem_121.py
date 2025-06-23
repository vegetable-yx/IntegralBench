import mpmath as mp

mp.dps = 15  # Initialize sum for the series
sum_series = mp.mpf(0)
m = 0
while True:
    # Calculate numerator and denominator components
    numerator = (-1) ** m
    denominator = (2 * m + 1) ** 2 * (4 ** m)
    # Compute current term in the series
    term = mp.fdiv(numerator, denominator)
    sum_series += term
    # Break loop if term is below precision threshold
    if mp.fabs(term) < 1e-15:
        break
    m += 1

# Multiply the summed series by pi to get final result
result = mp.pi * sum_series

# Print result to 10 decimal places
print(mp.nstr(result, n=10))