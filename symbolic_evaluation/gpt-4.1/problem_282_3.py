import mpmath as mp

mp.dps = 15  # Set internal decimal precision

# Compute Gamma(1/4) and precompute 0.5 * Gamma(1/4)^2
gamma_14 = mp.gamma(mp.mpf('0.25'))
gamma_term = mp.mpf('0.5') * gamma_14 ** 2

# Initialize sum and variables for series computation
series_sum = mp.mpf('0')
n = 0
term = mp.mpf('0')

while True:
    # Calculate components of the current term
    power_term = mp.power(16, n)
    factorial_denom = mp.factorial(2 * n)
    gamma_denom = mp.gamma(mp.mpf(n) + mp.mpf('0.25')) ** 2
    
    # Compute current term and add to series sum
    term = power_term / (factorial_denom * gamma_denom)
    series_sum += term
    
    # Break loop when term magnitude drops below precision threshold
    if mp.fabs(term) < mp.mpf('1e-15'):
        break
    
    n += 1

# Compute final result and print with 10 decimal precision
result = gamma_term * series_sum
print(mp.nstr(result, n=10))