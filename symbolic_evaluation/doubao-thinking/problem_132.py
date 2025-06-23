import mpmath as mp

mp.dps = 15  # Initialize sum and term variables
sum_result = mp.mpf(0)
k = 0

while True:
    # Calculate components of the current term
    factor = mp.mpf(2) ** (2 - k)  # 2^(2 - k)
    poly_part = (k + 1) * (k + 2)  # (k+1)(k+2)
    numerator = factor * poly_part  # Combine numerator parts
    
    denominator = mp.factorial(2*k + 4)  # Compute factorial denominator
    
    term = numerator / denominator  # Compute current term
    
    sum_result += term  # Add term to the sum
    
    # Check if term is below precision threshold
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1  # Increment k for next iteration

# Print result to 10 decimal places
print(mp.nstr(sum_result, n=10))