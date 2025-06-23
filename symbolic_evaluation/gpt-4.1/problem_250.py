import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Multiply pi by 3
numerator = 3 * pi_val

# Divide the result by 8 to get the final value
result = numerator / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))