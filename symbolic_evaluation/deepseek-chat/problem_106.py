import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi/2 by accessing the constant mp.pi and dividing by 2
pi_val = mp.pi  # Get the value of pi
result = pi_val / 2  # Divide pi by 2 to get the result

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))