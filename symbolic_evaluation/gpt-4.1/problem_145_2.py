import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)  # Initialize sum with mpmath floating point
k = 0

while True:
    # Calculate numerator components: 2^(2k) and sqrt(pi)
    power_term = mp.power(2, 2 * k)
    sqrt_pi = mp.sqrt(mp.pi)
    numerator = power_term * sqrt_pi
    
    # Calculate denominator components: (k+1)!, (2k+1), and Gamma(k + 3/2)
    factorial_term = mp.factorial(k + 1)
    linear_term = 2 * k + 1
    gamma_term = mp.gamma(k + mp.mpf('3/2'))
    denominator = factorial_term * linear_term * gamma_term
    
    # Compute current term value
    term = numerator / denominator
    
    # Add term to the cumulative sum
    sum_result += term
    
    # Check if term magnitude is below precision threshold
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1

# Print result with exactly 10 decimal places
print(mp.nstr(sum_result, n=10))