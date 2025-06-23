import mpmath as mp
mp.dps = 15

sum_total = mp.mpf(0)
k = 0
while True:
    # Calculate numerator (k + 1)
    numerator = k + 1
    # Compute factorial of k
    factorial_k = mp.factorial(k)
    # Compute Gamma(k + 5/2)
    gamma_term = mp.gamma(k + mp.mpf('5/2'))
    # Compute denominator components
    denominator = (2*k + 3) * gamma_term
    # Calculate current term value
    term = numerator / (factorial_k * denominator)
    # Add term to the total sum
    sum_total += term
    # Break loop if term becomes too small
    if mp.abs(term) < mp.mpf('1e-30'):
        break
    k += 1

# Multiply by sqrt(pi)/2 and print result
result = (mp.sqrt(mp.pi) / 2) * sum_total
print(mp.nstr(result, n=10))