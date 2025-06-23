import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

result = mp.mpf(0)
n = 0

while True:
    # Calculate components of the term
    sqrt_pi = mp.sqrt(mp.pi)
    numerator = sqrt_pi
    
    factorial_n = mp.factorial(n)
    gamma_term = mp.gamma(n + 1.5)  # Gamma(n + 3/2)
    denominator = 2 * (2*n + 1) * factorial_n * gamma_term
    
    term = numerator / denominator
    
    result += term
    
    # Check if the term is smaller than 1e-15 to stop summation
    if mp.fabs(term) < 1e-15:
        break
    
    n += 1

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))