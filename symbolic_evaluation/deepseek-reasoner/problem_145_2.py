import mpmath as mp

mp.dps = 15  # Set internal precision

sum_result = mp.mpf(0)
k = 0
while True:
    # Calculate numerator: 2^(2k) = 4^k
    numerator = mp.power(4, k)
    
    # Calculate denominator components
    fact_k = mp.factorial(k)
    fact_kp1 = mp.factorial(k + 1)
    linear_term = 2*k + 1
    fact_2kp1 = mp.factorial(2*k + 1)
    
    # Combine denominator components
    denominator = fact_k * fact_kp1 * linear_term * fact_2kp1
    
    # Calculate current term and add to sum
    term = numerator / denominator
    sum_result += term
    
    # Break when term becomes smaller than 1e-15
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1

print(mp.nstr(sum_result, n=10))