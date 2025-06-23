import mpmath as mp

mp.dps = 15  # Set internal precision

result = mp.mpf(0)
tolerance = mp.mpf('1e-15')  # Tolerance to ensure precision up to 1e-15

n = 0
while True:
    # Calculate components of the term
    numerator = mp.power(4, n)
    factorial_2n = mp.factorial(2 * n)
    gamma_n_plus_1 = mp.gamma(n + 1)
    gamma_n_half = mp.gamma(n + 0.5)
    gamma_2n_plus_1_5 = mp.gamma(2 * n + 1.5)
    
    # Compute the term for current n
    term = mp.mpf(2) * (numerator / factorial_2n) * (gamma_n_plus_1 * gamma_n_half) / gamma_2n_plus_1_5
    
    # Add term to the result
    result += term
    
    # Break loop if term is smaller than tolerance
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))