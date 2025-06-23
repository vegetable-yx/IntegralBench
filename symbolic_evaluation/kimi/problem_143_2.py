import mpmath as mp

mp.dps = 15

sum_result = mp.mpf(0)
k = 0

while True:
    # Calculate factorial of k
    factorial_k = mp.factorial(k)
    
    # Compute denominator_part1 = 1/(k! * Γ(k+1)) which simplifies to 1/(k!^2)
    denominator_part1 = factorial_k ** 2
    
    # Compute denominator_part2 = 1/(2k+2)
    denominator_part2 = 2 * (k + 1)
    
    # Calculate double factorial terms (2k+1)!! and (2k+2)!!
    numerator_double = mp.fac2(2*k + 1)
    denominator_double = mp.fac2(2*k + 2)
    
    # Compute the ratio of double factorials
    ratio_double = numerator_double / denominator_double
    
    # Calculate the term for current k
    term = (1 / denominator_part1) * (1 / denominator_part2) * ratio_double * (mp.pi / 2)
    
    # Add term to the cumulative sum
    sum_result += term
    
    # Check if term is below precision target
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1

# Print result with exactly 10 decimal places
print(mp.nstr(sum_result, n=10))