import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi to sufficient precision
pi_val = mp.pi

# Calculate pi raised to the 4th power
pi_4 = mp.power(pi_val, 4)

# Multiply by 5 for the numerator
numerator = 5 * pi_4

# Divide by the denominator 336
result = numerator / 336

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))