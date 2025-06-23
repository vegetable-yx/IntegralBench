import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

result = mp.mpf(0)  # Initialize the result as an mpmath floating-point number
k = 0  # Start summation from k=0

while True:
    # Calculate numerator components
    power_term = mp.power(2, 2 * k + 1)  # Compute 2^(2k+1)
    linear_term = k + 1  # (k+1) term
    
    # Calculate denominator components
    squared_term = mp.power(2 * k + 3, 2)  # (2k+3)^2
    factorial_term = mp.factorial(2 * k + 1)  # (2k+1)!
    
    # Compute the current term in the series
    term = (power_term * linear_term) / (squared_term * factorial_term)
    
    result += term  # Add current term to the result
    
    # Check if term is smaller than 1e-15 to ensure precision
    if mp.fabs(term) < mp.mpf('1e-15'):
        break
    
    k += 1  # Increment k for next iteration

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))