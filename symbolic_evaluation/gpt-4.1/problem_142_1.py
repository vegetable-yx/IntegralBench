import mpmath as mp

mp.dps = 15  # Set internal precision

total = mp.mpf(0)
k = 0

while True:
    # Calculate numerator: 4^k
    numerator = mp.power(4, k)
    
    # Calculate denominator components
    fact_k = mp.factorial(k)
    denominator_part1 = fact_k ** 2  # (k!)^2
    denominator_part2 = 2 * k + 1    # (2k+1)
    gamma_term = mp.gamma(k + 1.5)   # Γ(k + 3/2)
    
    # Combine denominator components
    denominator = denominator_part1 * denominator_part2 * gamma_term
    
    # Compute current term and add to total
    term = numerator / denominator
    total += term
    
    # Check if term is smaller than 1e-15 to break loop
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1

# Multiply by sqrt(pi)/2 as per the formula
result = (mp.sqrt(mp.pi) / 2) * total

# Print result to 10 decimal places
print(mp.nstr(result, n=10))