import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

total = mp.mpf(0)  # Initialize sum for the series
k = 1  # Start with the first term

while True:
    # Calculate components of the term denominator
    two_k_minus_1 = mp.mpf(2*k - 1)  # (2k-1) term
    cubed_term = two_k_minus_1**3  # (2k-1)^3
    power_of_two = mp.power(2, 2*k - 1)  # 2^(2k-1)
    
    denominator = cubed_term * power_of_two  # Combine denominator parts
    term = mp.mpf(1) / denominator  # Compute current series term
    
    total += term  # Add term to cumulative sum
    
    # Break loop when term magnitude drops below precision threshold
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1  # Move to next term in series

result = -2 * total  # Apply final multiplicative constant
print(mp.nstr(result, n=10))  # Print result with 10 decimal places