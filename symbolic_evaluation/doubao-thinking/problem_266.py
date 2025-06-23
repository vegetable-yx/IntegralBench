import mpmath as mp

mp.dps = 15  # Set internal precision

total = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')  # Tolerance for term magnitude

while True:
    # Calculate components for the series term
    sign = (-1) ** n
    numerator = mp.factorial(2 * n)
    fact_n = mp.factorial(n)
    denominator = (fact_n ** 3) * (n + 1) * (4 ** n) * (2 * n + 1)
    term = sign * numerator / denominator
    
    total += term
    
    # Check if term is below precision threshold
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Multiply accumulated sum by pi/2 for final result
result = (mp.pi / 2) * total

# Print with exactly 10 decimal places
print(mp.nstr(result, n=10))