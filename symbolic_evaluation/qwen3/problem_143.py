import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)
k = 0

while True:
    # Calculate numerator (2k+1)!
    numerator = mp.factorial(2 * k + 1)
    
    # Calculate denominator components
    two_power = mp.mpf(2) ** (2 * k)  # 2^(2k)
    k_plus_1_sq = mp.mpf(k + 1) ** 2  # (k+1)^2
    fact_k_pow4 = mp.factorial(k) ** 4  # (k!)^4
    
    # Combine denominator components
    denominator = two_power * k_plus_1_sq * fact_k_pow4
    
    # Compute current term and add to sum
    term = numerator / denominator
    sum_result += term
    
    # Break loop if term is smaller than 1e-25
    if mp.fabs(term) < 1e-25:
        break
    
    k += 1

# Multiply sum by pi/8 and print result
result = (mp.pi / 8) * sum_result
print(mp.nstr(result, n=10))