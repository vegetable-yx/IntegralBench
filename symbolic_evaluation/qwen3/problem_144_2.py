import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

result = mp.mpf(0)  # Initialize the result to 0
k = 0  # Start summation from k=0

while True:
    # Calculate numerator components
    four_power = mp.mpf(4) ** (k + 1)
    k_sq = (k + 1) ** 2
    numerator = four_power * k_sq
    
    # Calculate denominator components
    denominator_base = (2 * k + 3) ** 2
    factorial_term = mp.factorial(2 * k + 2)
    denominator = denominator_base * factorial_term
    
    # Compute current term and add to result
    term = numerator / denominator
    result += term
    
    # Check if term is smaller than 1e-15 to break the loop
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1  # Increment k for next iteration

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))