import mpmath as mp

mp.dps = 15  # Set internal precision

sum_result = mp.mpf(0)
k = 1
tolerance = mp.mpf('1e-20')  # Convergence threshold

while True:
    k_mp = mp.mpf(k)
    # Calculate numerator components
    numerator_part1 = 2 * k_mp + 1
    numerator_part2 = 2 * k_mp + 3
    numerator = numerator_part1 * numerator_part2
    
    # Calculate denominator components
    denom_term1 = (k_mp + 1)
    denom_term2 = k_mp ** 2
    denom_term3 = (k_mp + 2) ** 2
    denom_term4 = mp.power(4, k_mp)  # Use mpmath power for precision
    
    denominator = denom_term1 * denom_term2 * denom_term3 * denom_term4
    
    term = numerator / denominator
    sum_result += term
    
    # Check for convergence
    if mp.fabs(term) < tolerance:
        break
    
    k += 1

# Multiply by π/32 and print result
final_result = sum_result * mp.pi / 32
print(mp.nstr(final_result, n=10))