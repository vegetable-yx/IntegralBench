import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)  # Initialize the summation variable
k = 0  # Start summation index at 0
tolerance = mp.mpf('1e-20')  # Term magnitude threshold for stopping

while True:
    # Calculate numerator (2k+1)!
    numerator = mp.factorial(2 * k + 1)
    
    # Calculate denominator components
    denom_power = mp.power(4, k)  # 4^k term
    denom_factorial = mp.power(mp.factorial(k), 4)  # (k!)^4 term
    denom_square = mp.power(k + 1, 2)  # (k+1)^2 term
    
    # Combine denominator components
    denominator = denom_power * denom_factorial * denom_square
    
    # Calculate current term value
    term = numerator / denominator
    
    # Add term to summation
    sum_result += term
    
    # Check if term is below precision threshold
    if mp.fabs(term) < tolerance:
        break
    
    k += 1  # Increment index for next term

# Multiply summation by π/8 to get final result
result = (mp.pi / 8) * sum_result

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))