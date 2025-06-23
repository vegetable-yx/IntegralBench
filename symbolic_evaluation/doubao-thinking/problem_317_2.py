import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate 2√2
two_sqrt2 = 2 * mp.sqrt(2)

# First term: π²/(2√2)
term1 = pi_squared / two_sqrt2

# Calculate 8√2
eight_sqrt2 = 8 * mp.sqrt(2)

# Second term: 8√2/3
term2 = eight_sqrt2 / 3

# Final result calculation
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))