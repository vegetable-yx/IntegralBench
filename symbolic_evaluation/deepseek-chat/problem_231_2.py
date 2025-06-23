import mpmath as mp

# Set internal decimal precision to 15 digits for calculations
mp.dps = 15

# Calculate pi constant
pi_value = mp.pi

# Compute pi divided by 2
result = pi_value / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))