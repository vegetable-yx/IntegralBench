import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi to the fourth power
pi_4 = mp.pi**4

# Multiply by the numerator constant 3661
numerator = 3661 * pi_4

# Divide by the denominator 1125
result = numerator / 1125

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))