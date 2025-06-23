import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the analytical expression: (3 * pi) / 4
pi_val = mp.pi            # Get the value of pi
numerator = 3 * pi_val    # Multiply pi by 3
result = numerator / 4    # Divide by 4 to get final result

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))