import mpmath as mp

mp.dps = 15

sum_part = mp.mpf(0)
n = 0

while True:
    # Calculate the term for n
    term_coeff = mp.power(2, n) / mp.fac(2 * n)
    gamma_num = mp.gamma((n + 1)/2) * mp.gamma((n + 2)/2)
    gamma_den = mp.gamma((2*n + 3)/2)
    term = term_coeff * gamma_num / gamma_den
    
    sum_part += term
    
    # Check if the term is smaller than 1e-15 (using magnitude)
    if mp.mag(term) < -50:
        break
    
    n += 1

# Multiply by sqrt(2) to get the final result
result = mp.sqrt(2) * sum_part

print(mp.nstr(result, n=10))