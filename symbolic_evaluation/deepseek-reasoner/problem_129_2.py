import mpmath as mp
mp.dps = 15

# Initialize sum for the series
series_sum = mp.mpf(0)
m = 1
epsilon = mp.mpf('1e-20')  # Convergence threshold

# Calculate terms until they become smaller than epsilon
while True:
    numerator = mp.power(m, 2)
    denominator = mp.factorial(2*m + 1)
    term = numerator / denominator
    series_sum += term
    
    # Break loop when term is smaller than threshold
    if term < epsilon:
        break
    m += 1

# Multiply by 8*sqrt(2) for final result
result = 8 * mp.sqrt(2) * series_sum

# Print with 10 decimal precision
print(mp.nstr(result, n=10))