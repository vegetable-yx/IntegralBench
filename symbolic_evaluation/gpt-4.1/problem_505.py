import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant pi from mpmath
pi_value = mp.pi

# Calculate the expression: π/4
result = pi_value / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))