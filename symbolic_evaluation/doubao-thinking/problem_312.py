import mpmath as mp

mp.dps = 15

sum_result = mp.mpf(0)
n = 0

while True:
    # Calculate sign (-1)^n
    sign = (-1) ** n
    
    # Compute (2n)!! / (2n+1)!! using factorials
    numerator_ratio = (2 ** (2 * n)) * (mp.factorial(n) ** 2)
    denominator_ratio = mp.factorial(2 * n + 1)
    double_fact_ratio = numerator_ratio / denominator_ratio
    
    # Compute denominator components: (2n+1) * 2^(4n+3) )
    denominator_term = (2 * n + 1) * (2 ** (4 * n + 3))
    
    # Combine all components for the term
    term = sign * mp.pi * double_fact_ratio / denominator_term
    
    # Add term to the sum and check convergence
    sum_result += term
    if mp.fabs(term) < 1e-15:
        break
    
    n += 1

print(mp.nstr(sum_result, n=10))