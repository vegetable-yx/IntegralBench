import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum for the series
series_sum = mp.mpf(0)
n = 0

while True:
    # Compute binomial coefficient C(2n, n)
    binom = mp.binomial(2*n, n)
    
    # Compute (1/16)^n
    power_factor = mp.power(mp.mpf(1)/16, n)
    
    # Compute ratio of Gamma functions: Gamma(n+2) / Gamma(n+2.5)
    gamma_ratio = mp.gamma(n+2) / mp.gamma(n + mp.mpf('2.5'))
    
    # Compute denominator factor: 2 / ((2n+1)(2n+3))
    denom_factor = mp.mpf(2) / ((2*n + 1) * (2*n + 3))
    
    # Compute current term
    term = binom * power_factor * gamma_ratio * denom_factor
    
    # Add term to the series sum
    series_sum += term
    
    # Break if term is below the threshold (1e-20)
    if mp.fabs(term) < mp.mpf('1e-20'):
        break
    
    n += 1

# Multiply by constant factor: sqrt(pi)/4
result = (mp.sqrt(mp.pi) / 4) * series_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))