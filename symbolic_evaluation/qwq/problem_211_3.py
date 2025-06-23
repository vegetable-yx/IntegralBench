import mpmath as mp
mp.dps = 15

total = mp.mpf(0)
n = 0
threshold = mp.mpf('1e-15')

while True:
    # Calculate current term components
    sign = (-1) ** n
    gamma_arg = 2 * n + mp.mpf('1.5')
    
    # Compute term value
    term = sign / mp.gamma(gamma_arg)
    total += term
    
    # Check convergence using absolute value of term
    if mp.fabs(term) < threshold:
        break
    
    n += 1

# Multiply sum by sqrt(pi) for final result
result = mp.sqrt(mp.pi) * total

print(mp.nstr(result, n=10))