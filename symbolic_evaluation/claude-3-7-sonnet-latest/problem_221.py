import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant pi from mpmath
pi_val = mp.pi

# Calculate the numerator: 3 * pi
numerator = 3 * pi_val

# Compute the final result by dividing by 16
result = numerator / 16

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))