import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

total = mp.mpf(0)  # Initialize the total sum
n = 0              # Start with n=0
tolerance = 1e-15  # Terminate when term < 1e-15

while True:
    # Calculate each component of the series term
    numerator = 16**n * mp.gamma(n + mp.mpf('0.75')) * mp.gamma(n + mp.mpf('0.25'))
    denominator = mp.factorial(2 * n)
    term = numerator / denominator
    
    total += term  # Add the term to the total
    
    # Check if the term is smaller than the tolerance
    if mp.fabs(term) < tolerance:
        break
    
    n += 1  # Increment n for the next term

# Print the result with exactly 10 decimal places
print(mp.nstr(total, n=10))