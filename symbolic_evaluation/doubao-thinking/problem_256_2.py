import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by pi to get π√2
pi_sqrt2 = mp.pi * sqrt2

# Multiply by 3 to get 3π√2
three_pi_sqrt2 = 3 * pi_sqrt2

# Apply negative sign for final result
result = -three_pi_sqrt2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))