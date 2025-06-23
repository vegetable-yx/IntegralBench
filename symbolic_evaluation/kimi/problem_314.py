import mpmath as mp

mp.dps = 15  # Initialize sum and variables
sum_result = mp.mpf(0)
k = 0
tolerance = mp.mpf('1e-25')

while True:
    # Calculate the current term's denominator components
    two_k_plus_1 = 2 * k + 1
    exponent = 2 * k + 1
    
    # Compute denominator using mpmath for high precision
    denominator = mp.power(mp.mpf(two_k_plus_1), 3) * mp.power(2, exponent)
    
    # Calculate the current term and add to sum
    term = mp.one / denominator
    sum_result += term
    
    # Break loop if term is below tolerance
    if term < tolerance:
        break
    
    k += 1

# Multiply by -2 to get the final result
result = -2 * sum_result

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))