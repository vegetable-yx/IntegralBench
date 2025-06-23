import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

result = mp.mpf(0)
k = 0

while True:
    # Calculate factorial of k
    factorial_k = mp.factorial(k)
    
    # Compute denominator part 1: k! * Γ(k+1) = k! * k! = (k!)^2
    denominator_part1 = factorial_k ** 2
    
    # Compute denominator part 2: 2k+2
    denominator_part2 = 2 * (k + 1)
    
    # Compute double factorial terms
    double_fact_num = mp.factorial2(2 * k + 1)  # (2k+1)!!
    double_fact_den = mp.factorial2(2 * k + 2)  # (2k+2)!!
    ratio_double_fact = double_fact_num / double_fact_den
    
    # Combine all components for the term
    term = (1 / denominator_part1) * (1 / denominator_part2) * ratio_double_fact * (mp.pi / 2)
    
    result += term
    
    # Check if term is smaller than 1e-15 to ensure 10 decimal precision
    if mp.fabs(term) < mp.mpf('1e-15'):
        break
    
    k += 1

print(mp.nstr(result, n=10))