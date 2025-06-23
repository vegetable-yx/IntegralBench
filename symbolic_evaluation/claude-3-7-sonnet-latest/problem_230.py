import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate pi to the third power
pi_cubed = mp.pi ** 3

# Multiply by 5 to get the numerator
numerator = 5 * pi_cubed

# Divide by 192 to get the final result
result = numerator / 192

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))