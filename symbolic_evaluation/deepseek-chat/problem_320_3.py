import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the constant pi from mpmath
pi_value = mp.pi

# Compute the expression: π/2
result = pi_value / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))