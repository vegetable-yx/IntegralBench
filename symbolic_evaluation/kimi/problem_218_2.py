import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 72 to get the result
result = pi_cubed / 72

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))