import mpmath as mp

mp.dps = 15  # Set internal precision

# Initialize sum and variables for the series
series_sum = mp.mpf(0)
k = 0
epsilon = mp.mpf('1e-20')  # Convergence threshold

while True:
    # Calculate (-1)^k term
    sign = (-1) ** k
    
    # Compute factorial terms
    factorial_2k = mp.factorial(2*k)
    factorial_k4 = mp.factorial(k) ** 4
    
    # Calculate denominator component 4^k
    four_power_k = 4 ** k
    
    # Compute current term in the series
    term = (sign * factorial_2k) / (four_power_k * factorial_k4)
    
    # Add term to cumulative sum
    series_sum += term
    
    # Check for convergence
    if mp.fabs(term) < epsilon:
        break
    
    k += 1

# Calculate final result components
pi_over_4 = mp.pi / 4
one_minus_sum = 1 - series_sum
result = pi_over_4 * one_minus_sum

# Print with 10 decimal precision
print(mp.nstr(result, n=10))