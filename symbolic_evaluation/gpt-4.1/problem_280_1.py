import mpmath as mp
mp.dps = 15

# Precompute constant factor sqrt(6π)/2
constant_factor = mp.sqrt(6 * mp.pi) / 2

# Initialize sum and set up variables for series calculation
series_sum = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')

# Calculate series terms until they drop below tolerance
while True:
    # Calculate numerator components
    nine_power = 9**n
    
    # Calculate denominator components
    factorial_term = mp.factorial(2 * n)
    gamma_ratio = 1 / (n + mp.mpf('5/4'))  # Using Γ(a+1) = aΓ(a) identity
    
    # Compute current term
    term = nine_power / (factorial_term * gamma_ratio)
    term = nine_power / (factorial_term * (n + mp.mpf('5/4')))
    
    series_sum += term
    
    # Break condition when term becomes smaller than tolerance
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Multiply accumulated sum by constant factor
result = constant_factor * series_sum

# Print final result with 10 decimal precision
print(mp.nstr(result, n=10))