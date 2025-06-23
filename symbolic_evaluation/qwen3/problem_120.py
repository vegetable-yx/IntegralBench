import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi cubed
pi_power3 = mp.pi ** 3

# Divide by 8 to get final result
result = pi_power3 / 8

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))