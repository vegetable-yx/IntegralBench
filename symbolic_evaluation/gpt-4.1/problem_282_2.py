import mpmath as mp
mp.dps = 15

# Calculate the constant factor (1/2) * Gamma(1/4)^2
gamma_1_4 = mp.gamma(mp.mpf(1)/4)
constant = mp.mpf(0.5) * gamma_1_4**2

# Initialize series sum and variables
series_sum = mp.mpf(0)
n = 0
term = mp.mpf('1e-25')  # Convergence threshold

while True:
    # Calculate numerator 16^n
    numerator = mp.power(16, n)
    
    # Calculate denominator components (2n)! and Gamma(1/4 + n)^2
    factorial_denom = mp.factorial(2*n)
    gamma_denom = mp.gamma(mp.mpf(1)/4 + n)**2
    
    # Compute current term value
    current_term = numerator / (factorial_denom * gamma_denom)
    
    # Add term to series sum
    series_sum += current_term
    
    # Check for convergence
    if mp.fabs(current_term) < term:
        break
    n += 1

# Calculate final result and print
result = constant * series_sum
print(mp.nstr(result, n=10))