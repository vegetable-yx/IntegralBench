import mpmath as mp

mp.dps = 15  # Set internal precision

result = mp.mpf(0)
k = 0
while True:
    # Calculate sign term
    sign = (-1) ** k
    # Calculate numerator components
    coeff = 8 * (4 ** k)
    poly_term = (k + 2) * (k + 1)
    factorial_sq = mp.factorial(k) ** 2
    numerator = coeff * poly_term * factorial_sq
    
    # Calculate denominator components
    denom1 = mp.factorial(2 * k)
    denom2 = mp.factorial(2 * k + 3)
    denominator = denom1 * denom2
    
    # Compute current term and add to result
    term = sign * numerator / denominator
    result += term
    
    # Check for convergence (term smaller than 1e-15)
    if mp.fabs(term) < 1e-15:
        break
    k += 1

# Print result to 10 decimal places
print(mp.nstr(result, n=10))