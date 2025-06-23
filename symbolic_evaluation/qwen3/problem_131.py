import mpmath as mp

mp.dps = 15

# Calculate the constant factor sqrt(2π)/2
constant = mp.sqrt(2 * mp.pi) / 2

# Initialize series sum and variables
sum_series = mp.mpf(0)
k = 0
epsilon = mp.mpf('1e-20')  # Convergence threshold

# Compute infinite series terms until they become negligible
while True:
    # Calculate numerator (2k+2)!
    numerator = mp.fac(2*k + 2)
    
    # Calculate denominator [(k+1)!]^2 * [k!]^2
    fac_k_plus_1 = mp.fac(k + 1)
    fac_k = mp.fac(k)
    denominator = (fac_k_plus_1**2) * (fac_k**2)
    
    # Compute current term and add to sum
    term = numerator / denominator * (mp.mpf(1)/16)**k
    sum_series += term
    
    # Check if term is below precision threshold
    if mp.fabs(term) < epsilon:
        break
    k += 1

# Multiply accumulated sum by constant factor
result = constant * sum_series

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))