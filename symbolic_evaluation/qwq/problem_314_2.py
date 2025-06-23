import mpmath as mp
mp.dps = 15

result = mp.mpf(0)
m = 0

while True:
    # Calculate components of the term
    exponent = 2 * m + 1
    two_power = mp.mpf(2) ** exponent
    cubic_term = mp.mpf(exponent) ** 3
    denominator = two_power * cubic_term
    
    # Compute current term value
    term = -1 / denominator
    result += term
    
    # Check convergence (term magnitude < 1e-15)
    if mp.fabs(term) < 1e-15:
        break
    
    m += 1

print(mp.nstr(result, n=10))