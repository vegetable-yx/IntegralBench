import mpmath as mp
mp.dps = 15

sum_result = mp.mpf(0)
n = 0
epsilon = mp.mpf('1e-15')

while True:
    # Calculate factorial terms in numerator and denominator
    numerator = mp.pi * mp.fac(2*n + 2)
    
    # Calculate denominator components
    four_power = 4**(n + 2)
    n_fac_sq = mp.fac(n)**2
    n_plus1_fac_sq = mp.fac(n + 1)**2
    denominator = four_power * n_fac_sq * n_plus1_fac_sq * (n + 1)
    
    term = numerator / denominator
    sum_result += term
    
    # Check convergence using absolute term size
    if mp.fabs(term) < epsilon:
        break
    
    n += 1

print(mp.nstr(sum_result, n=10))