import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.power(mp.pi, 3)

# Multiply by 4
numerator = 4 * pi_cubed

# Divide by 3
result = numerator / 3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))