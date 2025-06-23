import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 16 to get final result
result = pi_cubed / 16

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))