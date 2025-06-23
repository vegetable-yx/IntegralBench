import mpmath as mp

mp.dps = 15

result = mp.mpf(0)
n = 0

while True:
    n_fact = mp.factorial(n)
    sum_k = mp.mpf(0)
    k = 0
    
    while True:
        beta_val = mp.beta(n + 1, k + 1.5)
        term_k = (1 / (2 * k + 1)) * 0.5 * beta_val
        sum_k += term_k
        
        if mp.fabs(term_k) < 1e-20:
            break
        k += 1
    
    term_n = sum_k / (n_fact ** 2)
    result += term_n
    
    if mp.fabs(term_n) < 1e-15:
        break
    n += 1

result *= 2
print(mp.nstr(result, n=10))