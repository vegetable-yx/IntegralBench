import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_total = mp.mpf(0)
k = 0
epsilon = mp.mpf('1e-15')  # Convergence threshold

while True:
    # Calculate binomial coefficient (2k+1 choose k)
    binom = mp.binomial(2*k + 1, k)
    
    # Compute denominator components
    denom_part1 = mp.mpf(k + 1)
    denom_part2 = mp.power(4, k)  # 4^k as mpf
    fact_k = mp.factorial(k)
    denom_part3 = mp.power(mp.mpf(fact_k), 2)  # (k!)^2 as mpf
    
    denominator = denom_part1 * denom_part2 * denom_part3
    term = mp.mpf(binom) / denominator  # Ensure term is mpf
    
    sum_total += term
    
    # Check for convergence
    if mp.fabs(term) < epsilon:
        break
    
    k += 1

# Multiply sum by π/8 and print result
result = (mp.pi / 8) * sum_total
print(mp.nstr(result, n=10))