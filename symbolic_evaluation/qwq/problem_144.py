import mpmath as mp

mp.dps = 15  # Set internal precision

sum_result = mp.mpf(0)
m = 1

while True:
    # Calculate numerator components: 4^m and m^2
    power_term = mp.power(4, m)
    m_squared = mp.mpf(m ** 2)
    numerator = power_term * m_squared
    
    # Calculate denominator components: (2m+1) and (2m+1)!
    factorial_term = mp.fac(2 * m + 1)
    denominator_multiplier = mp.mpf(2 * m + 1)
    denominator = denominator_multiplier * factorial_term
    
    # Compute current term and add to sum
    term = numerator / denominator
    sum_result += term
    
    # Break loop if term is below precision threshold
    if term < 1e-15:
        break
    
    m += 1

# Print result with exactly 10 decimal places
print(mp.nstr(sum_result, n=10))