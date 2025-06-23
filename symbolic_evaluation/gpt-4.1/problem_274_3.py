import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)  # Initialize sum to zero with mpmath precision
k = 0  # Start summation index at 0

while True:
    # Calculate numerator components: 10^(2k) * (k+2)! * k!
    power_term = mp.power(10, 2 * k)
    fac_k_plus_2 = mp.fac(k + 2)
    fac_k = mp.fac(k)
    numerator = power_term * fac_k_plus_2 * fac_k
    
    # Calculate denominator components: (2k)! * 2 * (3 + 2k)!
    fac_2k = mp.fac(2 * k)
    fac_3_plus_2k = mp.fac(3 + 2 * k)
    denominator = fac_2k * 2 * fac_3_plus_2k
    
    # Compute term and add to sum
    term = numerator / denominator
    sum_result += term
    
    # Break loop if term is smaller than 1e-15 (sufficient for 10 decimal precision)
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1  # Increment index for next term

# Multiply the accumulated sum by 250 to get final result
result = 250 * sum_result

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))