import mpmath as mp
mp.dps = 15

sum_total = mp.mpf(0)
n = 0

# Compute the first term (n=0)
term = (mp.pi * mp.fac(2*n + 2)) / (4**(n + 2) * (n + 1)**3 * mp.fac(n)**4)
sum_total += term

epsilon = mp.mpf(1e-20)

while True:
    # Calculate ratio for next term based on current n
    ratio_numerator = 2 * n + 3
    ratio_denominator = 2 * (n + 1) * (n + 2)**2
    ratio = mp.mpf(ratio_numerator) / ratio_denominator
    
    # Update term and add to sum
    term *= ratio
    sum_total += term
    
    # Check if term is below precision threshold
    if mp.fabs(term) < epsilon:
        break
    n += 1

print(mp.nstr(sum_total, n=10))