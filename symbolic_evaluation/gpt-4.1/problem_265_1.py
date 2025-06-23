import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_total = mp.mpf(0)
tolerance = mp.mpf('1e-30')  # Term magnitude threshold to stop summation

for k in range(1000):  # Sufficiently large number of terms
    # Calculate numerator and denominator components
    sign = (-1) ** k
    factorial_k = mp.factorial(k)
    gamma_term = mp.gamma(k + 2.5)
    denominator = (k + 2) * factorial_k * gamma_term
    
    term = sign / denominator
    sum_total += term
    
    # Check if term is below tolerance to break early
    if mp.fabs(term) < tolerance:
        break

# Multiply by the constant factor sqrt(pi)/4
result = (mp.sqrt(mp.pi) / 4) * sum_total

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))