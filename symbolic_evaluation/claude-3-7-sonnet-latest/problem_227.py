import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Multiply by 7
numerator = 7 * pi_cubed

# Divide by 48 to get the result
result = numerator / 48

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))