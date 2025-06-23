import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Initialize the sum with the first term (n=0)
sum_total = mp.mpf(1)
current_term = mp.mpf(1)
n = 1
eps = mp.mpf('1e-15')  # Convergence threshold

while True:
    # Calculate the ratio for the next term using recurrence relation
    ratio_numerator = 2 * n + 1
    ratio_denominator = 2 * n * (n + 1)**2
    next_term = current_term * (ratio_numerator / ratio_denominator)
    
    # Break loop if next term is below precision threshold
    if mp.fabs(next_term) < eps:
        break
    
    sum_total += next_term
    current_term = next_term
    n += 1

# Multiply the sum by π/8 to get the final result
result = (mp.pi / 8) * sum_total

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))