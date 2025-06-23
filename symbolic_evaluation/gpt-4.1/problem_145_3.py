import mpmath as mp

mp.dps = 15  # Set internal precision

sum_result = mp.mpf(0)  # Initialize the sum
k = 0  # Start summation index at 0

while True:
    # Calculate factorial part (k+1)!
    factorial_part = mp.factorial(k + 1)
    
    # Calculate Gamma(k + 3/2)
    gamma_part = mp.gamma(k + 1.5)
    
    # Compute denominator components
    denominator = factorial_part * (2*k + 1) * gamma_part
    
    # Calculate current term in the series
    current_term = 1 / denominator
    
    # Add current term to the sum
    sum_result += current_term
    
    # Check if term is smaller than 1e-15 to ensure 10 decimal precision
    if mp.fabs(current_term) < 1e-15:
        break
    
    k += 1  # Increment index for next term

# Multiply sum by sqrt(pi)/2 to get final result
result = (mp.sqrt(mp.pi) / 2) * sum_result

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))