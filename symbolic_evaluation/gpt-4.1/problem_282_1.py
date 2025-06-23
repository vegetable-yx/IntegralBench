import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_total = mp.mpf(0)
n = 0
epsilon = mp.mpf('1e-20')  # Convergence threshold for term magnitude

while True:
    # Calculate 16^n term
    power_term = 16 ** n
    
    # Compute factorial of 2n
    factorial_2n = mp.factorial(2 * n)
    
    # Calculate Gamma(n + 1/4) and square it
    gamma_n_plus_14 = mp.gamma(n + mp.mpf('0.25'))
    gamma_squared = gamma_n_plus_14 ** 2
    
    # Calculate Gamma(2n + 1/2)
    gamma_denom = mp.gamma(2 * n + mp.mpf('0.5'))
    
    # Compute current term in the series
    term = (power_term / factorial_2n) * (gamma_squared / gamma_denom)
    sum_total += term
    
    # Check if term magnitude is below threshold
    if mp.fabs(term) < epsilon:
        break
    
    n += 1

# Apply the 1/2 factor from the original expression
result = sum_total * mp.mpf('0.5')

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))