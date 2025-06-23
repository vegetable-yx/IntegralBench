import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

tolerance = 1e-20
max_m = 2000
max_n = 50
total = mp.mpf(0)

for m in range(0, max_m + 1):
    for n in range(0, max_n + 1):
        # Compute Pochhammer symbols (0.5)_m and (0.5)_n
        poch_m = mp.rf(0.5, m)
        poch_n = mp.rf(0.5, n)
        
        # Calculate factorials for the current m and n
        fact_m = mp.factorial(m)
        fact_n = mp.factorial(n)
        fact_m2 = mp.factorial(m + 2)
        fact_mn3 = mp.factorial(m + n + 3)
        
        # Compute numerator: [(0.5)_m * (0.5)_n]^2 * (m+2)!
        numerator = (poch_m * poch_n) ** 2 * fact_m2
        
        # Compute denominator: (m!)^2 * (n!)^2 * (m+n+3)!
        denominator = (fact_m ** 2) * (fact_n ** 2) * fact_mn3
        
        term_val = numerator / denominator
        
        # If the term is below tolerance, break the inner loop early
        if term_val < tolerance:
            break
            
        total += term_val

# Multiply by the constant factor pi^2 / 4
result = (mp.pi ** 2 / 4) * total

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))