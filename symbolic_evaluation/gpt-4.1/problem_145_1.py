import mpmath as mp

mp.dps = 15  # Set internal precision

sqrt_pi = mp.sqrt(mp.pi)
sum_result = mp.mpf(0)
k = 0

while True:
    # Calculate numerator components
    four_power_k = 4**k
    numerator = four_power_k * sqrt_pi
    
    # Calculate denominator components
    gamma_k_plus_2 = mp.gamma(k + 2)  # (k+1)!
    gamma_k_plus_3_2 = mp.gamma(k + 1.5)
    denominator = gamma_k_plus_2 * (2*k + 1) * gamma_k_plus_3_2
    
    # Compute current term
    term = numerator / denominator
    sum_result += term
    
    # Check convergence (term < 1e-15)
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1

print(mp.nstr(sum_result, n=10))