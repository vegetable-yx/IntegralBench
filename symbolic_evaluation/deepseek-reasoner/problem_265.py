import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)  # Initialize the sum
k = 0  # Start summation index at 0

while True:
    # Calculate sign term (-1)^k
    sign = (-1) ** k
    
    # Calculate 2^(2k + 2) using mpmath power function
    power_term = mp.power(2, 2 * k + 2)
    
    # Calculate (k + 1) term
    k_plus_1 = k + 1
    
    # Compute numerator components
    numerator = sign * power_term * k_plus_1
    
    # Calculate denominator components
    factorial_k = mp.factorial(k)
    squared_term = mp.mpf(2 * k + 3) ** 2
    factorial_2k3 = mp.factorial(2 * k + 3)
    
    # Combine denominator parts
    denominator = factorial_k * squared_term * factorial_2k3
    
    # Compute current term in series
    term = numerator / denominator
    
    # Add term to cumulative sum
    sum_result += term
    
    # Check if term is smaller than 1e-15 to ensure 10 decimal precision
    if mp.fabs(term) < 1e-15:
        break
    
    # Increment index for next term
    k += 1

# Print result with exactly 10 decimal places
print(mp.nstr(sum_result, n=10))