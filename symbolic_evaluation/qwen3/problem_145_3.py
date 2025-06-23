import mpmath as mp

mp.dps = 15  # Set internal precision

result = mp.mpf(0)
term = mp.mpf(1)  # Initialize with k=0 term
k = 0

while True:
    result += term
    k += 1
    # Calculate numerator and denominator components
    numerator = 4**k
    denominator = (k + 1) * (2*k + 1) * mp.fac(2*k + 1)
    term = numerator / denominator
    # Check if term is smaller than 1e-15 to ensure 10 decimal precision
    if mp.fabs(term) < 1e-15:
        break

print(mp.nstr(result, n=10))