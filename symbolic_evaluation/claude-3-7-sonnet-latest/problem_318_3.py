import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi constant
pi_val = mp.pi

# Subtract 1 from pi
numerator = pi_val - 1

# Divide the result by 2
result = numerator / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))