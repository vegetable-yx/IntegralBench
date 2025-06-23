import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by pi
pi_times_sqrt2 = mp.pi * sqrt_2

# Multiply by 5 and divide by 8
result = (5 * pi_times_sqrt2) / 8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))