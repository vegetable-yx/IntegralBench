import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.power(mp.pi, 3)

# Multiply by 3
numerator = 3 * pi_cubed

# Divide by 128 to get final result
result = numerator / 128

# Print result to 10 decimal places
print(mp.nstr(result, n=10))