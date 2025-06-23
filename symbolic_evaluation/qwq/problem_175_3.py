import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Calculate natural logarithm of 4/3 with high precision
log_term = mp.log(mp.mpf(4)/3)

# Compute the coefficient part (2*ln(4/3) - 0.5)
coefficient = 2 * log_term - mp.mpf('0.5')

# Multiply by π to get final result
result = mp.pi * coefficient

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))