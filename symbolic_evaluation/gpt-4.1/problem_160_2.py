import mpmath as mp

mp.dps = 15

sum_part = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-25')  # Term magnitude tolerance for convergence

while True:
    # Calculate components for current term
    numerator = 2**n
    denominator = mp.fac(2 * n)
    beta_arg1 = (n + 1)/2
    beta_arg2 = (n + 2)/2
    beta_val = mp.beta(beta_arg1, beta_arg2)
    
    # Compute term and add to sum
    term = (numerator / denominator) * beta_val
    sum_part += term
    
    # Check for convergence
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Multiply by sqrt(2) and format result
result = mp.sqrt(2) * sum_part
print(mp.nstr(result, n=10))