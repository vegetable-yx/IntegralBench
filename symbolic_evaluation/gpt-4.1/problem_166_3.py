import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/4
pi_val = mp.pi  # Get the constant pi
result = pi_val / 4  # Divide by 4 to get the result

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))