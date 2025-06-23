import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_part = mp.mpf(0)
four = mp.mpf(4)
k = 0

while True:
    # Calculate components of the current term
    k_plus1 = mp.mpf(k + 1)
    k_plus2 = mp.mpf(k + 2)
    numerator = (k_plus1 ** 2) * k_plus2 * (four ** (k + 2))
    denominator = mp.factorial(2 * k + 4)
    term = numerator / denominator
    
    sum_part += term  # Add current term to the sum
    
    # Break loop if term is smaller than 1e-15
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1

# Compute the prefactor and final result
prefactor = 4 * mp.sqrt(2) / mp.sqrt(mp.pi)
result = prefactor * sum_part

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))