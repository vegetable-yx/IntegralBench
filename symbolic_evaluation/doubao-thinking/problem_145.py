import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

result = mp.mpf(0)  # Initialize sum
k = 0               # Starting index
epsilon = mp.mpf(1e-15)  # Convergence threshold
four = mp.mpf(4)     # Constant base for numerator

while True:
    # Calculate numerator 4^k using mpmath power
    numerator = four ** k
    
    # Calculate denominator components
    factorial_term = mp.factorial(2*k + 1)  # (2k+1)!
    linear_term = 2*k + 1                   # (2k+1)
    k_term = k + 1                          # (k+1)
    
    # Combine denominator components
    denominator = k_term * factorial_term * linear_term
    
    # Compute current term value
    term = numerator / denominator
    
    # Add term to cumulative result
    result += term
    
    # Check for convergence
    if mp.fabs(term) < epsilon:
        break
    
    k += 1  # Increment index for next term

# Print result formatted to 10 decimal places
print(mp.nstr(result, n=10))