import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.power(mp.pi, 3)

# Multiply by 3
numerator = 3 * pi_cubed

# Divide by 32 to get the result
result = numerator / 32

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))