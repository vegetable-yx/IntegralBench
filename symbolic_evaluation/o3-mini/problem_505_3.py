import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Calculate the constant π
pi_value = mp.pi

# Compute the expression: π divided by 4
result = pi_value / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))